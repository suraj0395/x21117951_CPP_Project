from ast import Global
from crypt import methods
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras
import db
from send_email import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@postgres123.cv1zqrmigcro.eu-west-1.rds.amazonaws.com/postgres'
db=SQLAlchemy(app)

DB_HOST = "postgres123.cv1zqrmigcro.eu-west-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"

conn=psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

class postgres(db.Model):
    __tablename__="data_collector"
    email_=db.Column(db.String(200), primary_key=True)
    food_=db.Column(db.String(200))
    address_=db.Column(db.String(400))

    def __init__(self, email_, food_, address_):
        self.email_=email_
        self.food_=food_
        self.address_=address_ 


@app.route("/")
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "select * from data_collector"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template("index.html", list_users = list_users)

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        food=request.form["food_name"]
        address=request.form["addr_name"]
        send_email(email) 
        data=postgres(email,food,address)
        db.session.add(data)
        db.session.commit()
    return render_template("success.html")

if __name__ == '__main__': 
    app.debug=True
    app.run()
