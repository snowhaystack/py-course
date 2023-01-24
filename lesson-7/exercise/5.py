import sqlalchemy as db
from rich.console import Console
import manage_users as mu
import random
import datetime

console = Console()

db_connection = "sqlite:///course.db"
engine = db.create_engine(db_connection, echo=True)
conn = engine.connect()
metadata = db.MetaData()
customer = db.Table("customer", metadata,
                    db.Column("id", db.Integer(), primary_key=True,
                              autoincrement=True),
                    db.Column("name", db.VARCHAR(255)),
                    db.Column("last_name", db.VARCHAR(255)),
                    db.Column("email", db.VARCHAR(255))
                    )
receipt = db.Table("receipt", metadata,
                   db.Column("id", db.Integer(), primary_key=True,
                             autoincrement=True),
                   db.Column("idcustomer", db.Integer(), db.ForeignKey(
                       "customer.id"), nullable=False),
                   db.Column("amount", db.Integer()),
                   db.Column("date", db.Date)
                   )
metadata.create_all(engine)

manage_user = mu.ManageUsers(3)
for user in manage_user.users:
    cust_insert = db.insert(customer).values(
        name=user.name,
        last_name=user.last_name,
        email=user.email
    )
    conn.execute(cust_insert)
cust_select = db.select(customer)
console.log(conn.execute(cust_select).fetchall())

for i in range(0, 10):
    receipt_insert = db.insert(receipt).values(
        idcustomer=random.randint(1, 8),
        amount=random.randint(10, 1000),
        date=datetime.datetime(2022, random.randint(
            1, 12), random.randint(1, 28))
    )
    conn.execute(receipt_insert)

receiptt_select = db.select(receipt)
console.log(conn.execute(receiptt_select).fetchall())

customer_receipt = receipt.join(customer)
select_join = db.select(receipt, customer).select_from(customer_receipt)
result = conn.execute(select_join).fetchall()
console.log(result)
