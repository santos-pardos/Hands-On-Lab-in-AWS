document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');

  modeSwitch.addEventListener('click', function () {
    document.documentElement.classList.toggle('dark');
  });
});

function openModal(){
  let modal= document.querySelector('#modal-window');
  modal.classList.add("showModal");
}

function closeM(){
    let m= document.querySelector('#modal-window');
  m.classList.remove("showModal");
}

document.getElementsByClassName('.mode-switch').onclick = function() {
  document.body.classList.toggle('dark');
}

const cardItems = document.querySelectorAll('.main-card');
const modalHeader = document.querySelector('.modalHeader-js');
const modalCardPrice = document.querySelector('.amount');

cardItems.forEach((cardItem) => {
  cardItem.addEventListener('click', function () {
    const cardHeader = cardItem.querySelector('.cardText-js');
    const cardPrice = cardItem.querySelector('.card-price');

    modalHeader.innerText = cardHeader.innerText;
    modalCardPrice.innerText = cardPrice.innerText;
  });
});

window.onkeydown = function (event) {
  if(event.keyCode == 27) {
    closeM();
  }
}

var modal =  document.querySelector('#modal-window');
window.onclick = function (event) {
  if(event.target == modal) {
    closeM();
  }
}

