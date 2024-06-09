async function fn(){
    l1=document.getElementById("1").value
    l2=document.getElementById("2").value
    console.log(l1)
    payload={
        "method":"POST"
        ,"headers":{
            "Content-Type":"application/json"
        }
        ,"body":JSON.stringify({"l1":l1,"l2":l2})
    }
    resp= await fetch("http://0.0.0.0:5000/",payload)
    res= await resp.text()
    document.getElementById("3").value=res
}