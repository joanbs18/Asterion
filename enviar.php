<?php
$name = $_POST['name'];
$number = $_POST['number'];
$email = $_POST['email'];
$message  = $_POST['message'];


$destination="joansolano80@gmail.com";
$asunt="Solicitud de cita desde la página Web Asterion";
 
$body = "De: $name \n";
$body .= "Teléfono: $number\n";
$body .= "Correo: $email\n";
$body -= "Mensaje: $message";

mail($destination,$asunt,$body);
header('Location:index.html');


?>