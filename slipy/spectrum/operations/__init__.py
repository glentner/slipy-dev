# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# slipy/spectrum/operations/__init__.py

"""Spectrum operations.
"""

from .add import _add
from .and import _and
from .base import _base
from .eq import _eq
from .ge import _ge
from .iadd import _iadd
from .imul import _imul
from .isub import _isub
from .itruediv import _itruediv
from .lshift import _lshift
from .lt import _lt
from .mul import _mul
from .ne import _ne
from .radd import _radd
from .rmul import _rmul
from .rshift import _rshift
from .rsub import _rsub
from .rtruediv import _rtruediv
from .sub import _sub
from .truediv import _truediv

__all__ = [_add, _and, _base, _eq, _ge, _iadd, _imul, _isub, _itruediv, _lshift, _lt,
    _mul, _ne, _radd, _rmul, _rshift, _rsub, _rshift, _rsub, _rtruediv, _sub, _truediv]
