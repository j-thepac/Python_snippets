async function fn(){
    strng= document.getElementById("a").value
    array= document.getElementById("b").value

    payload={
        "method":"POST"
        ,"headers":{"Content-Type":"application/json"}    
        ,"body":JSON.stringify({"strng":strng,"array":array.split(",")})
    }
    resp= await fetch("http://0.0.0.0:5000",payload)
    result= await resp.text()
    document.getElementById("d").value=result
}