let form=document.querySelector("#task_form");
let message=document.querySelector("#message");
let taskList=document.querySelector("#task_list");

form.addEventListener("submit", async function(event){

    event.preventDefault();

    let task=document.querySelector("#task").value;

    try{
        let response=await fetch("/add_task",{
            method:"POST",

            headers:{
                "content-type":"application/json"
            },

            body:JSON.stringify({
                task:task
            })
        });
        let data=await response.json();

        message.innerText= data.message;
        getTasks();
    }
    catch(error){
        console.log(error);
        message.innerText="server problem";
    }

});
async function getTasks(){
    let response=await fetch("/get_tasks");

    let tasks=await response.json();

    taskList.innerHTML="";

    tasks.forEach(function(task){
        taskList.innerHTML +=`
        <p>${task.task_name}
          <button onclick="editTask(${task.id},'${task.task_name}')">Edit</button>
          <button onclick="deleteTask(${task.id})">Delete</button>
        </p>
        `;
    });
}
getTasks();

async function deleteTask(taskId){

    let response=await fetch(`/delete_task/${taskId}`,{
        method:"DELETE"
    });
    let data =await response.json();
    message.textContent=data.message;

    getTasks();
}

async function editTask(taskId,taskName) {
   
    let newTask = prompt("Edit task:",taskName);

    if (!newTask){
        return;
    }
    let response = await fetch(`/update_task/${taskId}`,{
        method:"PUT",

        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            task:newTask
        })
    });

    let data = await response.json();

    message.textContent=data.message;

    getTasks();
}