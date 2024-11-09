

async function fn(){
    nums=document.getElementById("nums").value 
    console.log(nums)
    target=document.getElementById("target").value 

    payload={
        "method":"POST"
        ,"headers":{"Content-Type":"application/json"}
        ,"body":JSON.stringify({"nums":nums , "target":target})
    }
    resp=await fetch("http://localhost:5000/",payload)
    res= await resp.text()

    document.getElementById("result").value = res

}