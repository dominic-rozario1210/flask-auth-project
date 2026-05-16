from flask import Flask,render_template,request,session,jsonify,redirect
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)

app.secret_key=os.getenv("SECRET_KEY")


conn=mysql.connector.connect(
    host=os.getenv("BD_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=3306
)
cursor=conn.cursor(dictionary=True)

@app.route("/")
def home():
    return redirect("/register")

@app.route("/register")
def register_page():
    return render_template("register.html")
@app.route("/register",methods=["POST"])
def register():
    data=request.get_json()

    username=data.get("username")
    password=data.get("password")

    if username=="" or password=="":
        return jsonify({
            "message":"all fields required"
        }),400

    query="SELECT * FROM users WHERE username=%s"
    cursor.execute(query,(username,))

    existing_user=cursor.fetchone()

    if existing_user:
        return jsonify({
            "message":"user already exist"
        }),409
    hashed_password=generate_password_hash(password)

    query="INSERT INTO users (username,password) VALUES(%s,%s)"
    cursor.execute(query,(username,hashed_password))
    conn.commit()

    return jsonify({
        "message":"registration successfful"
    }),201
@app.route("/login")
def login_page():
    return render_template("login.html")
@app.route("/login",methods=["POST"])
def  login():
    data=request.get_json()

    username=data.get("username")
    password=data.get("password")

    query="SELECT * FROM users WHERE username=%s"
    cursor.execute(query,(username,))

    user=cursor.fetchone()

    if not user:
        return jsonify({
            "message":"user not found"
        }),404
    if not check_password_hash(user["password"],password):
        return jsonify({
            "message":"wrong password"
        }),401
    session["user"]=user["username"]
    return jsonify({
        "message":"login successful"
    }),200
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template(
        "dashboard.html",username=session["user"]
    )
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")

if __name__=="__main__":
    app.run(debug=True)
