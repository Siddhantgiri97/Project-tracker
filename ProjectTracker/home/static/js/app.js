const menu = document.querySelector("#mobile-menu")
const menuLinks = document.querySelector('.navbar_menu')
const navLogo = document.querySelector("#navbar_logo")
const body = document.querySelector('body')


//Display Mobile Menu
const mobileMenu = () =>{
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
    body.classList.toggle('active')
}

menu.addEventListener('click',mobileMenu)


