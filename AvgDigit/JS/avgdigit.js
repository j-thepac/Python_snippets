function fx(y){
    let z=y.toString().split('').map( i=> parseInt(i))
    p1=0,p2=1
    let a =[]
    while (p1<p2 && p2<=z.length-1){
     a.push(Math.ceil((z[p1]+z[p2])/2) )
     p2=p2+1
     p1=p1+1
    }
    return a.join('')
   }
   
   
   function fn(x){
   let y=x.toString()
   if (y.length===1) {return y}
    while (y.length!=1){
     y=fx(y)
    }
    return y
   }
   
   console.log(fn(246))
   
   
   
       
   