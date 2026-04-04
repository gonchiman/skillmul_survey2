from app import app


def test_skill_mul_page_get_returns_200():
    client = app.test_client()

    response = client.get("/skill_mul")

    assert response.status_code == 200
    assert b"Skill Multiple Search Page" in response.data


def test_skill_mul_page_post_displays_skill_mul():
    client = app.test_client()

    response = client.post("/skill_mul", data={
        "operator_name": "lifeng",
        "skill_type": "battle",
        "skill_id": "1",
        "stack": "0"
    })

    assert response.status_code == 200 
    assert b"Skill Multiple Search Page" in response.data
    assert b"Skill Mul:" in response.data


def test_skill_mul_page_post_with_changed_selects_returns_200():
    client = app.test_client()

    response = client.post("/skill_mul", data={
        "operator_name": "lifeng",
        "skill_type": "combo",
        "skill_id": "1",
        "stack": "0"
    })

    assert response.status_code == 200