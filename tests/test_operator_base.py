import pytest

from src.entities.operator_base import OperatorBase


class FakeOperator1(OperatorBase):
    BATTLE_SKILLS = [100, 150, 200]
    COMBO_SKILLS = [100, 150, 200]
    ULTIMATES = [100, 150, 200]
    BATTLE_SKILL_STACK_MUL = 100
    COMBO_SKILL_STACK_MUL = 100
    ULTIMATE_STACK_MUL = 100

class FakeOperator2(OperatorBase):
    BATTLE_SKILLS = [100, 150, 200]
    COMBO_SKILLS = [100, 150, 200]
    ULTIMATES = [100, 150, 200]


def test_get_skill_mul_without_stack():
    battle_skill_mul = FakeOperator1.get_battle_skill_mul(0)
    combo_skill_mul = FakeOperator1.get_combo_skill_mul(0)
    ultimate_mul = FakeOperator1.get_ultimate_mul(0)

    assert battle_skill_mul == sum([100, 150, 200])
    assert combo_skill_mul == sum([100, 150, 200])
    assert ultimate_mul == sum([100, 150, 200])

def test_get_skill_mul_with_stack():
    for i in range(0, 5):
        battle_skill_mul = FakeOperator1.get_battle_skill_mul(i)
        combo_skill_mul = FakeOperator1.get_combo_skill_mul(i)
        ultimate_mul = FakeOperator1.get_ultimate_mul(i)

        assert battle_skill_mul == sum([100, 150, 200]) + 100 * i
        assert combo_skill_mul == sum([100, 150, 200]) + 100 * i
        assert ultimate_mul == sum([100, 150, 200]) + 100 * i

def test_get_skill_mul_invalid_stack_1():
    stack = -1

    with pytest.raises(ValueError):
        FakeOperator1.get_battle_skill_mul(stack)

    with pytest.raises(ValueError):
        FakeOperator1.get_combo_skill_mul(stack)

    with pytest.raises(ValueError):
        FakeOperator1.get_ultimate_mul(stack)

def test_get_skill_mul_invalid_stack_2():
    stack = 1

    with pytest.raises(ValueError):
        FakeOperator2.get_battle_skill_mul(stack)

    with pytest.raises(ValueError):
        FakeOperator2.get_combo_skill_mul(stack)

    with pytest.raises(ValueError):
        FakeOperator2.get_ultimate_mul(stack)

def test_is_skill_stack_mul():
    assert FakeOperator1.is_battle_skill_stack_mul() == True
    assert FakeOperator1.is_combo_skill_stack_mul() == True
    assert FakeOperator1.is_ultimate_skill_stack_mul() == True
    assert FakeOperator2.is_battle_skill_stack_mul() == False
    assert FakeOperator2.is_combo_skill_stack_mul() == False
    assert FakeOperator2.is_ultimate_skill_stack_mul() == False