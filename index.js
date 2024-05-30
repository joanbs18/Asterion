window.onload = function () {
  $("#loader").fadeOut();
  $("body").removeClass("hidden");
};

//ESTE METODO ES PARA LAS ANIMACIONES

//SE UTILIZA PARA ACTUALIZAR EL AÑO DE LA PAGINA AUTOMATICAMENTE
document.addEventListener("DOMContentLoaded", function () {
  var yearSpan = document.getElementById("currentYear");
  if (yearSpan) {
    var currentYear = new Date().getFullYear();
    yearSpan.textContent = currentYear;
  }
});

window.addEventListener("DOMContentLoaded", function () {
  var responsiveImage = document.getElementById("responsiveImage");
  var btn = this.document.getElementById("btn");

  function setResponsiveImage() {
    // Obtener el ancho de la pantalla
    var windowWidth =
      window.innerWidth ||
      document.documentElement.clientWidth ||
      document.body.clientWidth;

    // Cambiar la imagen según el ancho de la pantalla
    if (windowWidth <= 600) {
      responsiveImage.src = "img/asterion-blanco-01-logo.png";
      btn.classList.add("bluebackground");
    }
  }

  // Llamar a la función inicialmente y escuchar el evento de cambio de tamaño de la ventana
  setResponsiveImage();
  window.addEventListener("resize", setResponsiveImage);
});

var checkLanguage = document.querySelector(".input__language");

checkLanguage.addEventListener("click", language);

function language() {
  let id = checkLanguage.checked;
  if (id === true) {
    location.href = "en.html";
  } else {
    location.href = "index.html";
  }
}

var listItems = document.getElementById("list").getElementsByTagName("li");
var toggler = document.getElementById("toggler");

// Agrega un evento de clic a cada elemento <li>
for (var i = 0; i < listItems.length; i++) {
  listItems[i].addEventListener("click", function () {
    toggler.checked = false;
  });
}
const menu = document.querySelector(".list");
const menuLinks = document.querySelectorAll('.list li a[href^="#"]');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      const id = entry.target.getAttribute("id");
      const menuLink = document.querySelector(`.list li a[href="#${id}"]`);
      console.log(menuLink);
      if (entry.isIntersecting) {
        console.log(document.querySelector(".list li a.selected"));
        document
          .querySelector(".list li a.selected")
          .classList.remove("selected");
        menuLink.classList.add("selected");
      }
    });
  },
  { rootMargin: "-30% 0px -70% 0px" }
);

menuLinks.forEach((menuLink) => {
  menuLink.addEventListener("click", function () {
    menu.classList.remove("menu_opened");
  });

  const hash = menuLink.getAttribute("href");
  const target = document.querySelector(hash);
  if (target) {
    observer.observe(target);
  }
});


function envioFormulario(){
  alert("ENVIADO\nGracias por tu mensaje. Nos pondremos en contacto contigo en la mayor brevedad posible");
}

function sendForm(){
  alert("SUBMITTED\nThank you for your message! We will get in touch with you as soon as possible.");
}