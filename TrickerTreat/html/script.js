async function fn(){
    data=document.getElementById("a").value 
    payload={
        method:"POST"
        ,headers:{"Content-Type":"application/json"}
        ,body:JSON.stringify({"data":data})
    }
    resp=await fetch("http://localhost:5000/",payload)
    res= await resp.text()
    document.getElementById("b").value = res
}