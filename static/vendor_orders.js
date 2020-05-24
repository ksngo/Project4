$(function(){

    checkboxElements = document.getElementsByClassName("checkbox")

    for (i=0; i<checkboxElements.length;i++){
        checkboxElements[i].addEventListener('change', createValue )
    }

})

function createValue(){
    
    this.nextElementSibling.setAttribute("name","special")
    document.getElementById('delivery-status').submit()
    
}