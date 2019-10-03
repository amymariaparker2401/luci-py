# Copyright 2016 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

"""Common code for platforms."""

from collections import namedtuple

import six


def _safe_parse(content, split=': '):
  """Safely parse a 'key: value' list of strings from a command."""
  values = {}
  for l in content.splitlines():
    if not l:
      continue
    parts = l.split(split, 2)
    if len(parts) != 2:
      continue
    if six.PY2:
      parts = map(unicode, parts)
    values.setdefault(parts[0].strip(), parts[1])
  return values


ComputerSystemInfo = namedtuple('ComputerSystemInfo', [
    'name', 'vendor', 'version', 'serial'])
