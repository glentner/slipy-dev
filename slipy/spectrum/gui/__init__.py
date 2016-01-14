# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# slipy/spectrum/gui/__init__.py
# TODO: gui/__init__.py

"""gui (functions) for Spectrum object.
"""

from .auto_fit import _auto_fit
from .base import _base
from .deblend import _deblend
from .draw import _draw
from .extract_line import _extract_line
from .fit import _fit
from .select_line import _select_line

__all__ = [_auto_fit, _base, _deblend, _draw, _extract_line, _fit, _select_line]
