async function fn(){
    s=document.getElementById("s").value
    numRows=document.getElementById("numRows").value

    payload={
        method:"POST"
        ,headers:{
            "Content-Type":"application/json"
        }
        ,body:JSON.stringify({"s":s,"numRows":numRows})
    }
    resp= await fetch("http://0.0.0.0:5000/",payload)
    result= await resp.text()
    document.getElementById("result").value=result
}