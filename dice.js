'./images/dice1.png'
'./images/dice2.png'
'./images/dice4.png'
'./images/dice5.png'
'./images/dice6.png'
'./images/dice3.png'



// alert("working")
var i,j;
function randomnumber(){
    var t=Math.ceil(Math.random()*6);
    return t;
}

function diceimg(){
    var player1=randomnumber();
    var player2=randomnumber();
    var img="images/dice"+player1+".png";
    var img1="images/dice"+player2+".png";
    
    console.log(img);
    document.querySelectorAll("p")[2].innerText=img;
    document.querySelectorAll("img")[0].setAttribute("src",img);
    document.querySelectorAll("img")[1].setAttribute("src",img1);
    document.querySelectorAll("p")[2].innerText=img;
    if(player1>player2){
         document.querySelectorAll("h1")[0].innerText="Player 1 wins. ";
         document.createElement("p").appendChild(document.createTextNode("Player1"));
        
          document.getElementById("h1").appendChild("p");



    }
    else if(player1<player2){
                 document.querySelectorAll("h1")[0].innerText="Player 2 wins. ";
                 
    }
   else{
    document.querySelectorAll("h1")[0].innerText=" Draw. "
   }
    return img;
}
diceimg();