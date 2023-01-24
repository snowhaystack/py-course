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
console = Console()
endpoint = 'https://randomuser.me/api/?results=22'
table = Table()
table.add_column("gender", style='red')
table.add_column("name", style='blue')
table.add_column("last-name", style='yellow')
result = request.get(url=endpoint).json()['results']
for user in result:
    table.add_row(user['gender'], user['name']['first'], user['name']['last'])
console.print(table)
