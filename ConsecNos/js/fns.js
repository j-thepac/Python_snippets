async function postApi(){
    data=document.getElementById("ip").value;
    console.log("input = "+ data);
    payload={method:"POST",body:data};
    resp= await fetch("http://localhost:4321",payload);
    result = await resp.text();     
    console.log(result);
}