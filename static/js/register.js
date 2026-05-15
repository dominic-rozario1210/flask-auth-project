let form=document.querySelector("#form");
let btn=document.querySelector("#btn");
let message=document.querySelector("#message");

form.addEventListener("submit", async function(){
    event.preventDefault()
    let username=document.querySelector("#username").value;
    let password=document.querySelector("#password").value;

    btn.disabled= true;
    btn.innerText="loading";
    try{
        let response=await fetch("/register",{
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                username:username,
                password:password
            })
        });
        let data=await response.json();
        message.innerText=data.message;

    }
    catch(error){
        console.log(error);
        message.innerText="server error";
    }
    finally{
        btn.disabled=false;
        btn.innerText="register";
    }
});