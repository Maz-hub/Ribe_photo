// Navbar Scroll Effect

function userScroll() {
  const navbar = document.querySelector(".navbar");
  const toTopBtn = document.querySelector("#to-top");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("bg-dark");
      navbar.classList.add("navbar-sticky");
      toTopBtn.classList.add("show");
    } else {
      navbar.classList.remove("bg-dark");
      navbar.classList.remove("navbar-sticky");
      toTopBtn.classList.remove("show");
    }
  });
}

// Go to top

function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// Smooth scrolling

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// run when DOM is loaded / Event Listeners
document.addEventListener("DOMContentLoaded", userScroll);
document.querySelector("#to-top").addEventListener("click", scrollToTop);

// MASONRY

window.onload = () => {
  const grid = document.querySelector(".masonry-grid");
  if (grid) {
    const masonryInstance = new Masonry(grid, {
      itemSelector: ".gallery-item",
      gutter: 10,
    });

    // Force Masonry to re-layout after window resizing
    window.addEventListener("resize", () => {
      masonryInstance.layout();
    });
  }
};

// MODAL
document.addEventListener('DOMContentLoaded', function () {
  // Select all elements with the class 'open-modal'
  document.querySelectorAll('.open-modal').forEach((el) => {
    el.addEventListener('click', function (e) {
      e.preventDefault(); // Prevent default behavior of the <a> tag

      // Get the image URL and title from the data attributes
      const imageUrl = this.getAttribute('data-bs-image');
      const imageTitle = this.getAttribute('data-bs-title');

      // Set the modal image src
      const modalImage = document.getElementById('modalImage');
      modalImage.setAttribute('src', imageUrl);

      // Set the modal title
      const modalTitle = document.getElementById('imageModalLabel');
      modalTitle.textContent = imageTitle;
    });
  });
});



