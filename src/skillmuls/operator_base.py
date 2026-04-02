class OperatorBase:
    BATTLE_SKILLS = {}
    COMBO_SKILLS = {}
    ULTIMATES = {}
    BATTLE_SKILL_STACK_MUL = None
    COMBO_SKILL_STACK_MUL = None
    ULTIMATE_STACK_MUL = None

    @classmethod
    def _calc_mul(cls, skill_table: dict, skill_id: int, stack: int, stack_mul: int | None) -> int:
        extra = 0
        if stack > 0:
            if stack_mul is None:
                raise ValueError("This operator doesn't support stack.")
            extra = stack_mul * stack
        return sum(skill_table[skill_id]) + extra
    
    @classmethod
    def get_battle_skill_mul(cls, skill_id: int, stack: int = 0) -> int:
        return cls._calc_mul(cls.BATTLE_SKILLS, skill_id, stack, cls.BATTLE_SKILL_STACK_MUL)

    @classmethod
    def get_combo_skill_mul(cls, skill_id: int, stack: int = 0) -> int:
        return cls._calc_mul(cls.COMBO_SKILLS, skill_id, stack, cls.COMBO_SKILL_STACK_MUL)

    @classmethod
    def get_ultimate_mul(cls, skill_id: int, stack: int = 0) -> int:
        return cls._calc_mul(cls.ULTIMATES, skill_id, stack, cls.ULTIMATE_STACK_MUL)