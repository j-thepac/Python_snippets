

async function fn(){

     width= document.getElementById("1").value
     ratio=document.getElementById("2").value
     console.log(width)
     console.log(ratio)
     payload={method:"POST" , headers:{"Content-Type":"application/json"},body:JSON.stringify({"width":width,"ratio":ratio})}
     resp= await fetch(url="http://0.0.0.0:5000/",payload)
     result= await resp.text()

     document.getElementById("3").value=result
}
