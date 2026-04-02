from dataclasses import dataclass

from skill_type import SkillType


@dataclass
class SkillMulCondition:
    operator_name: str
    skill_type: SkillType
    skill_id: int
    stack: int = 0
