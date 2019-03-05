#!/usr/bin/env python
# coding: utf-8
# Copyright 2019 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import datetime
import logging
import os
import sys
import unittest

# Sets up environment.
import test_env_handlers

import webtest

import handlers_backend
from components import utils
from server import bot_management
from server import task_result


class BackendTest(test_env_handlers.AppTestBase):
  def _GetRoutes(self):
    """Returns the list of all routes handled."""
    return [
        r.template for r in self.app.app.router.match_routes
    ]

  def setUp(self):
    super(BackendTest, self).setUp()
    # By default requests in tests are coming from bot with fake IP.
    self.app = webtest.TestApp(
        handlers_backend.create_application(True),
        extra_environ={
          'REMOTE_ADDR': self.source_ip,
          'SERVER_SOFTWARE': os.environ['SERVER_SOFTWARE'],
        })
    self._enqueue_task_orig = self.mock(
        utils, 'enqueue_task', self._enqueue_task)

  def _enqueue_task(self, *args, **kwargs):
    return self._enqueue_task_orig(*args, use_dedicated_module=False, **kwargs)

  def testCronJobTasks(self):
    # Tests all the cron tasks are securely handled.
    prefix = '/internal/cron/'
    cron_job_urls = [r for r in self._GetRoutes() if r.startswith(prefix)]
    self.assertTrue(cron_job_urls)

    for cron_job_url in cron_job_urls:
      rest = cron_job_url[len(prefix):]
      section = rest.split('/', 2)[0]
      self.assertIn(section, ('cleanup', 'monitoring', 'important'), rest)
      self.app.get(
          cron_job_url, headers={'X-AppEngine-Cron': 'true'}, status=200)

      # Only cron job requests can be gets for this handler.
      response = self.app.get(cron_job_url, status=403)
      self.assertEqual(
          '403 Forbidden\n\nAccess was denied to this resource.\n\n '
          'Only internal cron jobs can do this  ',
          response.body)
    # The actual number doesn't matter, just make sure they are unqueued.
    self.execute_tasks()

  def testCronBotsAggregateTask(self):
    # Tests that the aggregation works
    now = datetime.datetime(2010, 1, 2, 3, 4, 5)
    self.mock_now(now)

    bot_management.bot_event(
        event_type='bot_connected', bot_id='id1',
        external_ip='8.8.4.4', authenticated_as='bot:whitelisted-ip',
        dimensions={'foo': ['beta'], 'id': ['id1']}, state={'ram': 65},
        version='123456789', quarantined=False, maintenance_msg=None,
        task_id=None, task_name=None)
    bot_management.bot_event(
        event_type='bot_connected', bot_id='id2',
        external_ip='8.8.4.4', authenticated_as='bot:whitelisted-ip',
        dimensions={'foo': ['alpha'], 'id': ['id2']}, state={'ram': 65},
        version='123456789', quarantined=True, maintenance_msg=None,
        task_id='987', task_name=None)

    self.app.get('/internal/cron/monitoring/bots/aggregate_dimensions',
        headers={'X-AppEngine-Cron': 'true'}, status=200)
    actual = bot_management.DimensionAggregation.KEY.get()
    expected = bot_management.DimensionAggregation(
        key=bot_management.DimensionAggregation.KEY,
        dimensions=[
            bot_management.DimensionValues(
                dimension='foo', values=['alpha', 'beta'])
        ],
        ts=now)
    self.assertEqual(expected, actual)

  def testCronTagsAggregateTask(self):
    self.mock_default_pool_acl([])
    self.set_as_admin()
    now = datetime.datetime(2011, 1, 2, 3, 4, 5)
    self.mock_now(now)

    self.client_create_task_raw(tags=['alpha:beta', 'gamma:delta'])
    self.assertEqual(1, self.execute_tasks())
    self.client_create_task_raw(tags=['alpha:epsilon', 'zeta:theta'])
    self.assertEqual(0, self.execute_tasks())

    self.app.get('/internal/cron/monitoring/tasks/aggregate_tags',
        headers={'X-AppEngine-Cron': 'true'}, status=200)
    actual = task_result.TagAggregation.KEY.get()
    expected = task_result.TagAggregation(
        key=task_result.TagAggregation.KEY,
        tags=[
            task_result.TagValues(tag='alpha', values=['beta', 'epsilon']),
            task_result.TagValues(tag='gamma', values=['delta']),
            task_result.TagValues(tag='os', values=['Amiga']),
            task_result.TagValues(tag='pool', values=['default']),
            task_result.TagValues(tag='priority', values=['20']),
            task_result.TagValues(tag='service_account', values=['none']),
            task_result.TagValues(
                tag='swarming.pool.template', values=['none']),
            task_result.TagValues(
                tag='swarming.pool.version', values=['pools_cfg_rev']),
            task_result.TagValues(tag='user', values=['joe@localhost']),
            task_result.TagValues(tag='zeta', values=['theta']),
        ],
        ts=now)
    self.assertEqual(expected, actual)

  def testCronCountTaskBotDistributionHandler(self):
    self.mock_default_pool_acl([])
    self.set_as_admin()
    now = datetime.datetime(2011, 1, 2, 3, 4, 5)
    self.mock_now(now)

    self.client_create_task_raw(tags=['alpha:beta', 'gamma:delta'])
    self.assertEqual(1, self.execute_tasks())
    self.client_create_task_raw(tags=['alpha:epsilon', 'zeta:theta'])
    self.assertEqual(0, self.execute_tasks())

    self.app.get('/internal/cron/monitoring/count_task_bot_distribution',
        headers={'X-AppEngine-Cron': 'true'}, status=200)

  def testTaskQueueUrls(self):
    # Tests all the task queue tasks are securely handled.
    # TODO(maruel): Test mapreduce.
    task_queue_urls = sorted(
      r for r in self._GetRoutes() if r.startswith('/internal/taskqueue/')
      if not r.startswith('/internal/taskqueue/mapreduce/launch/')
    )
    # This help to keep queue.yaml and handlers_backend.py up to date.
    # Format: (<queue-name>, <base-url>, <argument>).
    task_queues = sorted(
      [
        ('cancel-task-on-bot',
          '/internal/taskqueue/important/tasks/cancel-task-on-bot', ''),
        ('cancel-tasks', '/internal/taskqueue/important/tasks/cancel', ''),
        ('delete-tasks', '/internal/taskqueue/cleanup/tasks/delete', ''),
        ('es-notify-tasks',
          '/internal/taskqueue/important/external_scheduler/notify-tasks', ''),
        ('machine-provider-manage',
        '/internal/taskqueue/important/machine-provider/manage', ''),
        ('pubsub', '/internal/taskqueue/important/pubsub/notify-task/',
          'abcabcabc'),
        ('rebuild-task-cache',
          '/internal/taskqueue/important/task_queues/rebuild-cache', ''),
        ('tsmon', '/internal/taskqueue/monitoring/tsmon/', 'executors'),
        ('named-cache-task',
          '/internal/taskqueue/important/named_cache/update-pool', ''),
      ],
      key=lambda x: x[1])
    self.assertEqual(len(task_queues), len(task_queue_urls))
    for i, url in enumerate(task_queue_urls):
      self.assertTrue(
          url.startswith(task_queues[i][1]),
          '%s does not start with %s' % (url, task_queues[i][1]))

    for _, url, arg in task_queues:
      self.app.post(
          url+arg, headers={'X-AppEngine-QueueName': 'bogus name'}, status=403)


if __name__ == '__main__':
  if '-v' in sys.argv:
    unittest.TestCase.maxDiff = None
  logging.basicConfig(
      level=logging.DEBUG if '-v' in sys.argv else logging.CRITICAL,
      format='%(levelname)-7s %(filename)s:%(lineno)3d %(message)s')
  unittest.main()