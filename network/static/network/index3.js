
document.addEventListener('DOMContentLoaded',function(){

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  var no = document.getElementById("paged").textContent;
  var usern  = document.getElementById("usern").textContent;
  //fetches the post of the function with this page number
  fetch(`new3?page=${no}`)
    .then (response =>response.json())
    .then(poss=>{
      console.log(poss);

      poss.forEach((post)=>{

        var element =document.createElement('div');
        element.setAttribute("id", `post${post.id}`);
        var element2 =document.createElement('div');
        element2.setAttribute("id", `edit${post.id}`);
        element2.innerHTML=` <form id="compose-form${post.id}">
        <textarea class="form-control" id="compose-body${post.id}" placeholder="Edit">${post.body}</textarea>
        <input type="submit" class="btn btn-primary"/>
    </form>`;
    element2.style.display = 'none';
        if(usern== post.sender){
          element.innerHTML=`${post.sender} at ${post.timestamp}<br>     <span id="body${post.id}" >${post.body}</span><br><span id="a${post.id}"><i class="material-icons like" class="like">favorite</i> </span><span id="${post.id}">${post.like}</span><br>
          <span><button type="button" class="btn btn-outline-primary" id="button${post.id}">Edit</button></span>`;
          }
          else{
           element.innerHTML=`${post.sender} at ${post.timestamp}<br>     <span id="body${post.id}" >${post.body}</span><br><span id="a${post.id}"><i class="material-icons like" class="like">favorite</i> </span> <span id="${post.id}">${post.like}</span><br>`;
          }

        element.style.backgroundColor = "#FFFFFF";
        element.style.padding="25px";
        element.style.border="thick solid #000000";
        var x = document.getElementById("poss");
        x.appendChild(element);
        x.appendChild(element2);
      });
    });

    fetch(`new3?page=${no}`)
    .then (response =>response.json())
    .then(poss=>{
      console.log(poss);
      poss.forEach((post)=>{
        element=document.getElementById(`a${post.id}`)
        element.addEventListener('click', function() {
          console.log("This element has been clicked")
            var l=vview(post,element);

      });
      });
    });

    fetch(`new3?page=${no}`)
    .then (response =>response.json())
    .then(poss=>{
      console.log(poss);
      poss.forEach((post)=>{
        if(document.getElementById(`button${post.id}`)!=null){
        element=document.getElementById(`button${post.id}`)
        element.addEventListener('click', function() {
          console.log("This element has been clicked")
            var l=bview(post,element);
      });
    }
      });
    });


  function vview(post,element){ 
    const b=post.id;
      fetch(`/like/${b}`, {
  method: 'POST',
  body: JSON.stringify({
  })
})
.then(response => response.json())
.then(result => {
    // Print result
    document.getElementById(`${post.id}`).textContent=result.likes;
    console.log(result);

});
 
}

function bview(post,element){ 
  const b=post.id;
  document.querySelector(`#edit${post.id}`).style.display = 'block';
  document.querySelector(`#post${post.id}`).style.display = 'none';
}

fetch(`new3?page=${no}`)
.then (response =>response.json())
.then(poss=>{
  console.log(poss);
  poss.forEach((post)=>{
    
    
    document.querySelector(`#compose-form${post.id}`).onsubmit = ()=>{
      console.log("Submit button has been clicked")
      const body= document.querySelector(`#compose-body${post.id}`).value;
      console.log(body);
      const b=post.id;
      fetch(`/edit/${b}`, {
        method: 'POST',
        body: JSON.stringify({
            body: body
        })
      })
      .then(response => response.json())
      .then(result => {
        console.log(result);
        document.getElementById(`body${post.id}`).textContent=result.body;
        document.querySelector(`#edit${post.id}`).style.display = 'block';
        document.querySelector(`#post${post.id}`).style.display = 'none';


});
      
     
    }
      

  });
});

});
