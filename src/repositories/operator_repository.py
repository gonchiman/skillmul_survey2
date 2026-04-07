from src.entities.operator_base import OperatorBase
from src.constants.operator_names import OperatorNames
from src.repositories.operator_registry import OPERATORS


class OperatorRepository:
    @classmethod
    def get_by_id(cls, name: OperatorNames) -> OperatorBase:
        if name not in OPERATORS:
            raise ValueError("operator not found")
        return OPERATORS[name]