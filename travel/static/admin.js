const buttons = document.querySelectorAll('.season-btn');
const seasonInput = document.getElementById('season-input');
const selectedSeasons = new Set();  // 중복 방지 + 선택 해제 가능

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.getAttribute('data-value');
        if (selectedSeasons.has(value)) {
        selectedSeasons.delete(value);
        button.classList.remove('selected');
        } else {
        selectedSeasons.add(value);
        button.classList.add('selected');
        }

        // 쉼표로 구분된 문자열로 입력값 설정
        seasonInput.value = Array.from(selectedSeasons).join(',');
    });
});
