async function fn(){
    game=document.getElementById("g").value;
    text=document.getElementById("t").value;
    console.log(game);
    console.log(text);
    payload={method:"POST",body:JSON.stringify({"game":game,"text":text}),headers: {"Content-Type": "application/json"}};
     res=await fetch("http://localhost:4321/",payload);
     data = await res.json();
    console.log(data);
}
