import base64
import hmac
from datetime import datetime


def parse_params_to_str(params: dict):
    url = "?"
    for key, value in params.items():
        url = url + str(key) + "=" + str(value) + "&"
    return url[1:-1]


def hash_string(params: dict, secret_key: str):
    mac = hmac.new(
        bytes(secret_key, encoding="utf8"), bytes(parse_params_to_str(params), encoding="utf-8"), digestmod="sha256"
    )
    digest = mac.digest()
    validating_secret = str(base64.b64encode(digest).decode("utf-8"))
    return validating_secret


p = {"ts": int(datetime.utcnow().timestamp()), "access_key": "9AdwckcOrBVBwrqZwL0cxItJ"}
print(p)
print(hash_string(p, "JyH2woaiwGXaOc8JyK4Fzs58ZWTQAsGD"))
