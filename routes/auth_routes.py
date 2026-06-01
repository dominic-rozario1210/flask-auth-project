from flask import Blueprint,render_template,session,redirect,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from database import conn,cursor


auth_bp=Blueprint("auth",__name__)
@auth_bp.route("/login")
def login_page():
    return render_template("login.html")

@auth_bp.route("/register")
def register_page():
    return render_template("register.html")

@auth_bp.route("/register",methods=["POST"])
def register():
    data=request.get_json()

    username=data.get("username")
    password=data.get("password")

    if username == "" or password == "":
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

    query="INSERT INTO users (username,password) VAlUES(%s,%s)"
    cursor.execute(query,(username,hashed_password))
    conn.commit()

    return jsonify({
        "message":"registration successful"
    }),201

@auth_bp.route("/login",methods=["POST"])
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

@auth_bp.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")
