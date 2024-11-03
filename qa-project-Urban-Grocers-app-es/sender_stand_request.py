import configuration
import data
import requests

from data import user_body

# ======= Solicitud para crear un nuevo usuario ======= ##

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response_post = post_new_user(get_user_body("Axel"))
print(response_post.status_code)
print(response_post.json())

# ======= Solicitud para crear Nuevo Kit ======= ##

def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=data.kit_headers,
                         json=body)
response_kit = post_new_client_kit(data.kit_body)
print(response_kit.status_code)
print(response_kit.json())

