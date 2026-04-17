from src.constants.operator_names import OperatorNames
from src.entities.operators.akekuri import Akekuri
from src.entities.operators.alesh import Alesh
from src.entities.operators.arclight import Arclight
from src.entities.operators.catcher import Catcher
from src.entities.operators.chen_qianyu import ChenQianyu
from src.entities.operators.ember import Ember
from src.entities.operators.endministrator import Endministrator
from src.entities.operators.estella import Estella
from src.entities.operators.lifeng import Lifeng
from src.entities.operators.pogranichnik import Pogranichnik
from src.entities.operators.rossi import Rossi
from src.entities.operators.snowshine import Snowshine


OPERATORS = {
    OperatorNames.LIFENG: Lifeng,
    OperatorNames.ROSSI: Rossi,
    OperatorNames.ENDMINISTRATOR: Endministrator,
    OperatorNames.CHEN_QIANYU: ChenQianyu,
    OperatorNames.ESTELLA: Estella,
    OperatorNames.POGRANICHNIK: Pogranichnik,
    OperatorNames.ALESH: Alesh,
    OperatorNames.ARCLIGHT: Arclight,
    OperatorNames.AKEKURI: Akekuri,
    OperatorNames.EMBER: Ember,
    OperatorNames.SNOWSHINE: Snowshine,
    OperatorNames.CATCHER: Catcher,
}