import configuration
import requests
import data
from data import user_body


##from data import user_body


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body
##user_body = get_user_body("Ana")

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                  		      json=body,
                		      headers=data.headers)
response_post = post_new_user(data.user_body)
print(response_post.status_code)
print(response_post.json())


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response_get = get_users_table()
print(response_get.status_code)

























