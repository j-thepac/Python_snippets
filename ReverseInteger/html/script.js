async function fn(){
    x=document.getElementById("a").value
    payload={
        "method":"POST"
        ,"headers":{
            "Content-Type":"application/json"
        }
        ,"body":JSON.stringify({"x":x})
    }
    resp= await fetch("http://0.0.0.0:5000/",payload)
    result=await resp.text()
    document.getElementById("b").value=result
}