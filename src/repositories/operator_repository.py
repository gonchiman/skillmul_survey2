from src.constants.operator_names import OPERATORS, OperatorNames


class OperatorRepository:
    @classmethod
    def get_by_id(cls, name: OperatorNames):
        if name not in OPERATORS:
            raise ValueError("operator not found")
        return OPERATORS[name]