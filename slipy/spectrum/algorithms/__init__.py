# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# slipy/spectrum/algorithms/__init__.py

"""algorithm (functions) for Spectrum object.
"""

from .rms import _rms
from .xcorr import _xcorr

__all__ = ('_rms', '_xcorr')
