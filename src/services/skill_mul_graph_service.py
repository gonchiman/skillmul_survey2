from io import BytesIO

import matplotlib
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

        match skill_type:
            case SkillType.BATTLE:
                skill_mul_column = SkillMulColumns.BATTLE
            case SkillType.COMBO:
                skill_mul_column = SkillMulColumns.COMBO
            case SkillType.ULTIMATE:
                skill_mul_column = SkillMulColumns.ULTIMATE
            case _:
                raise ValueError(f"Invalid skill_type: {skill_type}")

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