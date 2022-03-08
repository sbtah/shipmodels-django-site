const modal = document.querySelector(".modal") ;
const modalBtn = document.querySelector(".modal__btn")
const previews = document.querySelectorAll(".modal__gallery img") ;
const original = document.querySelector(".modal__full-img") ;
const caption = document.querySelector(".caption");

previews.forEach(preview => {
    preview.addEventListener("click" , () => {
        modal.classList.add("open");
        original.classList.add("open");
       
        // Dynamic img and txt change 
        const originalSrc = preview.getAttribute("data-original");
        original.src = `/media/images/${originalSrc}`;
        const altTxt = preview.alt ;
        caption.textContent = altTxt ;
        
        
    })
})

modal.addEventListener("click" , (e) =>{
if(e.target.classList.contains("modal")) {
    modal.classList.remove("open");
    original.classList.remove("open")
}

});

modalBtn.addEventListener("click" , (e) =>{
    if(modal.classList.contains("modal")) {
        modal.classList.remove("open");
        original.classList.remove("open")
        console.log("click");
        
    }
    
    });