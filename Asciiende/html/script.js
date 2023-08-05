

async function fn(){
    // console.log("hi")
    v=document.getElementById("1").value
    const headers = {'Content-Type':'application/json'}
    payload={ method:"POST",headers,body:JSON.stringify({data:v}) }

    resp=await fetch("http://0.0.0.0:4321/",payload)
    result= await resp.text()
    document.getElementById("2").value=result

}