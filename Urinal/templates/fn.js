async function fn(){
    data=document.getElementById("myInput").value;
    console.log(data)
    payload={method:"POST" , headers:{"Content-Type":"text/plain"}, body:data};
    resp = await fetch("http://localhost:4321/",payload);
    result= await resp.text()
    document.getElementById("Result").innerText=result;
    // document.getElementById("Result").classList.add("slide-fwd-center");
}

function anime(ele){
    ele.classList.add("rotate-in-center");
    // ele.classList.remove("flip-scale-2-hor-top");
}