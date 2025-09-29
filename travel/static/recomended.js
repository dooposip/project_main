function toggleLike(el) {
  // 하트 채우기/비우기
  if (el.classList.contains('active')) {
    el.classList.remove('active');
    el.classList.replace('fa-solid', 'fa-regular'); // 빈 하트로
  } else {
    el.classList.add('active');
    el.classList.replace('fa-regular', 'fa-solid'); // 채운 하트로
  }
}