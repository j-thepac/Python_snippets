async function fn(){
d=document.getElementById("a").value 
data = d.split(",").map(i=> parseInt(i))
console.log(data)
// data=
payload={
    method:"POST"
    ,headers:{"Content-Type":"application/json"}
    ,body:JSON.stringify({"data":d})

    }
    resp=await fetch("http://0.0.0.0:5000/",payload)
    res= await resp.text()
    document.getElementById("b").value=res
}

