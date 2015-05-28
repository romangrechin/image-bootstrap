# Copyright (C) 2015 Sebastian Pipping <sebastian@pipping.org>
# Licensed under AGPL v3 or later

from __future__ import print_function

import sys

try:
    from requests import get
except ImportError as e:
    print('ERROR: Please install Requests '
        '(https://pypi.python.org/pypi/requests).  '
        'Thank you!', file=sys.stderr)
    sys.exit(1)

del sys
