
async function fn(){

    d1=document.getElementById("1").value
    d2=document.getElementById("2").value

    payload={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({"data1":d1,"data2":d2})}
    resp=await fetch(url="http://0.0.0.0:5000/",payload)
    result = await resp.text()
    console.log(result)

    document.getElementById("3").value=result

}