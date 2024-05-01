from config.db import db


def find():
    mycursor = db.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM users")

    return mycursor.fetchall()


def first(user_id):
    mycursor = db.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM users WHERE Personid=%s", (user_id,))

    return mycursor.fetchone()


def to_json(row):
    return {
        "id": row["Personid"],
        "first_name": row["FirstName"],
        "last_name": row["LastName"],
        "address": row["Address"],
        "city": row["City"]
    }
