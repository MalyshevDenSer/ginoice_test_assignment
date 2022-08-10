import json
from sql_service import sign_up_sql_service, auth_up_sql_service
from eth_and_validator import get_eth_hash, validate, authentication

from flask import Flask, request

app = Flask(__name__)


@app.route("/sign_up", methods=['POST'])
def sign_up() -> str:
    """
    Получение POST-запроса на регистрацию и его обработка
    """
    json_in = request.get_json()
    val = validate(json_in['email'], json_in['password'])
    if val is True:
        user_id = sign_up_sql_service(json_in)
        eth_hash = get_eth_hash(user_id)
        return json.dumps({'user_id': user_id, 'eth_hash': eth_hash}, indent=4)
    else:
        return 'Error. Something went wrong'


@app.route("/sign_in", methods=['POST'])
def sign_in() -> str:
    """
    Получение POST-запроса для входа и его обработка
    """
    json_in = request.get_json()
    auth = authentication(json_in['email'], json_in['password'])
    if isinstance(auth, str):
        return json.dumps({'eth_address': auth}, indent=4)
    else:
        return 'Error. Wrong password'
