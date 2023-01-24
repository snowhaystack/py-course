import sqlalchemy as db
from rich.console import Console
import users as us
import random
import datetime

console = Console()

db_connection = "sqlite:///courseMapped.db"
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
                   db.Column("customer_id", db.Integer(), db.ForeignKey(
                       "customer.id"), nullable=False),
                   db.Column("amount", db.Integer()),
                   db.Column("date", db.Date)
                   )
user = db.Table("user", metadata,
                db.Column("id", db.Integer(), primary_key=True,
                          autoincrement=True),
                db.Column("name", db.VARCHAR(255)),
                db.Column("last_name", db.VARCHAR(255)),
                db.Column("email", db.VARCHAR(255))
                )
metadata.create_all(engine)

manage_user = us.ManageUsers(100)
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
    receipt_ins = db.insert(receipt).values(
        customer_id=random.randint(1, 8),
        amount=random.randint(10, 1000),
        date=datetime.datetime(2022, random.randint(
            1, 12), random.randint(1, 28))
    )
conn.execute(receipt_ins)

receipt_sel = db.select(receipt)
console.log(conn.execute(receipt_sel).fetchall())

customer_receipt = receipt.join(customer)
sel_join = db.select(receipt, customer).where(
    receipt.c.amount > 400).select_from(customer_receipt)
result = conn.execute(sel_join).fetchall()

console.log(result)
