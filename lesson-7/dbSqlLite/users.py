# https://randomuser.me/api/?results=100

"""
from rich.table import Table
table = Table()
table.add_column("id")
table.add_column("desc")
table.add_row("1","test")
table.add_row("2","test2")
table.add_row("3","test3")
console.print(table)
"""
import requests as request
from rich.console import Console
from rich.table import Table
import sqlite3


class User():
    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

    def __str__(self) -> str:
        return f'{self.name},{self.last_name},{self.email}'

    def __repr__(self) -> str:
        return f'{self.name},{self.last_name},{self.email}'


class ManageUsers():
    endpoint = 'https://randomuser.me/api/?results={}'
    file_db = 'courseMapped.db'
    conn = None

    def __initDB(self):
        self.conn = sqlite3.connect(self.file_db)
        cursor = self.conn.cursor()
        qry_drop_user = """
            DROP TABLE users
        """
        cursor.execute(qry_drop_user)

        qry_create_user = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            );
            """
        cursor.execute(qry_create_user)

    def __clodeDB(self):
        self.conn.commit()
        self.conn.close()

    def __getUserFromApi(self, num):
        users_retrieved = []
        users_from_api = request.get(
            self.endpoint.format(num)).json()["results"]
        for user_from_api in users_from_api:
            user_from_api_converted = User(
                user_from_api["name"]["first"], user_from_api["name"]["last"], user_from_api["email"])
            users_retrieved.append(user_from_api_converted)
        return users_retrieved

    def __init__(self, num=10) -> None:
        self.__initDB()
        self.users = self.__getUserFromApi(num)

    def save(self):
        cursor = self.conn.cursor()
        for user in self.users:
            qry_insert_user = "INSERT INTO users (name, last_name, email) VALUES (?, ?, ?)"
            cursor.execute(qry_insert_user,
                           (user.name, user.last_name, user.email))

    def __del__(self):
        self.__clodeDB()

    def table(self):
        table = Table()
        table.add_column("gender", style='red')
        table.add_column("name", style='blue')
        table.add_column("last-name", style='yellow')
        for user in self.users:
            table.add_row(user.name, user.last_name, user.email)
        return table


if __name__ == "__main__":
    console = Console()
    manageUsers = ManageUsers(100)
    manageUsers.save()
    console.log(manageUsers.users)
    console.log(*manageUsers.users)
    console.print(manageUsers.table())
    del manageUsers
