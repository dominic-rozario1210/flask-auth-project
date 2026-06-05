from flask import Flask,render_template,session,redirect
from decorators import login_required
import os
from dotenv import load_dotenv
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

load_dotenv()


app=Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.secret_key=os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return redirect("/register")


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",username=session["user"]
    )

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
