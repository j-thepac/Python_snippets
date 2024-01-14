async function fn(){
    data=document.getElementById("1").value
    payload={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({"data":data})}
    resp=await fetch(url="http://0.0.0.0:5000/",payload)
    result= await resp.text()
    document.getElementById("2").value=result
}