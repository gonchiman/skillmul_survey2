from src.constants.operator_names import OperatorNames
from src.entities.operators.lifeng import Lifeng
from src.entities.operators.rossi import Rossi


OPERATORS = {
    OperatorNames.LIFENG: Lifeng,
    OperatorNames.ROSSI: Rossi
}