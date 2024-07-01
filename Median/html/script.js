async function fn(){
    data1=document.getElementById("a").value
    data2=document.getElementById("b").value
    payload={
        "method":"POST"
        ,"headers":{
            "Content-Type":"application/json"
        }
        ,"body":JSON.stringify({"data1":data1,"data2":data2})
    
    }
    resp=await fetch("http://0.0.0.0:5000/",payload)
    result= await resp.text()
    document.getElementById("c").value=result
}