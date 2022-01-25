###############################################################################
# Copyright Kitware Inc. and Contributors
# Distributed under the Apache License, 2.0 (apache.org/licenses/LICENSE-2.0)
# See accompanying Copyright.txt and LICENSE files for details
###############################################################################
from danesfield.surface.curve_surface import Curved_building

def test_Curved_building_init():
    raise NotImplementedError()


def test_get_bottomsurface():
    raise NotImplementedError()


def test_add_topsurface():
    raise NotImplementedError()


def test_get_obj_string():
    raise NotImplementedError()


def test_get_top_string():
    raise NotImplementedError()


def test_get_flatsurface():
    assert Curved_building().get_flatsurface() == 'get_flatsurface'


def test_split_surface():
    assert Curved_building().split_surface() == 'split_surface'
