import requests

base_url = "https://reqres.in"


def test_get_user_page2():
    get_url = f"{base_url}/api/users?page=2"
    response = requests.get(get_url)
    status = response.status_code
    assert status is 200, f"Actual status is {status}"
    text = response.json()
    assert text["page"] is 2
    assert text["total"] is 12
    assert text["data"][0]["id"] is 7
    assert text["data"][1]["id"] is 8
    assert text["data"][2]["id"] is 9
    assert text["data"][3]["id"] is 10
    assert text["data"][4]["id"] is 11
    assert text["data"][5]["id"] is 12


def test_create_user():
    post_url = f"{base_url}/api/users"
    body = {"name": "morpheus", "job": "leader"}
    response = requests.post(post_url, json = body)
    status = response.status_code
    assert status is 201
    text = response.json()
    assert text['name'] == "morpheus"
    assert text['job'] == "leader"
