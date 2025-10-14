// 페이지 버튼 클릭시 동작
    const page_elements = document.querySelectorAll('.page-link')
    page_elements.forEach(element =>{
            element.addEventListener('click', function(){
                document.getElementById('page').value = this.dataset.page;
                document.getElementById('searchForm').submit();
            })
    })
