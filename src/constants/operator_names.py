from enum import Enum

from src.entities.skill_muls.operators.lifeng import Lifeng


class OperatorNames(Enum):
    LIFENG = "lifeng"


OPERATORS = {
    OperatorNames.LIFENG: Lifeng
}