from app import app


def test_skill_mul_page_get_returns_200():
    client = app.test_client()
    response = client.get("/skill_mul")

    assert response.status_code == 200


def test_skill_mul_page_post_displays_skill_mul():
    client = app.test_client()
    response = client.post("/skill_mul", data={
        "operator_name": "rossi",
        "skill_type": "battle",
        "skill_id": "1",
        "stack": "4"
    })

    assert response.status_code == 200 
    assert b"480" in response.data