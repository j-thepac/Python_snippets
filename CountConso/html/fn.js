async function api(){
    data=document.getElementById("ip").value;
    console.log(data)
    payload={method:"POST",headers:{"Content-Type": "text/plain"},"body":data};
    resp=await fetch("http://localhost:4321", payload)
    result= await resp.text();
    console.log(result);
    document.getElementById("op").value=result;
}