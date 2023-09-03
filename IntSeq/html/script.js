async function fs(){


    myData=document.getElementById("1").value 
    console.log("input="+myData)
    payload={method: "POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({"data":myData})}
    raw=await fetch(url="http://0.0.0.0:5000/",payload)
    res= await raw.text()
    document.getElementById("2").value =res

}
    