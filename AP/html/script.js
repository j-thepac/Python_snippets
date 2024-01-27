async function fn(){

data=document.getElementById("a").value
payload={
    method:"POST"
    ,headers:{"Content-Type":"application/json"}
    ,body:JSON.stringify({"seq":data})
}
 resp = await fetch("http://0.0.0.0:5000/",payload)
result = await resp.text()
console.log(result)
document.getElementById("b").value= result



}