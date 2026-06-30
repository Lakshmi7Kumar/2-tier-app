from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():

    db = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    cursor = db.cursor()
    cursor.execute("SELECT 'Database Connected Successfully!'")

    result = cursor.fetchone()

    return result[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0")
