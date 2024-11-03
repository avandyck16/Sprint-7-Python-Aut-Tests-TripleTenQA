import data
import configuration
import requests
import sender_stand_request
from data import kit_body


def get_kit_body(name):
    current_kit = data.kit_body.copy()
    current_kit["name"] = name
    return current_kit

## ======================= Positive Asserts ====================##

def positive_assert(name):
    kit_name = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(kit_name)

    assert user_response.status_code == 201
    response_body = user_response.json()
    assert response_body.get("name") == kit_name["name"]

## ===================== Positive Tests ====================== ##

def test_create_kit_allowed_chars_1_success():
    positive_assert("a")

def test_create_kit_max_allowed_chars_511_success():
    user_response = sender_stand_request.post_new_client_kit(data.max_kit_body)
    assert user_response.status_code == 201
    response_body = user_response.json()
    assert response_body.get("name") == data.max_kit_body["name"]

def test_create_kit_with_special_chars_success():
    positive_assert("\\\"№%@\",")

def test_create_kit_with_spaces_success():
    positive_assert(" A Aaa " )

def test_create_kit_with_numbers_success():
    positive_assert("123" )

## ======================= Negative Asserts ====================##

def negative_assert(name):
    kit_name = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(kit_name)

    assert user_response.status_code == 400


## ===================== Negative Tests ====================== ##

def test_create_kit_zero_chars_code_400():
    negative_assert("")

def test_create_kit_512_chars_code_400():
    user_response = sender_stand_request.post_new_client_kit(data.surpass_max_kit_body)
    assert user_response.status_code == 400
    response_body = user_response.json()

def test_create_kit_empty_params_code_400():
    negative_assert({})

def test_create_kit_integer_code_400():
    negative_assert(123)






