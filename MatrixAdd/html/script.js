async function fn(){
    a=document.getElementById("1").value
    b=document.getElementById("2").value
    payload={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify([{"a":a,"b":b}])}
    resp=await fetch(url="http://localhost:5000/",payload)
    res= await resp.text()
    document.getElementById("3").value=res


}