const updateHeaderButton = document.querySelector('#update_header');


const header = document.querySelector('header');


updateHeaderButton.addEventListener('click', function() {
   
    header.textContent = 'New Header!!!';
});