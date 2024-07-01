<?php
if ($_SERVER["REQUEST_METHOD"] != "POST") {
    http_response_code(405);
    exit;
}
  // Configuración del correo electrónico
  $destino = "ispamer98@gmail.com";
  $asunto = "Mensaje desde formulario de contacto";

  // Recuperar información del formulario
  $nombre = $_POST["nombre"];
  $email = $_POST["email"];
  $mensaje = $_POST["mensaje"];

  // Crear mensaje
  $mensaje = "Nombre: $nombre\n";
  $mensaje .= "Correo electrónico: $email\n";
  $mensaje .= "Mensaje: $mensaje\n";

  // Enviar correo electrónico
  mail($destino, $asunto, $mensaje);

  // Redirigir a una página de agradecimiento
  header("Location: index.html");
  exit;
?>