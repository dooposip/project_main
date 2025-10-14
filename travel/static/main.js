//슬라이더
const swiper = new Swiper('.mySwiper', {
  direction: 'vertical',
  loop: true,
  speed: 1000,
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
  effect: 'slide',
  grabCursor: true,
  on: {
    slideChange: function () {
      const realIndex = this.realIndex;
      const currentNum = document.querySelector('.slide-counter .current');
      if (currentNum) {
        currentNum.textContent = String(realIndex + 1).padStart(2, '0');
      }

      document.querySelectorAll('.pagination-bullet').forEach((bullet, idx) => {
        bullet.classList.toggle('active', idx === realIndex);
      });
    }
  }
});

document.getElementById('buttonPrev').addEventListener('click', () => {
  swiper.slidePrev();
});

document.getElementById('buttonNext').addEventListener('click', () => {
  swiper.slideNext();
});

document.querySelectorAll('.pagination-bullet').forEach((bullet, idx) => {
  bullet.addEventListener('click', () => {
    swiper.slideToLoop(idx);
  });
});

var swiper2 = new Swiper(".swiper2", {
  slidesPerView: 4,
  spaceBetween: 20,
  loop: true,
  navigation: {
    nextEl: ".custom-next2",
    prevEl: ".custom-prev2",
  },
});

// 계절여행지 추천 하트 채우기/비우기
function toggleLike(el) {
  if (el.classList.contains('active')) {
    el.classList.remove('active');
    el.classList.replace('fa-solid', 'fa-regular'); // 빈 하트로
  } else {
    el.classList.add('active');
    el.classList.replace('fa-regular', 'fa-solid'); // 채운 하트로
  }
}