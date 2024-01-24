async function fn(){

    invested=document.getElementById("a").value

     changes=document.getElementById("b").value
     payload={
        method:"POST"
        ,headers:{"Content-Type":"application/json"}
        ,body:JSON.stringify({
            "invested":invested,
            "changes":changes })
     }

     resp=await fetch("http://0.0.0.0:5000/",payload=payload)
     res=await resp.text()
     document.getElementById("c").value=res
     console.log("done")

}