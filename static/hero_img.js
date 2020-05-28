
$(function(){

    window.addEventListener("scroll", changeImage)
    window.addEventListener("scroll", toggleBrand)
    window.addEventListener("scroll", toggleLogo)
    

})

const scrollAmount = 10

function changeImage() {

    let top = document.querySelector(".tier-hero").getBoundingClientRect().top
    
    if (top < scrollAmount) {
        document.querySelector(".tier-hero").style.backgroundImage =  "url(/static/images/maxwell.jpg)"
    } else {
        document.querySelector(".tier-hero").style.backgroundImage =  "url(/static/images/merlion.jpg)"
    }

}

const scrollBrand = 300

function toggleBrand() {

    
    let topLocation = document.querySelector(".tier-zero").getBoundingClientRect().top

    if (topLocation < scrollBrand) {
        document.querySelector(".tier-minus-two").style.display = "none"
    } else {
        document.querySelector(".tier-minus-two").style.display = "block"
    }

}

function toggleLogo(){

    let topLocation = document.querySelector(".tier-zero").getBoundingClientRect().top

    if (topLocation < scrollBrand) {
        document.querySelector("#fixed-logo").style.display = "block"
    } else {
        document.querySelector("#fixed-logo").style.display = "none"
    }



}