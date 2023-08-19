

async function fn(){
inp=document.getElementById("1").value
payload={method:"POST",headers:{"Content-Type":"application/json"}, body:JSON.stringify({"data":inp})}
req=await fetch(url="http://localhost:5000/",payload)
result= await req.text()
document.getElementById("2").value=result


}


 function anim(ele){
    console.log("anim")
    ele.classList.add('shadow-pop-tr');
}