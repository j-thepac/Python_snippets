async function fn(){
    data=document.getElementById("a").value 
    payload={
        method: "POST"
        ,headers:{"Content-Type":"application/json"}
        ,body:JSON.stringify({"cmd":data})
    }
    resp= await fetch("http://0.0.0.0:5000/", payload)
    res= await resp.text()

    document.getElementById("b").value=res
}