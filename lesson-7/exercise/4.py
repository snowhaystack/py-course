import sqlalchemy as db
from rich.console import Console

console = Console()

db_connection = "sqlite:///course.db"
engine = db.create_engine(db_connection, echo=True)
conn = engine.connect()

result = list(conn.execute("select * from users"))
console.log(result)
# insert directly into list
result = conn.execute("select * from users ").fetchall()
console.log(result)
result = conn.execute(
    "select * from users where id>:idfilter", idfilter=10).fetchall()
console.log(result)
# mapping metadata
metadata = db.MetaData()
users = db.Table("users", metadata,
                 db.Column("id", db.Integer(), primary_key=True),
                 db.Column('name', db.VARCHAR(255)),
                 db.Column('last_name', db.VARCHAR(255)),
                 db.Column('email', db.VARCHAR(255))
                 )
insert_obj = db.insert(users).values(
    name="test-name",
    last_name="test_last_name",
    email="test_email"
)
with engine.begin() as conn:
    conn.execute(insert_obj)

select_obj = db.select(users)
with engine.begin() as conn:
    result = conn.execute(select_obj).fetchall()
    console.log(result)
# using c collection
select_obj = db.select(users).where(
    db.and_(users.c.name.like("%ar%"), users.c.last_name.like("%chi%")))
with engine.begin() as conn:
    result = conn.execute(select_obj).fetchall()
    console.log(result)
