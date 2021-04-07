// настроки слайдера SWIPER
let wrapper = document.querySelector('.wrapper__main_page');

let pageSlider = new Swiper('.page__slider', {
	//Свои классы
	wrapperClass: 'page__wrapper',
	slideClass: 'page__screen',

	//Вертикальный слайдер
	direction: 'vertical',

	//Кол-во сладов для показа
	slidesPerView: 'auto',

	//Параллакс
	parallax: true,

	//Управление клавиатурой
	keyboard: {
		enabled: true,
		onlyInViewport: true,
		pageUpDown: true,
	},

	//Управление колесом мыши
	mousewheel: {
		sensitivity: 1,
	},

	//Отключение ф-онала = слайдов меньше, чем нужно
	watchOverflow: false,

	//Скорость прокрутки
	speed: 800,

	//Автообновление при добавлении слайдов
	observer: true,
	observeParents: true,
	observeSlideChildren: true,

	//Навигация
	pagination: {
		el: '.page__pagination',
		type: 'bullets',
		clickable: true,
		bulletClass: "page__bullet",
		bulletActiveClass: "page__bullet_active",
	},
	//Скролл
	scrollbar: {
		el: '.page__scroll',
		dragClass: "page__drag-scroll",
		draggable: true,
	},
	//Отключение автоинициализации
	init: false,
	//События
	on: {
		//Событие инифиализации
		init: function () {
			menuSlider();
			setScrollType();
			wrapper.classList.add('_loaded');
		},
		//Событие смены слайда
		slideChange: function () {
			menuSliderRemove();
			MenuLinks[pageSlider.realIndex].classList.add('_active');
		},
		resize: function () {
			setScrollType();
		}
	},
});

let MenuLinks = document.querySelectorAll('.header-menu__link');

function menuSlider() {
	if (MenuLinks.length > 0) {
		MenuLinks[pageSlider.realIndex].classList.add('_active');
		for (let index = 0; index < MenuLinks.length; index++) {
			const MenuLink = MenuLinks[index];
			MenuLink.addEventListener("click", function (e) {
				menuSliderRemove();
				pageSlider.slideTo(index, 800);
				MenuLinks.classList.add('_active');
				e.preventDefault();
			});
		}
	}
}

function menuSliderRemove() {
	let MenuLinkActive = document.querySelector('.header-menu__link._active');
	if (MenuLinkActive) {
		MenuLinkActive.classList.remove('_active');
	}
}

function setScrollType() {
	if(wrapper.classList.contains('_free')) {
		wrapper.classList.remove('_free');
		pageSlider.params.freeMode = false;
	}
	for (let index = 0; index < pageSlider.slides.length; index++) {
		const pageSlide = pageSlider.slides[index];
		const pageSlideContent = pageSlide.querySelector('.screen__content');
		if (pageSlideContent) {
			const pageSlideContentHeight = pageSlideContent.offsetHeight;
			if (pageSlideContent > window.innerHeight) {
				wrapper.classList.add('_free');
				pageSlider.params.freeMode = true;
				break;
			}
		}
	}
}

pageSlider.init();