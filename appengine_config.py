# Copyright 2013 The Swarming Authors. All rights reserved.
# Use of this source code is governed by the Apache v2.0 license that can be
# found in the LICENSE file.

"""Configures appstats.

https://developers.google.com/appengine/docs/python/tools/appengineconfig
"""

# The app engine headers are located locally, so don't worry about not finding
# them.
# pylint: disable=E0611,F0401
from google.appengine.api import app_identity
# pylint: enable=E0611,F0401


# Enable appstats and optionally cost calculation on a dev instance.
enable_appstats = app_identity.get_application_id().endswith('-dev')
appstats_CALC_RPC_COSTS = False


def webapp_add_wsgi_middleware(app):
  """Overrides the wsgi application with appstats if enabled.

  https://developers.google.com/appengine/docs/python/tools/appstats
  """
  if enable_appstats:
    # pylint: disable=E0611,F0401
    from google.appengine.ext.appstats import recording
    return recording.appstats_wsgi_middleware(app)

  return app
