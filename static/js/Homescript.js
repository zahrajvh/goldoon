

// Float Navbar
const navbtn = document.querySelector(".btnav");
const navbarlist = document.querySelector(".navbar-items");
const menuicon = document.querySelector(".dot-menu__checkbox");
let sticky = document.querySelector(".navbar-org").offsetHeight + 30;
window.addEventListener("scroll", function () {
    if (window.pageYOffset > sticky) {
        navbtn.classList.add("show");
        navbarlist.classList.add('right');
        navbarlist.classList.add('float');
    }
    else {
        navbarlist.classList.remove("float");
        navbarlist.classList.remove('left');
        menuicon.classList.remove("active");
        navbtn.classList.remove("show");
        navbarlist.style.right = "";
    }
})
navbtn.addEventListener("click", function (e) {
    e.preventDefault();
    menuicon.classList.toggle("active");
    navbarlist.classList.toggle('right');
    navbarlist.classList.toggle('left');
})


// text slider

const control = document.querySelectorAll(".controler");
const TextSlide = document.querySelectorAll(".inf-text");
const ImgSlide = document.querySelectorAll(".slider-img");
let num = -1;

function secund() {
    for (let n = 0; n < control.length; n++) {
        control[n].classList.remove('active');
    }

    if (num <= 3) {
        num = num + 1;
    } else {
        num = 0;
    }

    control[num].classList.add("active");

    let Circle_id = control[num].getAttribute("id");

    for (let i = 0; i < TextSlide.length; i++) {
        TextSlide[i].classList.remove('show-inf');
        ImgSlide[i].classList.remove('show-img');
        let Text_id = TextSlide[i].getAttribute("id");

        if (Circle_id == Text_id) {
            TextSlide[i].classList.add("show-inf")
            ImgSlide[i].classList.add("show-img")
        }
    }
    const slideTimeout = setTimeout(secund, 5000);
}
secund();

function myGreeting() {
  document.getElementById("demo").innerHTML = "Happy Birthday to You !!"
}

function myStopFunction() {
  clearTimeout(myTimeout);
}

control.forEach(circle => {
    circle.addEventListener("click", function () {
        for (let n = 0; n < control.length; n++) {
            control[n].classList.remove('active');
        }
        circle.classList.add("active");

        let Circle_id = circle.getAttribute("id");

        for (let i = 0; i < TextSlide.length; i++) {
            TextSlide[i].classList.remove('show-inf');
            ImgSlide[i].classList.remove('show-img');
            let Text_id = TextSlide[i].getAttribute("id");

            if (Circle_id == Text_id) {
                TextSlide[i].classList.add("show-inf")
                ImgSlide[i].classList.add("show-img")
                num = i-1;
            }
        }
        // click!
        clearTimeout(slideTimeout);  
        secund();
    })
});



// video play

const video = document.querySelector(".video");
const video_overlay = document.querySelector(".overlay");
const closeicon = document.querySelector(".close-icon");
// const videoicon = document.querySelector(".play-icon").childNodes[1];

document.querySelector(".video-Preview").addEventListener("click", function(){
    video.classList.add("play-vid");
})

// video_overlay.addEventListener("click", function(){
//     video.classList.remove("play-vid");
    
// })

closeicon.addEventListener("click", function(e){
    video.classList.remove("play-vid");
    e.preventDefault();
    console.log("dddd");
})


// FAQ

const title = document.querySelectorAll('.accordion-title');

title.forEach(item => {
    item.addEventListener('click', function(){
        // const span = document.getElementsByTagName(span);
        // console.log(span);
        item.classList.toggle('active');
        const content = item.nextElementSibling;
        if(content.style.height){
            content.style.height = null
            content.style.padding = null;
            content.style.overflow = "hidden";
            // +

        }else{
            content.style.height = (content.scrollHeight) + 'px';
            content.style.padding = '1.8rem 2.5rem';
            content.style.padding = '1.8rem 2.5rem';
            content.style.overflow = "scroll";
            // -
        }
    })
} )

