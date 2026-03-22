var drumElementLength=document.querySelectorAll(".drum").length;

for(var i=0;i<drumElementLength;i++){

    document.querySelectorAll(".drum")[i].addEventListener("click",function(){
        //  this.style.backgroundColor="blue";
          
        // var audio=new Audio("./sounds/snare.mp3");
        // audio.play();
        // this.style.color="blue";
        var content=this.innerHTML;
        switch(content){
            case 'w':
            this.style.backgroundColor="green";
            var audio=new Audio("./sounds/kick-bass.mp3");
            audio.play();
            this.style.color="red";
            break;         
            case 'a':
            this.style.backgroundColor="pink";
            var audio=new Audio("./sounds/tom-1.mp3");
            audio.play();
            this.style.color="black";
            break;
            case 's':
            this.style.backgroundColor="orange";
            var audio=new Audio("./sounds/tom-2.mp3");
            audio.play();
            this.style.color="yellow";
            break;
            case 'd':
            this.style.backgroundColor="indigo";
            var audio=new Audio("./sounds/tom-3.mp3");
            audio.play();
            this.style.color="white";
            break;
            case 'j':
            this.style.backgroundColor="blue";
            var audio=new Audio("./sounds/snare.mp3");
            audio.play();
            this.style.color="blue";
            break;
            case 'k':
            this.style.backgroundColor="blue";
            var audio=new Audio("./sounds/tom-4.mp3");
            audio.play();
            this.style.color="violet";
            break;
            case 'l':
            this.style.backgroundColor="red";
            var audio=new Audio("./sounds/crash.mp3");
            audio.play();
            this.style.color="green";
            break;
            default:
            this.style.backgroundColor="red";
            var audio=new Audio("./sounds/crash.mp3");
            audio.play();
            this.style.color="green";

        }
       keyPress(content)
       buttonAnimation(content)

    })
}
function keyPress(key){
    
switch(key){
            case 'w':
            // this.style.backgroundColor="green";
            var audio=new Audio("./sounds/kick-bass.mp3");
            audio.play();
            // this.style.color="red";
            break;         
            case 'a':
            // this.style.backgroundColor="pink";
            var audio=new Audio("./sounds/tom-1.mp3");
            audio.play();
            // this.style.color="black";
            break;
            case 's':
            // this.style.backgroundColor="orange";
            var audio=new Audio("./sounds/tom-2.mp3");
            audio.play();
            // this.style.color="yellow";
            break;
            case 'd':
            // this.style.backgroundColor="indigo";
            var audio=new Audio("./sounds/tom-3.mp3");
            audio.play();
            // this.style.color="white";
            break;
            case 'j':
            // this.style.backgroundColor="blue";
            var audio=new Audio("./sounds/snare.mp3");
            audio.play();
            // this.style.color="blue";
            break;
            case 'k':
            // this.style.backgroundColor="blue";
            var audio=new Audio("./sounds/tom-4.mp3");
            audio.play();
            // this.style.color="violet";
            break;
            case 'l':
            // this.style.backgroundColor="red";
            var audio=new Audio("./sounds/crash.mp3");
            audio.play();
            // this.style.color="green";
            break;
            default:
            // this.style.backgroundColor="red";
            var audio=new Audio("./sounds/crash.mp3");
            audio.play();
            // this.style.color="green";

        }
}
document.addEventListener("keydown",function(event){
     keyPress(event.key);
     buttonAnimation(event.key)
})
function buttonAnimation(key){
    var currentKey=document.querySelector("."+key);
    currentKey.classList.add("pressed");
    setTimeout(function(){
        currentKey.classList.remove("pressed")
    },105)
}