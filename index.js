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

window.addEventListener('DOMContentLoaded', function() {
  var responsiveImage = document.getElementById('responsiveImage');
  var btn= this.document.getElementById('btn');

  function setResponsiveImage() {
    // Obtener el ancho de la pantalla
    var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

    // Cambiar la imagen según el ancho de la pantalla
    if (windowWidth <= 600) {
      responsiveImage.src = 'img/asterion-blanco-01-logo.png';
      btn.classList.add('bluebackground');
    }
  }

  // Llamar a la función inicialmente y escuchar el evento de cambio de tamaño de la ventana
  setResponsiveImage();
  window.addEventListener('resize', setResponsiveImage);
});


