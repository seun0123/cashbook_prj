let modal = document.querySelector('#modal-notice'),
    modalActive = document.querySelector('#modal-active'),
    modalClose = document.querySelector('#modal-close');

function activeModal() { 
    modal.classList.add('active');
    document.querySelector('body').style.overflow = 'hidden';
}

function hideModal() { 
    modal.classList.remove('active');
    document.querySelector('body').style.overflow = 'visible';
}

modalActive.addEventListener('click', activeModal)
modalClose.addEventListener('click', hideModal)