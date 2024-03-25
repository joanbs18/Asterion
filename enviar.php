<?php
// Validación de datos
// Validación de datos
$name = isset($_POST['name']) ? htmlspecialchars($_POST['name']) : '';
$number = isset($_POST['number']) ? htmlspecialchars($_POST['number']) : '';
$email = isset($_POST['email']) ? filter_var($_POST['email'], FILTER_VALIDATE_EMAIL) : '';
$message = isset($_POST['message']) ? htmlspecialchars($_POST['message']) : '';

// Verifica si los datos son válidos antes de proceder
if ($name && $number && $email && $message) {
    $destination = "joansolano80@gmail.com";
    $asunto = "Solicitud de cita desde la página Web Asterion";
    
    $body = "De: $name \n";
    $body .= "Teléfono: $number\n";
    $body .= "Correo: $email\n";
    $body .= "Mensaje: $message";

    // Intenta enviar el correo y maneja errores si los hay
    try {
        mail($destination, $asunto, $body);
         echo $body;
       // header('Location: index.html');
        exit;
    } catch (Exception $e) {
        echo 'Error al enviar el correo: ' . $e->getMessage();
    }
    
} else {
     echo $name, ', ', $number, ', ', $email, ', ', $message;
    echo 'Datos no válidos. Por favor, complete todos los campos correctamente.';
}
?>