<?php
$name = $_POST['name'];
$number = $_POST['number'];
$email = $_POST['email'];
$messaje = $_POST['messaje'];


$destination="joansolano80@gmail.com";
$asunt="Solicitud de cita desde la página Web Asterion";
 
$body = "De: $name \n";
$body .= "Teléfono: $number";
$body .= "Correo: $email";
$body -= "Mensaje: $messaje";

mail($destination,$asunt,$body);


?>