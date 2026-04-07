from enum import Enum

import pytest

from src.constants.operator_names import OperatorNames
from src.entities.operators.lifeng import Lifeng
from src.repositories.operator_repository import OperatorRepository


class FakeOperatorNames(Enum):
    FAKE = "fake"

def test_get_by_id_normal():
    assert OperatorRepository.get_by_id(OperatorNames.LIFENG) == Lifeng

def test_get_by_id_value_error_when_operator_not_found():
    with pytest.raises(ValueError):
        OperatorRepository.get_by_id(FakeOperatorNames.FAKE)