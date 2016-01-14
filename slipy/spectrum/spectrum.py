# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Copyright (c) Geoffrey Lentner 2016. All Rights Reserved.
# slipy/spectrum/spectrum.py

"""Spectrum class interface."""

from algorithms import *
from calibration import *
from core import *
from etc import *
from gui import *
from measurement import *
from operations import *

class Error(Exception):
    """Error specific to the spectrum object."""
    pass


class Spectrum:
    """
    """

    def __init__(self, *args, **kwargs):
        """
        """
        _init(self, *args, **kwargs)


    def copy(self):
        """
        """
        return _copy(self)


    def resample(self, *args, **kwargs):
        """
        """
        return _resample(self, *args, **kwargs)


    def insert(self, *args, **kwargs):
        """
        """
        return _insert(self, *args, **kwargs)


    def normalize(self, *args, **kwargs):
        """
        """
        return _normalize(self, *args, **kwargs)


    def remove_telluric(self, *args, **kwargs):
        """
        """
        return _remove_telluric(self, *args, **kwargs)


    def apply_velocity_correction(self, *args, **kwargs):
        """
        """
        return _apply_velocity_correction(self, *args, **kwargs)


    def draw(self, *args, **kwargs):
        """
        """
        return _draw(self, *args, **kwargs)


    def select_line(self, *args, **kwargs):
        """
        """
        return _select_line(self, *args, **kwargs)


    def extract_line(self, *args, **kwargs):
        """
        """
        return _extract_line(self, *args, **kwargs)


    def auto_fit(self, *args, **kwargs):
        """
        """
        return _auto_fit(self, *args, **kwargs)


    def fit(self, *args, **kwargs):
        """
        """
        return _fit(self, *args, **kwargs)


    def deblend(self, *args, **kwargs):
        """
        """
        return _deblend(self, *args, **kwargs)


    def optical_depth(self, *args, **kwargs):
        """
        """
        return _optical_depth(self, *args, **kwargs)


    def equivalent_width(self, *args, **kwargs):
        """
        """
        return _equivalent_width(self, *args, **kwargs)


    def column_density(self, *args, **kwargs):
        """
        """
        return _column_density(self, *args, **kwargs)


    def __getitem__(self, key):
        """
        """
        return _getitem(self, key):


    def __str__(self):
        """
        """
        return _str(self)


    def __repr__(self):
        """
        """
        return _repr(self)


    def __len__(self):
        """
        """
        return _len(self)


    def __contains__(self, other):
        """
        """
        return _contains(self, other)


    def __add__(self, other):
        """
        """
        return _add(self, other)


    def __sub__(self, other):
        """
        """
        return _sub(self, other)


    def __mul__(self, other):
        """
        """
        return _mul(self, other)


    def __truediv__(self, other):
        """
        """
        return _truediv(self, other)


    def __iadd__(self, other):
        """
        """
        return _iadd(self, other)


    def __isub__(self, other):
        """
        """
        return _isub(self, other)


    def __imul__(self, other):
        """
        """
        return _imul(self, other)


    def __itruediv__(self, other):
        """
        """
        return _itruediv(self, other)


    def __radd__(self, other):
        """
        """
        return _radd(self, other)


    def __rsub__(self, other):
        """
        """
        return _rsub(self, other)


    def __rmul__(self, other):
        """
        """
        return _rmul(self, other)

    def __rtruediv__(self, other):
        """
        """
        return _rtruediv(self, other)


    def __lshift__(self, other):
        """
        """
        return _lshift(self, other)

    def __rshift__(self, other):
        """
        """
        return _rshift(self, other)


    def __eq__(self, other):
        """
        """
        return _eq(self, other)


    def __ne__(self, other):
        """
        """
        return _ne(self, other)


    def __lt__(self, other):
        """
        """
        return _lt(self, other)


    def __gt__(self, other):
        """
        """
        return _gt(self, other)


    def __le__(self, other):
        """
        """
        return _le(self, other)


    def __ge__(self, other):
        """
        """
        return _ge(self, other)

    def __and__(self, other):
        """
        """
        return _and(self, other)


    def __or__(self, other):
        """
        """
        return _or(self, other)


    def __xor__(self, other):
        """
        """
        return _xor(self, other)


    def __rand__(self, other):
        """
        """
        return _rand(self, other)


    def __ror__(self, other):
        """
        """
        return _ror(self, other)


    def __rxor__(self, other):
        """
        """
        return _rxor(self, other)


    @classmethod
    def rms(cls, *args, **kwargs):
        """
        """
        return _rms(cls, *args, **kwargs)


    @classmethod
    def xcorr(cls, *args, **kwargs):
        """
        """
        return _xorr(cls, *args, **kwargs)
