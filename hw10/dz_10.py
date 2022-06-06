import json
import string
import random
import requests

URL = ["https://www.aqa.science/", "https://www.aqa.science/users/"]
USER = "xxxxx"
PASSWORD = "xxxxx"

first_response = requests.get(URL[0]).json()

results = []


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def create_user_creds():
    users = {"login": "", "password": ""}
    for i in users:
        users[i] = generate_random_string(15)

    return users


def get_user_list(users_url):
    global results
    response = requests.get(users_url, auth=(USER, PASSWORD))
    initial_object = response.json()
    results += initial_object["results"]
    next_ = initial_object["next"]
    if next_:
        get_user_list(next_)
    with open("../response.json", "w") as f:
        json.dump(results, f)
    return response


def add_user():
    users = create_user_creds()
    params = {'username': users['login']}
    new_user_response = requests.post('https://www.aqa.science/users/', auth=(USER, PASSWORD),
                                      data=params)
    get_user_list(URL[1])
    new_user_data = new_user_response.json()
    new_user_link = str(new_user_data["url"])
    users_list = json.load(open('../response.json', 'r'))
    response = new_user_response.status_code
    for i in users_list:
        for key, value in i.items():
            if new_user_link in value:
                user_id = str(new_user_data["url"]).split("/")[-2]
                assert response == 201
                print(f"User with id {user_id} is added. Link: {new_user_link}")
            elif value == False:
                print("User is not added")
            else:
                continue



def read_users():
    get_user_list(URL[1])
    current_users_list = json.load(open('../response.json', 'r'))

    for i in current_users_list:
        for key, value in i.items():
            if 'url' in key:
                current_users_link = value
                current_user_response = requests.patch(current_users_link, auth=(USER, PASSWORD))
                current_user_object = current_user_response.json()
                current_user_results = current_user_object["username"]
                response = current_user_response.status_code
                assert response == 200
                print(f"User with link {current_users_link} has the {current_user_results} username")
            elif key == False:
                print("Empty user list")


def update_users():
    get_user_list(URL[1])
    current_users_list = json.load(open('../response.json', 'r'))

    for i in current_users_list:
        for key, value in i.items():
            if 'url' in key:
                current_users_link = value
                current_user_response = requests.patch(current_users_link, auth=(USER, PASSWORD))
                current_user_object = current_user_response.json()
                current_user_results = current_user_object["username"]
                params = {"username": current_user_results, "email": f"{current_user_results}@email.com"}
                update_current_user_response = requests.put(current_users_link, auth=(USER, PASSWORD), data=params)
                updated_current_user_object = update_current_user_response.json()
                updated_current_user_results = updated_current_user_object["email"]
                response = update_current_user_response.status_code
                assert response == 200
                print(f"User with username {current_user_results} has the {updated_current_user_results} email")
            elif key == False:
                print("Empty user list")

def delete_users():
    get_user_list(URL[1])
    current_users_list = json.load(open('../response.json', 'r'))

    for i in current_users_list:
        for key, value in i.items():
            if 'url' in key:
                current_users_link = value
                current_user_response = requests.patch(current_users_link, auth=(USER, PASSWORD))
                current_user_object = current_user_response.json()
                current_user_results = current_user_object["url"]
                user_id = str(current_user_results).split("/")[-2]
                params = {'username': current_user_object['username']}
                if len(str(current_user_object['username'])) == 15:
                    delete_user_response = requests.delete(current_user_results, auth=(USER, PASSWORD), data=params)

                    response = delete_user_response.status_code
                    assert response == 204
                    print(f"User with username {current_user_object['username']} and the user id {user_id} was deleted")
            elif key == False:
                print("Empty user list")


def test_add_user():
    add_user()


def test_read_user():
    read_users()

def test_update_user():
    update_users()

def test_delete_user():
    delete_users()
