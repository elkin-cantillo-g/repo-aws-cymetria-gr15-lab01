# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from .glir import GlirQueue

class GLObject(object):
    # Type of GLIR object, reset in subclasses
    _GLIR_TYPE: str = ...

    # Internal id counter to keep track of GPU objects
    _idcount: int = ...

    def __init__(self): ...
    def __del__(self): ...
    def delete(self): ...
    @property
    def id(self): ...
    @property
    def glir(self): ...
