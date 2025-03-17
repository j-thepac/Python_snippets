async function fn(){
    l=document.getElementById("a").value 
    k=document.getElementById("b").value 

    payload={
        method:"POST"
        ,headers:{"Content-Type":"application/json"}
        ,body:JSON.stringify({"root":l,"k":k})
    }
    result=await fetch("http://0.0.0.0:5000/",payload)
    resp= await result.text()
    document.getElementById("c").value=resp
}