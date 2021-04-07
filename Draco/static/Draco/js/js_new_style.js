"use strict"

//ОПРЕДЕЛЕНИЕ МОБ ИЛИ ПК
const isMobile = {
	Android: function() {
	    return navigator.userAgent.match(/Android/i);
	},
	BlackBerry: function() {
	    return navigator.userAgent.match(/BlackBerry/i);
	},
	iOS: function() {
	    return navigator.userAgent.match(/iPhone|iPad|iPod/i);
	},
	Opera: function() {
	    return navigator.userAgent.match(/Opera Mini/i);
	},
	Windows: function() {
	    return navigator.userAgent.match(/IEMobile/i);
	},
	any: function() {
	    return (
	        isMobile.Android() ||
            isMobile.BlackBerry() ||
            isMobile.iOS() ||
            isMobile.Opera() ||
            isMobile.Windows());
	}
};

if (isMobile.any()) {
    document.body.classList.add('_touch');

    let menuArrows = document.querySelectorAll('.menu__arrow');
    if (menuArrows.length>0){
        for (let index = 0; index < menuArrows.length; index++) {
            const menuArrow = menuArrows[index];
            menuArrow.addEventListener("click", function (e) {
              menuArrow.parentElement.classList.toggle('_active');
            });
        }
    }
} else {
    document.body.classList.add('_pc');
}

//МЕНЮ БУРГЕР
const iconMenu = document.querySelector('.menu__icon');
const menuBody = document.querySelector('.menu__body');
if (iconMenu) {
    iconMenu.addEventListener("click", function (e) {
        document.body.classList.toggle('_lock');
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
    });
}

//ПРОКРУТКА ПРИ КЛИКЕ
const menuLinks = document.querySelectorAll('.menu__sub-link[data-goto]');
if (menuLinks.length>0) {
    menuLinks.forEach(menuLink => {
        menuLink.addEventListener("click", onMenuLinkClick);
    });

    function onMenuLinkClick(e) {
        const menuLink = e.target;
        if (menuLink.dataset.goto && document.querySelector(menuLink.dataset.goto)) {
           const gotoBlock = document.querySelector(menuLink.dataset.goto);
           const gotoBlockValue = gotoBlock.getBoundingClientRect().top + pageYOffset - document.querySelector('header').offsetHeight;

           if(iconMenu.classList.contains('_active')) {
               document.body.classList.remove('_lock');
                iconMenu.classList.remove('_active');
                menuBody.classList.remove('_active');
           }

           window.scrollTo({
               top: gotoBlockValue,
               behavior: "smooth"
           });
           e.preventDefault();
        }
    }
}

//ФУНКЦИЯ ПОДСЧЕТА И ВЫВОДА ТЕКУЩЕГО ВРЕМЕНИ
function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    }

    function startTime() {
        var today = new Date();
        var h = today.getHours();
        var m = today.getMinutes();
        var s = today.getSeconds();
        // add a zero in front of numbers<10
        m = checkTime(m);
        s = checkTime(s);
        if (document.getElementById('time')) {
            document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
        }
        let t;
        t = setTimeout(function() {
            startTime()
        }, 500);
    }
    startTime();