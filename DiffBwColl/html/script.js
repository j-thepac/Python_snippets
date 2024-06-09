async function fn(){
    a=document.getElementById("a").value
    b=document.getElementById("b").value

    payload={
        method:"POST"
        ,headers:{"Content-Type":"application/json"}
        ,body:JSON.stringify({"a":a.split(","),"b":b.split(",")})
    }

    resp=await fetch("http://0.0.0.0:5000/",payload)
    result= await resp.json()
    document.getElementById("d").value=result
}