import pandas as pd

from src.constants.skill_mul_columns import SKILL_MUL_COLUMNS
from src.services.skill_mul_table_builder import SkillMulTableBuilder


def test_get_skill_mul_table(monkeypatch):
    mock_table = {
        "operator1": [10, 20, 30],
        "operator2": [40, 50, 60],
    }

    monkeypatch.setattr(
        SkillMulTableBuilder,
        "_get_data",
        staticmethod(lambda: mock_table)
    )

    actual = SkillMulTableBuilder.get_skill_mul_table()

    expected = pd.DataFrame.from_dict(
        mock_table,
        orient="index",
        columns=SKILL_MUL_COLUMNS
    )

    pd.testing.assert_frame_equal(actual, expected)