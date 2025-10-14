function selectDestination(city) {
  alert(`${city}을(를) 선택하셨습니다!\n\n다음 페이지에서 ${city}의 상세 정보를 확인하실 수 있습니다.`);
  // 실제로는 다음 페이지 이동 가능:
  // window.location.href = `/sub/detail/${city}`;
}

function filterDestinations() {
  const searchInput = document.getElementById('searchInput').value.toLowerCase();
  const cards = document.querySelectorAll('.destination-card');

  cards.forEach(card => {
    const title = card.querySelector('.card-title').textContent.toLowerCase();
    const description = card.querySelector('.card-description').textContent.toLowerCase();
    const tags = Array.from(card.querySelectorAll('.tag'))
      .map(tag => tag.textContent.toLowerCase())
      .join(' ');
    const searchText = `${title} ${description} ${tags}`;

    if (searchText.includes(searchInput)) {
      card.style.display = 'block';
      card.style.animation = 'fadeInUp 0.4s ease both';
    } else {
      card.style.display = 'none';
    }
  });
}

// 카드 순차적 등장 애니메이션
document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.destination-card');
  cards.forEach((card, index) => {
    card.style.animation = `fadeInUp 0.6s ease ${index * 0.1}s both`;
  });
});
