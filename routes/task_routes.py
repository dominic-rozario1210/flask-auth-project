from flask import Blueprint,request,jsonify,session
from database import conn,cursor

task_bp=Blueprint("task",__name__)
@task_bp.route("/add_task",methods=["POST"])
def add_task():
    if "user_id" not in session:
        return jsonify({"message":"please login first"})
    data=request.get_json()

    task_name=data.get("task")

    cursor.execute(
        "INSERT INTO tasks (task_name,user_id) VALUES(%s,%s)",
        (task_name,session["user_id"])
    )
    conn.commit()

    return jsonify({"message":"task added successfully"})

@task_bp.route("/get_tasks")
def get_tasks():
    if "user_id" not in session:
        return jsonify([])

    cursor.execute(
        "SELECT * FROM tasks where user_id=%s",
        (session["user_id"],)
    )
    tasks=cursor.fetchall()
    return jsonify(tasks)

@task_bp.route("/delete_task/<int:task_id>",methods=["DELETE"])
def delete_task(task_id):
    if "user_id" not in session:
        return jsonify({"message":"please login first"})

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (task_id,)
    )
    conn.commit()
    return jsonify({
        "message":"Task deleted successfully"
    })

@task_bp.route("/update_task/<int:task_id>",methods=["PUT"])
def update_task(task_id):

    if "user_id" not in session:
        return jsonify({"message":"please login first"})

    data=request.get_json();

    task_name=data.get("task")

    cursor.execute(
        "UPDATE tasks SET task_name=%s WHERE id=%s",
        (task_name,task_id)
    )
    conn.commit()

    return jsonify({
        "message":"task updated successfully"
    })


