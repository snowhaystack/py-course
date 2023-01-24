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


class User():
    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

    def __str__(self) -> str:
        return f'{self.name},{self.last_name},{self.email}'


class ManageUsers():
    endpoint = 'https://randomuser.me/api/?results={}'

    def __init__(self, num=10) -> None:
        self.users = []
        users_from_api = request.get(
            self.endpoint.format(num)).json()["results"]
        for user_from_api in users_from_api:
            user_from_api_converted = User(
                user_from_api["name"]["first"], user_from_api["name"]["last"], user_from_api["email"])
            self.users.append(user_from_api_converted)

    def table(self):
        table = Table()
        table.add_column("gender", style='red')
        table.add_column("name", style='blue')
        table.add_column("last-name", style='yellow')
        for user in self.users:
            table.add_row(user.name, user.last_name, user.email)
        return table


console = Console()
manageUsers = ManageUsers(25)
console.log(manageUsers.users)
console.log(*manageUsers.users)
console.print(manageUsers.table())
