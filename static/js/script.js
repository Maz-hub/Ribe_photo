// NAVBAR SCROLL EFFECT
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

// GO TO TOP BTN
function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// SMOOTH SCROLLING
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
document.addEventListener("DOMContentLoaded", function () {
  // Select all elements with the class 'open-modal'
  document.querySelectorAll(".open-modal").forEach((el) => {
    el.addEventListener("click", function (e) {
      e.preventDefault(); // Prevent default behavior of the <a> tag

      // Get the image URL and title from the data attributes
      const imageUrl = this.getAttribute("data-bs-image");
      const imageTitle = this.getAttribute("data-bs-title");

      // Set the modal image src
      const modalImage = document.getElementById("modalImage");
      modalImage.setAttribute("src", imageUrl);

      // Set the modal title
      const modalTitle = document.getElementById("imageModalLabel");
      modalTitle.textContent = imageTitle;
    });
  });
});

// EMAILS
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contactForm");
  const flashMessage = document.getElementById("flash-message");

  form.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(form);

    try {
      // Ensure the request goes to the correct route and uses POST
      const response = await fetch("/send_email", {
        method: "POST",
        body: formData,
      });

      const messageText = await response.text();

      if (response.ok) {
        // Show success message
        flashMessage.textContent = "Your message has been sent successfully!";
        flashMessage.className = "alert alert-success";
      } else {
        // Show error message
        flashMessage.textContent = `Error: ${messageText}`;
        flashMessage.className = "alert alert-danger";
      }

      // Display the message and hide it after a few seconds
      flashMessage.style.display = "block";
      setTimeout(() => {
        flashMessage.style.display = "none";
      }, 5000);

      // Clear form fields on success
      if (response.ok) {
        form.reset();
      }
    } catch (error) {
      // Show error message if Fetch fails
      flashMessage.textContent = "An error occurred. Please try again.";
      flashMessage.className = "alert alert-danger";
      flashMessage.style.display = "block";

      setTimeout(() => {
        flashMessage.style.display = "none";
      }, 5000);
    }
  });
});
