let elInputUsername = document.querySelector('#id_username')
let elInputPassword = document.querySelector('#id_password1')
let elInputPasswordretype = document.querySelector('#id_password2')
let elNumbertype = document.querySelector('#id_phone')
let elAgetype = document.querySelector('#id_age')
let elAddresstype = document.querySelector('#id_address')
let elJoinbutton = document.querySelector('#joinbutton')

let elPwlimitmessage = document.querySelector('.pwlimit-message')
let elPwallowmessage = document.querySelector('.pwallow-message')
let elFailuremessage = document.querySelector('.failure-message')
let elSuccessmessage = document.querySelector('.success-message')
let elMismatchmessage = document.querySelector('.mismatch-message')
let elMatchmessage = document.querySelector('.match-message')
let elMisnumbermessage = document.querySelector('.misnumber-message')
let elNumbermessage = document.querySelector('.number-message')
let elMisagemessage = document.querySelector('.misage-message')
let elMisaddressmessage = document.querySelector('.misaddress-message')

let usernameCheck = 0
let pwCheck
let phonenumberCheck = 0
let ageCheck = 1
let addressCheck = 1

elJoinbutton.disabled = true;

elInputUsername.onkeyup = function () {
    if (isMoreThan4Length(elInputUsername.value)) {
        elSuccessmessage.classList.remove('hide')
        elFailuremessage.classList.add('hide')
        usernameCheck = 1
    }
    else {
        elSuccessmessage.classList.add('hide')
        elFailuremessage.classList.remove('hide')
        usernameCheck = 0
    }
}

function isMoreThan4Length(value) {
    return value.length >= 4
}

elInputPassword.onkeyup = function () {
    if (pwConditions(elInputPassword.value)) {
        elPwlimitmessage.classList.add('hide')
        elPwallowmessage.classList.remove('hide')
        pwCheck = 1
    }
    else {
        elPwlimitmessage.classList.remove('hide')
        elPwallowmessage.classList.add('hide')
        pwCheck = 0
    }

    if (isMatch(elInputPassword.value, elInputPasswordretype.value)) {
        elMismatchmessage.classList.add('hide')
        elMatchmessage.classList.remove('hide')
    }
    else {
        elMismatchmessage.classList.remove('hide')
        elMatchmessage.classList.add('hide')
    }
}

function pwConditions(value) {
    let pwcon = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,15}$/;
    if (pwcon.test(value) === true) {
        return true;
    }
    else {
        return false;
    }
}

elInputPasswordretype.onkeyup = function () {
    if (isMatch(elInputPassword.value, elInputPasswordretype.value)) {
        elMismatchmessage.classList.add('hide')
        elMatchmessage.classList.remove('hide')
    }
    else {
        elMismatchmessage.classList.remove('hide')
        elMatchmessage.classList.add('hide')
    }
}

function isMatch (password1, password2) {
    if (password1 === password2) {
        return true;
    }
    else {
        return false;
    }
}

elNumbertype.onkeyup = function () {
    if (isNumbermatch(elNumbertype.value)) {
        elMisnumbermessage.classList.add('hide')
        elNumbermessage.classList.remove('hide')
        phonenumberCheck = 1
    }
    else {
        elMisnumbermessage.classList.remove('hide')
        elNumbermessage.classList.add('hide')
        phonenumberCheck = 0
    }
}

function isNumbermatch(value) {
    let phonenumber = /^(?=.*[0-9]).{11,11}$/;
    if (phonenumber.test(value) === true) {
        return true;
    }
    else {
        return false;
    }
}

elAgetype.addEventListener('click', function() {
    if (elAgetype.value < 0) {
        elMisagemessage.classList.remove('hide')
        ageCheck = 0
    }
    else {
        elMisagemessage.classList.add('hide')
        ageCheck = 1
    }
})
elAgetype.onkeyup = function () {
    if (elAgetype.value < 0) {
        elMisagemessage.classList.remove('hide')
        ageCheck = 0
    }
    else {
        elMisagemessage.classList.add('hide')
        ageCheck = 1
    }
}

elAddresstype.onkeyup = function () {
    if (isAddressmatch(elAddresstype.value) || elAddresstype == "") {
        elMisaddressmessage.classList.add('hide')
        addressCheck = 1
    }
    else {
        elMisaddressmessage.classList.remove('hide')
        addressCheck = 0
    }
}

function isAddressmatch(value) {
    let address = /^(?=.*[0-9]).{5,5}$/;
    if (address.test(value) === true) {
        return true;
    }
    else {
        return false;
    }
}

elInputUsername.addEventListener('keyup', button)
elInputPassword.addEventListener('keyup', button)
elInputPasswordretype.addEventListener('keyup', button)
elNumbertype.addEventListener('keyup', button)
elAgetype.addEventListener('click', button)
elAgetype.addEventListener('keyup', button)
elAddresstype.addEventListener('keyup', button)

function button() {
    switch (!(elInputUsername.value && elInputPassword.value && elInputPasswordretype.value && elNumbertype.value
        && elInputPassword.value === elInputPasswordretype.value && usernameCheck == phonenumberCheck == ageCheck == addressCheck == 1)) {
            case true : elJoinbutton.disabled = true; break;
            case false : elJoinbutton.disabled = false; break;
    }
}