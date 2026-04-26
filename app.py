from flask import Flask, render_template, request, send_file

from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition
from src.services.skill_mul_graph_service import SkillMulGraphService
from src.services.skill_mul_service import SkillMulService
from src.services.skill_mul_statistics_service_for_personal import SkillMulStatisticsServiceForPersonal


def get_skill_mul(operator_name: OperatorNames, skill_type: SkillType) -> int:
    cond = SkillMulCondition(
        operator_name=operator_name,
        skill_type=skill_type,
    )

    skill_mul_raw = SkillMulService.get_skill_mul(cond)
    skill_mul = skill_mul_raw if skill_mul_raw != 0 else "---"

    return skill_mul

def get_standard_score(operator_name: OperatorNames, skill_type: SkillType) -> float | str:
    cond = SkillMulCondition(
        operator_name=operator_name,
        skill_type=skill_type,
    )

    standard_score_raw = SkillMulStatisticsServiceForPersonal.get_standard_score(cond)
    standard_score = round(standard_score_raw, 2) if standard_score_raw is not None else "---"

    return standard_score


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        page_title="Home"
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

    skill_mul_raw = SkillMulService.get_skill_mul(cond)
    deviation_from_mean_raw = SkillMulStatisticsServiceForPersonal.get_deviation_from_mean(cond)
    deviation_from_median_raw = SkillMulStatisticsServiceForPersonal.get_deviation_from_median(cond)
    standard_score_raw = SkillMulStatisticsServiceForPersonal.get_standard_score(cond)

    skill_mul = skill_mul_raw if skill_mul_raw != 0 else "---"
    deviation_from_mean = round(deviation_from_mean_raw, 2) if deviation_from_mean_raw is not None else "---"
    deviation_from_median = round(deviation_from_median_raw, 2) if deviation_from_median_raw is not None else "---"
    standard_score = round(standard_score_raw, 2) if standard_score_raw is not None else "---"
    
    return render_template(
        "skill_mul_search.html",
        page_title="Skill Multiple Search",
        operator_names=OperatorNames,
        skill_types=SkillType,
        selected_operator_name=selected_operator_name,
        selected_skill_type=selected_skill_type,
        skill_mul=skill_mul,
        deviation_from_mean=deviation_from_mean,
        deviation_from_median=deviation_from_median,
        standard_score=standard_score,
    )

@app.route("/skill_mul_2", methods=["GET", "POST"])
def skill_mul_page_2():
    selected_operator_name = request.form.get("operator_name", list(OperatorNames)[0].value)
    selected_skill_type = request.form.get("skill_type", list(SkillType)[0].value)

    operator_name = OperatorNames(selected_operator_name)

    skill_mul_battle = get_skill_mul(operator_name, SkillType.BATTLE)
    standard_score_battle = get_standard_score(operator_name, SkillType.BATTLE)

    skill_mul_combo = get_skill_mul(operator_name, SkillType.COMBO)
    standard_score_combo = get_standard_score(operator_name, SkillType.COMBO)

    skill_mul_ultimate = get_skill_mul(operator_name, SkillType.ULTIMATE)
    standard_score_ultimate = get_standard_score(operator_name, SkillType.ULTIMATE)

    return render_template(
        "skill_mul_search_2.html",
        page_title="Skill Multiple Search",
        operator_names=OperatorNames,
        selected_operator_name=selected_operator_name,
        selected_skill_type=selected_skill_type,
        skill_mul_battle=skill_mul_battle,
        skill_mul_combo=skill_mul_combo,
        skill_mul_ultimate=skill_mul_ultimate,
        standard_score_battle=standard_score_battle,
        standard_score_combo=standard_score_combo,
        standard_score_ultimate=standard_score_ultimate,
    )

@app.route("/histogram/<skill_type>/<skill_mul>")
def histogram(skill_type, skill_mul):
    skill_type = SkillType(skill_type)

    if skill_mul == "---":
        skill_mul = None
    else:
        skill_mul = int(skill_mul)
        
    img = SkillMulGraphService.get_histogram(skill_type, skill_mul)
    return send_file(img, mimetype="image/png")

@app.route("/barplot/<skill_type>/<operator_name>")
def barblot(skill_type, operator_name):
    skill_type = SkillType(skill_type)
    operator_name = OperatorNames(operator_name)
        
    img = SkillMulGraphService.get_barplot(
        skill_type, 
        operator_name,
        ascending=False
    )
    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)