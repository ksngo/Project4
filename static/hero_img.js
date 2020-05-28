
$(function(){

    window.addEventListener("scroll", changeImage)
    window.addEventListener("scroll", toggleBrand)
    window.addEventListener("scroll", toggleLogo)
    
    

})



function changeImage() {

    let top = document.querySelector(".tier-hero").getBoundingClientRect().top
    
    if (top < 20) {
        document.querySelector(".tier-hero").style.backgroundImage =  "url(/static/images/maxwell.jpg)"
    } else {
        document.querySelector(".tier-hero").style.backgroundImage =  "url(/static/images/merlion.jpg)"
    }

}


function toggleBrand() {

    
    let topLocation = document.querySelector(".tier-zero").getBoundingClientRect().top

    if (topLocation < 300) {
        document.querySelector(".tier-minus-two").style.display = "none"
    } else {
        document.querySelector(".tier-minus-two").style.display = "block"
    }

}



// topOne refers to the distance from top to 2nd box(below hero image box)
// topTwo refers to distance from top to box(middle of 2nd image)
// topThree refers to distance from top to box(last box above footer)

function toggleLogo(){

    let topOne = document.querySelector(".tier-zero").getBoundingClientRect().top
    let topTwo = document.querySelector(".tier-three").getBoundingClientRect().top
    let topThree = document.querySelector(".tier-six").getBoundingClientRect().top

    if (topOne < 300 && topTwo > 400 ) {
        document.querySelector("#fixed-logo").style.display = "block"
    } else if (topThree <0) {
        document.querySelector("#fixed-logo").style.display = "block"
    } else {
        document.querySelector("#fixed-logo").style.display = "none"
    }

}


