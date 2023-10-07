
async function fn(){
    a=  JSON.parse(document.getElementById("1").value)
    b= document.getElementById("2").value

    console.log(a)
    payload={
        method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({"data":(a),"name":b})
        }
    resp= await fetch(url="http://0.0.0.0:5000/",payload)
    res= await resp.text()
     document.getElementById("3").value = res
}

