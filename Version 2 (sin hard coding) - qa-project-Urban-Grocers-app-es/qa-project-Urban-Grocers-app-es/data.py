## Account Creation Parameters:

headers ={
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

## ============ Kit Creation Parameters: ======================== ##

kit_headers = {
    "Content-Type": "application/json"
    }

params = {"cardId":1} ## No es necesario

kit_body = {
    "name": "Conjunto"
}
## ======================= Success 201 Names ======================= ##

one_letter = {"name": "a"}

max_allowed_chars = {"name":"a" * 511 }

special_chars = {"name":"\\\"№%@\","}

name_with_spaces = {"name": " A Aaa " }

name_with_numbers = {"name":"123"}

## ======================= Success 400 Names ======================= ##

zero_chars = {"name":""}

surpass_max_allowed_chars = {"name":"a" * 512 }

no_name = None

int_numbers = {"name":123}


