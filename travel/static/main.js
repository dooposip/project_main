//슬라이더
var swiper = new Swiper(".mySwiper", {
  loop:true,
  autoplay: {
      delay: 3000,
      disableOnInteraction: false,
  },
  navigation: {
    nextEl: "#buttonRight",
    prevEl: "#buttonLeft",
  },
});

var swiper2 = new Swiper(".swiper2", {
  slidesPerView: 4,
  spaceBetween: 20,
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