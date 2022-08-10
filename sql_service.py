import sqlite3


def sign_up_sql_service(json: dict) -> int:
    """
    Функция которая обслуживает эндпоинт регистрации при работе с SQLite
    """
    c = sqlite3.connect('db')
    c.execute('''CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY autoincrement,
        name VARCHAR(30),
        surname VARCHAR(50),
        email VARCHAR(30),
        eth_address VARCHAR (42),
        password VARCHAR(30)
    )''')
    n, s, m, e, p = [x for x in list(json.values())]
    c.execute("INSERT INTO users (name, surname, email, eth_address, password) VALUES (?, ?, ?, ?, ?)", (n, s, m, e, p))
    cur = c.cursor()
    cur.execute('SELECT id from users WHERE eth_address=?', (e,))
    c.commit()
    return cur.fetchone()[0]


def auth_up_sql_service(email: str) -> str:
    c = sqlite3.connect('db')
    c.execute('''CREATE TABLE IF NOT EXISTS users
        (
            id INTEGER PRIMARY KEY autoincrement,
            name VARCHAR(30),
            surname VARCHAR(50),
            email VARCHAR(30),
            eth_address VARCHAR (42),
            password VARCHAR(30)
        )''')
    cur = c.cursor()
    cur.execute('''SELECT eth_address, email, password
    FROM users
    WHERE email = (?)
    ''', (email,))
    user_data = cur.fetchall()[0]
    return user_data
