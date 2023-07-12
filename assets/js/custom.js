// ==================
// Scroll top button - START
// ==================

const scrollToTopBtn = document.getElementById("scrollToTopBtn");
const rootElement = document.documentElement;

function scrollFunction() {
  if (document.body.scrollTop > 100 || rootElement.scrollTop > 100) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
}

// When the user scrolls down 100px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction()
};

// When the user clicks on the button, scroll to the top of the document
function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  })
}

scrollToTopBtn.addEventListener("click", scrollToTop)
// ==================
// Scroll top button - END
// ==================
