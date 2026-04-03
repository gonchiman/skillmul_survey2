from flask import Flask, render_template, request

from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.services.skill_mul_service.skill_mul_condition import SkillMulCondition
from src.services.skill_mul_service.skill_mul_service import SkillMulService


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skill_mul", methods=["GET", "POST"])
def skill_mul_page():
    if request.method == "POST":
        cond = SkillMulCondition(
            operator_name=OperatorNames(request.form["operator_name"]),
            skill_type=SkillType(request.form["skill_type"]),
            skill_id=int(request.form["skill_id"]),
            stack=int(request.form["stack"] or 0)
        )
        skill_mul = SkillMulService.get_skill_mul(cond)
        return render_template("skill_mul_search.html", skill_mul=skill_mul)
    
    return render_template("skill_mul_search.html")

if __name__ == "__main__":
    app.run(debug=True)