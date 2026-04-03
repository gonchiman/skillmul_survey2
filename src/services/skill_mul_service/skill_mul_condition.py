from dataclasses import dataclass

from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType


@dataclass
class SkillMulCondition:
    operator_name: OperatorNames
    skill_type: SkillType
    skill_id: int
    stack: int = 0
