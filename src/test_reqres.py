import requests
import names
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
    name = names.get_first_name()
    body = {"name": name , "job": "leader"}
    response = requests.post(post_url, json = body)
    status = response.status_code
    assert status is 201
    text = response.json()
    assert text['name'] == name
    assert text['job'] == "leader"

def test_update_user():
    put_url = f"{base_url}/api/users/"
    name = names.get_last_name()
    body = {"name": name , "job": "zion resident"}
    response = requests.put(put_url, json = body)
    status = response.status_code
    assert status is 200
    text = response.json()
    assert text['name'] == name
    assert text['job'] == "zion resident"

def test_delete_user():
    delete_url = f"{base_url}/api/users/2"
    response = requests.delete(delete_url)
    status = response.status_code
    assert status is 204
    