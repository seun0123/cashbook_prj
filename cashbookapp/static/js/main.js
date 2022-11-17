var loading = document.querySelector('#loading-notice'),
    checkValue = 0,
    slideWrapper = document.getElementsByClassName('content'),
    slideContainer = document.getElementsByClassName('slider-container'),
    slides = document.getElementsByClassName('slide'),
    slideCount = slides.length,
    currentIndex = 0,
    topHeight = 0,
    navPrev = document.getElementById('prev'),
    navNext = document.getElementById('next');

document.querySelector('.signup').addEventListener('click', () => {
    loading.classList.add('active');
    document.querySelector('body').style.overflow = 'hidden';

    setTimeout(function() {location.href = 'account/signup';
    loading.classList.remove('active');
    document.querySelector('body').style.overflow = 'visible';
    }, 3000);
})

document.querySelector('.toggle').addEventListener('click', () => {
    if (checkValue == 0) {
        document.querySelector('.theme').checked = true;
        document.querySelector('.body').style.backgroundImage = 'var(--colorful)';
        checkValue = checkValue + 1
    }
    else if (checkValue == 1) {
        document.querySelector('.theme').checked = false;
        document.querySelector('.body').style.backgroundImage = 'var(--default)';
        checkValue = checkValue - 1
    }
})

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

window.addEventListener("load", function() {
    clockRun();
});

function clockRun() {
    var d = new Date();

    var s = d.getSeconds();
    var s_angle = s * 6;
    var s_angle_value = "rotate(" + s_angle + "deg)";
    document.getElementById("second").style.transform = s_angle_value;

    var m = d.getMinutes();
    var m_angle = m * 6;
    var m_angle_value = "rotate(" + m_angle + "deg)";
    document.getElementById("minute").style.transform = m_angle_value;

    var h = d.getHours();
    if(h<12){
        var h = h;
    } else{
        var h = h - 12;
    }

    var h_angle = (h * 30) + (30 / 60 * m);
    var h_angle_value = "rotate(" + h_angle + "deg)";
    document.getElementById("hour").style.transform = h_angle_value;

    setTimeout(clockRun, 1000);
}