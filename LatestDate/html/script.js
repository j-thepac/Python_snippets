async function fn(){
    a=document.getElementById("a").value
    b=document.getElementById("b").value
    c=document.getElementById("c").value
    d=document.getElementById("d").value

    payload={
        method:"POST"
        ,headers:{
            "Content-Type":"application/json"
        }
        ,body:JSON.stringify({
            "a":a,
            "b":b,
            "c":c,
            "d":d
          
          })   
    }

    resp= await fetch("http://0.0.0.0:5000/",payload)
    result= await resp.text()
    document.getElementById("e").value=result
}