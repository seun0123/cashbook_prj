var slideWrapper = document.getElementsByClassName('content'),
    slideContainer = document.getElementsByClassName('slider-container'),
    slides = document.getElementsByClassName('slide'),
    slideCount = slides.length,
    currentIndex = 0,
    topHeight = 0,
    navPrev = document.getElementById('prev'),
    navNext = document.getElementById('next'),
    number = 0;

function calculateTallestSlide() {
    for (var i = 0; i < slideCount; i++) {
        if (slides[i].offsetHeight > topHeight) {
            topHeight = slides[i].offsetHeight;
        }
    }

    slideContainer[0].style.height = topHeight + "px";
    slideWrapper[0].style.height = topHeight + "px";
}
calculateTallestSlide();

if (slideCount > 0) {
    for (var i = 0; i < slideCount; i++) {
        slides[i].style.left = 100 * i + "%";
    }
}

function goToSlide(index) {
    slideContainer[0].style.left = -100 * index + "%";
    slideContainer[0].classList.add('animated');
    currentIndex = index;
    updateNav();
}

function updateNav() {

    if(currentIndex == 0) {
        navPrev.classList.add('disabled');
    } else {
        navPrev.classList.remove('disabled');
    }

    if(currentIndex == slideCount - 1) {
        navNext.classList.add('disabled');
    } else {
        navNext.classList.remove('disabled');
    }

}

navPrev.addEventListener('click', function(event) {
    event.preventDefault();
    goToSlide(currentIndex - 1);
});

navNext.addEventListener('click', function(event) {
    event.preventDefault();
    goToSlide(currentIndex + 1);
});

$('#bodyBG').click(function() {
    changeBG();
})

function changeBG() {
    if (number == 0) {
        $('.body').css('backgroundImage', 'var(--colorful)');
        setTimeout(() => console.log("after"), 1000);
        number = number +1;
    }

    else if (number == 1) {
        $('.body').css('backgroundImage', 'var(--default)');
        setTimeout(() => console.log("after"), 1000);
        number = number -1;
    }
}