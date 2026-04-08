from flask import Flask, render_template, request

from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition
from src.services.skill_mul_service import SkillMulService


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        page_title="Endfield WikiWiki"
    )

@app.route("/skill_mul", methods=["GET", "POST"])
def skill_mul_page():
    selected_operator_name = request.form.get("operator_name", list(OperatorNames)[0].value)
    selected_skill_type = request.form.get("skill_type", list(SkillType)[0].value)

    operator_name = OperatorNames(selected_operator_name)
    skill_type = SkillType(selected_skill_type)

    cond = SkillMulCondition(
        operator_name=operator_name,
        skill_type=skill_type,
    )
    skill_mul = SkillMulService.get_skill_mul(cond)
    
    return render_template(
        "skill_mul_search.html",
        page_title="Skill Multiple Search",
        operator_names=OperatorNames,
        skill_types=SkillType,
        selected_operator_name=selected_operator_name,
        selected_skill_type=selected_skill_type,
        skill_mul=skill_mul,
    )

if __name__ == "__main__":
    app.run(debug=True)