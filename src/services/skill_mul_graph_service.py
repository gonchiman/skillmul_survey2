from io import BytesIO

import matplotlib

from src.constants.operator_names import OperatorNames, OPERATOR_IDENTIFIERS
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from src.constants.skill_type import SkillType
from src.services.skill_mul_table_builder import SkillMulTableBuilder
from src.constants.skill_mul_columns import SkillMulColumns


class SkillMulGraphService:
    @staticmethod
    def get_histogram(
        skill_type: SkillType,
        skill_mul: int | None = None,
    ):        
        skill_mul_table = SkillMulTableBuilder.get_skill_mul_table()

        skill_mul_column = SkillMulGraphService._get_skill_mul_column(skill_type)
        data = skill_mul_table[skill_mul_column].dropna()

        min_class = (data.min() // 100) * 100
        max_class = (data.max() // 100) * 100 + 100

        bins = np.arange(min_class, max_class + 100, 100)

        fig, ax = plt.subplots()

        fig.patch.set_facecolor("gray")
        ax.set_facecolor("gray")

        _, bins, patches = ax.hist(data, bins=bins)

        ax.set_title(f"histogram ({skill_type.name})")
        ax.set_xlabel("skill multiplier")
        ax.set_ylabel("count")

        for p in patches:
            p.set_facecolor("lightgray")

        if skill_mul is not None:
            for i in range(len(bins) - 1):
                left = bins[i]
                right = bins[i + 1]

                if left <= skill_mul < right:
                    patches[i].set_facecolor("orange")

        buf = BytesIO()
        fig.savefig(buf, format="png")
        plt.close(fig)
        buf.seek(0)

        return buf

    @staticmethod
    def get_barplot(
        skill_type: SkillType,
        operator_name: OperatorNames | None = None,
        ascending: bool | None = None,
    ):
        skill_mul_table = SkillMulTableBuilder.get_skill_mul_table()

        if ascending is not None:
            skill_mul_table = SkillMulTableBuilder.sort_skill_mul_table(
                skill_mul_table=skill_mul_table,
                skill_type=skill_type,
                ascending=ascending,
            )

        skill_mul_column = SkillMulGraphService._get_skill_mul_column(skill_type)

        series = skill_mul_table[skill_mul_column].dropna()
        labels = [OPERATOR_IDENTIFIERS[operator] for operator in series.index]
        data = series.values

        fig, ax = plt.subplots()

        fig.patch.set_facecolor("gray")
        ax.set_facecolor("gray")

        bars = ax.bar(labels, data)

        ax.set_title(f"barplot ({skill_type.name})")
        ax.set_xlabel("operators")
        ax.set_ylabel("skill multiplier")
        ax.tick_params(axis="x", labelsize=8)

        for bar in bars:
            bar.set_color("lightgray")

        if operator_name is not None:
            for operator, bar in zip(series.index, bars):
                if operator == operator_name:
                    bar.set_color("orange")

        buf = BytesIO()
        fig.savefig(buf, format="png")
        plt.close(fig)
        buf.seek(0)

        return buf

    @staticmethod
    def _get_skill_mul_column(skill_type: SkillType) -> str:
        match skill_type:
            case SkillType.BATTLE:
                return SkillMulColumns.BATTLE
            case SkillType.COMBO:
                return SkillMulColumns.COMBO
            case SkillType.ULTIMATE:
                return SkillMulColumns.ULTIMATE
            case _:
                raise ValueError(f"Invalid skill_type: {skill_type}")