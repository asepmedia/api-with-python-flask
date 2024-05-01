from config.db import db


def find():
    mycursor = db.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM portfolio")

    return mycursor.fetchall()

def first(portfolio_id):
    mycursor = db.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM portfolio WHERE id=%s", (portfolio_id,))

    return mycursor.fetchone()

def to_json(row):
    return {
        "id": row["id"],
        "title": row["Title"],
        "description": row["Description"],
    }
