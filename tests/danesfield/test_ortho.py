###############################################################################
# Copyright Kitware Inc. and Contributors
# Distributed under the Apache License, 2.0 (apache.org/licenses/LICENSE-2.0)
# See accompanying Copyright.txt and LICENSE files for details
###############################################################################
from danesfield.ortho import circ_structure, orthorectify, COMPLETE_DSM_INTERSECTION, PARTIAL_DSM_INTERSECTION, EMPTY_DSM_INTERSECTION, ERROR
import numpy


def test_circ_structure():
    raise NotImplementedError


def test_orthorectify():
    raise NotImplementedError


def test_COMPLETE_DSM_INTERSECTION():
    assert COMPLETE_DSM_INTERSECTION == 0


def test_PARTIAL_DSM_INTERSECTION():
    assert PARTIAL_DSM_INTERSECTION == 1


def test_EMPTY_DSM_INTERSECTION():
    assert EMPTY_DSM_INTERSECTION == 2


def test_ERROR():
    assert ERROR == 10
