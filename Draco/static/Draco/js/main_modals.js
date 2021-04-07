/*задаем переменные в которые получаем все объекты класса*/
const popupLinks = document.querySelectorAll('.popup__link');
const body = document.querySelector('body');
const lockPadding = document.querySelectorAll(".lock-padding");

let unlock = true;

const timeout = 800;

/*проверка существует ли класс popup-link*/
if (popupLinks.length > 0) {
	/*цикл поиск объектов, идут в переменную popupLink */
	for (let index = 0; index < popupLinks.length; index++) {
		const popupLink = popupLinks[index];
		/*на popupLink вешается событие клик*/
		popupLink.addEventListener("click", function (e) {
			/*убираем тег # из href, popupName получает имя без #*/
			const popupName = popupLink.getAttribute('href').replace('#', '');
			/*popupName идет в переменную currentPopup #*/
			const currentPopup = document.getElementById(popupName);
			/*Вызов функции которая открывает окно*/
			popupOpen(currentPopup);
			/*не даем перезагружаться странице*/
			e.preventDefault();
		});
	}
}

/*будет проверять ссылки у которых есть класс .close-popup, нужно для закрытия*/
const popupCloseIcon = document.querySelectorAll('.close__popup');
if (popupCloseIcon.length > 0) {
	for (let index = 0; index < popupCloseIcon.length; index++) {
		const el = popupCloseIcon[index];
		/*Функция которая будет закрывать модальное окно*/
		el.addEventListener('click', function (e) {
			popupClose(el.closest('.popup'));
			e.preventDefault();
		});
	}
}

/*Функция которая открывает окно*/
function popupOpen(currentPopup) {
	if (currentPopup && unlock) {
		const popupActive = document.querySelector('.popup.open');
		if (popupActive) {
			popupClose(popupActive, false);
		} else {
			bodyLock();
		}
		currentPopup.classList.add('open');
		currentPopup.addEventListener("click", function (e) {
			if (!e.target.closest('popup__content')) {
				popupClose(e.target.closest('.popup'));
			}
		});
	}
}

/*Функция которая закрывает модальное окно */
function popupClose(popupActive, doUnlock = true) {
	if (unlock) {
		popupActive.classList.remove('open');
		if (doUnlock) {
			bodyUnLock();
		}
	}
}
/*Функция которая скрывает скролл для сайта и высчитывает его ширину*/
function bodyLock() {
	const lockPaddingValue = window.innerWidth - document.querySelector('.wrapper').offsetWidth + 'px';

	if (lockPadding.length > 0) {
		for (let index = 0; index < lockPadding.length; index++) {
			const el = lockPadding[index];
			el.style.paddingRight = lockPaddingValue;
		}
	}
	body.style.paddingRight = lockPaddingValue;
	body.classList.add('lock');

	unlock = false;
	setTimeout(function() {
		unlock = true;
	}, timeout);
}

function bodyUnLock() {
	setTimeout(function () {
	    if (lockPadding.length > 0) {
		    for (let index = 0; index < lockPadding.length; index++) {
                const el = lockPadding[index];
                el.style.paddingRight = '0px';
            }
		}
		body.style.paddingRight = '0px';
		body.classList.remove('lock');
	}, timeout);

	unlock = false;
	setTimeout(function() {
		unlock = true;
	}, timeout);
}

/*попап закрывается через клавишу esc*/
document.addEventListener('keydown', function (e) {
	if (e.key === "Escape") {
	const popupActive = document.querySelector('.popup.open');
	popupClose(popupActive);
	}
});