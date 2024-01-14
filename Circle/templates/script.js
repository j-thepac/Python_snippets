

async function fn(){

    n=document.getElementById("1").value
    fst=document.getElementById("2").value
    console.log("n")
    console.log("fst")
    payload={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({"n":n,"fst":fst})}
    resp = await fetch(url="http://0.0.0.0:5000/",payload)
    res=await resp.text()
    document.getElementById("3").value=res

}