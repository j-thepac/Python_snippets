async function request(){

    d=document.getElementById("1").value
    payload={method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({data: d})};
    resp=await fetch("http://localhost:4321/",payload)
    result=await resp.text()

    console.log(result)
    document.getElementById("2").value=result
}