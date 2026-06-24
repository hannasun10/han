const header = document.querySelector("#header");
const menuButton = document.querySelector(".menu-toggle");
const nav = document.querySelector("#main-nav");
const navLinks = nav.querySelectorAll("a");
const form = document.querySelector("#contact-form");
const formStatus = document.querySelector("#form-status");

const updateHeader = () => {
  header.classList.toggle("scrolled", window.scrollY > 24);
};

const closeMenu = () => {
  menuButton.setAttribute("aria-expanded", "false");
  nav.classList.remove("open");
  document.body.classList.remove("menu-open");
};

menuButton.addEventListener("click", () => {
  const isOpen = menuButton.getAttribute("aria-expanded") === "true";
  menuButton.setAttribute("aria-expanded", String(!isOpen));
  nav.classList.toggle("open", !isOpen);
  document.body.classList.toggle("menu-open", !isOpen);
});

navLinks.forEach((link) => link.addEventListener("click", closeMenu));
window.addEventListener("scroll", updateHeader, { passive: true });
updateHeader();

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);

document.querySelectorAll(".reveal").forEach((element, index) => {
  element.style.transitionDelay = `${Math.min(index % 4, 3) * 70}ms`;
  observer.observe(element);
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const data = new FormData(form);
  const name = data.get("name").trim();
  const contact = data.get("contact").trim();
  const message = data.get("message").trim();

  if (!name || !contact || !message) {
    formStatus.textContent = "모든 항목을 입력해 주세요.";
    return;
  }

  const subject = encodeURIComponent(`[AI 강의 문의] ${name}`);
  const body = encodeURIComponent(
    `기관·성함: ${name}\n연락처: ${contact}\n\n문의 내용:\n${message}`
  );

  formStatus.textContent = "이메일 앱에서 문의 내용을 확인해 주세요.";
  window.location.href = `mailto:?subject=${subject}&body=${body}`;
});
