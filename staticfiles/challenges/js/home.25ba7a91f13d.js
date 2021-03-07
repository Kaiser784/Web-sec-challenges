// Get the modal
let modal1 = document.getElementById("myModal1");
/*let modal2 = document.getElementById("myModal2");
let modal3 = document.getElementById("myModal3");
let modal4 = document.getElementById("myModal4");
let modal5 = document.getElementById("myModal5");*/
let modals = document.querySelectorAll(".modal");
//Get buttons
let btn1 = document.getElementById("myBtn1");
/*let btn2 = document.getElementById("myBtn2");
let btn3 = document.getElementById("myBtn3");
let btn4 = document.getElementById("myBtn4");
let btn5 = document.getElementById("myBtn5");*/
let buttons = document.querySelectorAll(".btn.btn-success");


//hints 

let hb1 = document.getElementById("hint_useragent");
let h1 = document.getElementById("h_usa");
//Opening the modal when the button is pressed
btn1.onclick = function() {
  modal1.style.display = "block";
}
/*
btn2.onclick = function() {
  modal2.style.display = "block";
}

btn3.onclick = function() {
  modal3.style.display = "block";
}

btn4.onclick = function() {
	modal4.style.display = "block";
}

btn5.onclick = function() {
  modal5.style.display = "block";
}
*/

/*
buttons.forEach(function(button) {
	let i = buttons.indexOf(button)
	button.onclick = function(i) {
		modals[i].style.display = "block";
	}
});
*/

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }

/*  if (event.target == modal2) {
    modal2.style.display = "none";
  }

  if (event.target == modal3) {
    modal3.style.display = "none";
  }

  if (event.target == modal4) {
  	modal4.style.display = "none";
  }

  if (event.target == modal5) {
    modal5.style.display = "none";
  }*/

  if (event.target == modal6) {
    modal6.style.display = "none";
  }

    if (event.target == modal7) {
    modal7.style.display = "none";
  }

}





