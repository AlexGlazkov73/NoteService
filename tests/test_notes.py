import json
from uuid import UUID


def is_valid_uuid(uuid_to_test):
    try:
        uuid_obj = UUID(uuid_to_test, version=4)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def test_create_note(test_app, example_note):
    response = test_app.post("/generate", json=example_note)
    assert response.status_code == 201
    assert is_valid_uuid(response.json().get('note_id'))


def test_create_note_invalid_json(test_app):
    request_payload = json.dumps({"t": "something"})
    response = test_app.post("/generate", content=request_payload)
    assert response.status_code == 422


def test_get_note_after_create(test_app, example_note):
    response = test_app.post("/generate", json=example_note)
    assert response.status_code == 201
    assert response.json().get('note_id')

    test_note_id = response.json()['note_id']
    response = test_app.get(f"/secrets/{test_note_id}")
    assert response.status_code == 200
    assert response.json()['text'] == 'Hello World!'

    response = test_app.get(f"/secrets/{test_note_id}")
    assert response.status_code == 404
    assert response.json()["message"] == "Note not found"


def test_read_note_incorrect_id(test_app):
    response = test_app.get("/secrets/ac3ca82d-cf38-4222-a5ce-9ee6d0432744")
    assert response.status_code == 404
    assert response.json()["message"] == "Note not found"

    response = test_app.get("/secrets/0")
    assert response.status_code == 422
