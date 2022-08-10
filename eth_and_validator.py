from web3 import Web3
import re
from email_validator import validate_email, EmailNotValidError
from sql_service import auth_up_sql_service
from typing import Union


def get_eth_hash(user_id: int) -> str:
    """
    Получение Ethereum Signed Message(ethHash). В одну строчку получается
    хешированый в keccak256 id и сразу же хеширование в Ethereum Signed Message(ethHash)
    """
    eth_hash = Web3.solidityKeccak(["string", "bytes"],
                                   ["\x19Ethereum Signed Message:\n32", Web3.solidityKeccak
                                   (["uint256"], [user_id])]).hex()
    return eth_hash


def validate(email: str, password: str) -> bool:
    """
    Проверка эмейла и пароля на валидность
    """
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Make sure your email is correct")
    if len(password) < 8:
        raise ValueError("Make sure your password has at least 8 letters")
    if re.search("[0-9]", password) is None:
        raise ValueError("Make sure your password has a number in it")
    if re.search("[A-Z]", password) is None:
        raise ValueError("Make sure your password has a capital letter in it")
    return True


def authentication(email: str, password: str) -> Union[str, bool]:
    user_data = auth_up_sql_service(email)
    print(user_data)
    if user_data[2] == password:
        return user_data[0]
    else:
        return False
