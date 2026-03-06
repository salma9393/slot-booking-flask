from flask import Flask, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Database Connection Function
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Salma786ms@",
        database="slot_booking"
    )
    return conn


# Home Page - Show All Slots
@app.route('/')
def index():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM slots")
    slots = cursor.fetchall()

    conn.close()

    return render_template("index.html", slots=slots)


# Book Slot
@app.route('/book/<int:id>')
def book(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE slots SET status='booked' WHERE id=%s",(id,))
    conn.commit()

    conn.close()

    return redirect('/')


# View Booked Slots
@app.route('/booked')
def booked():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM slots WHERE status='booked'")
    slots = cursor.fetchall()

    conn.close()

    return render_template("booked.html", slots=slots)


# Reschedule Slot
@app.route('/reschedule/<int:id>')
def reschedule(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    # Change booked slot back to available
    cursor.execute("UPDATE slots SET status='available' WHERE id=%s",(id,))
    conn.commit()

    conn.close()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)