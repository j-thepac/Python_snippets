async function fn(){
    l=document.getElementById("a").value
    payload={
        "method":"POST"
        ,"headers":{ "Content-Type":"application/json"}
        ,"body":JSON.stringify({"data":l})
    
    }
    resp=await fetch("http://0.0.0.0:5000/",payload)
    result= await resp.text()
    document.getElementById("b").value=result
}