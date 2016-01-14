# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# slipy/spectrum/core/__init__.py

"""core (functions) for Spectrum object.
"""

from .copy import _copy
from .from_array import _from_array
from .from_file import _from_file
from .init import _init
from .insert import _insert
from .resample import _resample

__all__ = [_copy, _from_array, _from_file, _init, _insert, _resample]
