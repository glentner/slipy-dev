# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# slipy/spectrum/calibration/__init__.py

"""calibration (functions) for Spectrum object.
"""

from .apply_velocity_correction import _apply_velocity_correction
from .normalize import _normalize
from .remove_telluric import _remove_telluric

__all__ = [_apply_velocity_correction, _normalize, _remove_telluric]
