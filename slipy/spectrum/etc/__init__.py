# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# slipy/spectrum/etc/__init__.py

"""etc (functions) for Spectrum object.
"""

from .contains import _contains
from .getitem import _getitem
from .len import _len
from .repr import _repr
from .str import _str

__all__ = ('_contains', '_getitem', '_len', '_repr', '_str')
