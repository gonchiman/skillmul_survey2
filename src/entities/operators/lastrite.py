from src.entities.operator_base import OperatorBase


class Lastrite(OperatorBase):
    BATTLE_SKILLS = (320,)
    COMBO_SKILLS = (160, 160)
    ULTIMATES = (400, 400, 800)
    COMBO_SKILL_STACK_MUL = 240