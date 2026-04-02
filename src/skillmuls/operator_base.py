class OperatorBase:
    BATTLE_SKILLS = {}
    COMBO_SKILLS = {}
    ULTIMATES = {}
    BATTLE_SKILL_STACK_MUL = None
    COMBO_SKILL_STACK_MUL = None
    ULTIMATE_STACK_MUL = None

    @classmethod
    def get_battle_skill_mul(cls, skill_id: int, stack: int = 0) -> int:
        stack_mul = 0
        if stack > 0 :
            if cls.BATTLE_SKILL_STACK_MUL is None:
                raise Exception("This operator doesn't have the SKILL_STACK_MUL.")
            else:
                stack_mul = cls.BATTLE_SKILL_STACK_MUL * stack
        return sum(cls.BATTLE_SKILLS[skill_id]) + stack_mul
    
    @classmethod
    def get_combo_skill_mul(cls, skill_id: int, stack: int = 0) -> int:
        stack_mul = 0
        if stack > 0 :
            if cls.COMBO_SKILL_STACK_MUL is None:
                raise Exception("This operator doesn't have the SKILL_STACK_MUL.")
            else:
                stack_mul = cls.COMBO_SKILL_STACK_MUL * stack
        return sum(cls.COMBO_SKILLS[skill_id]) + stack_mul
    
    @classmethod
    def get_ultimate_mul(cls, skill_id: int, stack: int = 0) -> int:
        stack_mul = 0
        if stack > 0 :
            if cls.ULTIMATE_STACK_MUL is None:
                raise Exception("This operator doesn't have the SKILL_STACK_MUL.")
            else:
                stack_mul = cls.ULTIMATE_STACK_MUL * stack
        return sum(cls.ULTIMATES[skill_id]) + stack_mul