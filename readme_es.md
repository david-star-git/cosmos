# Manual de uso del Bot de Discord

## Versiones en idioma
[![Inglés](https://img.shields.io/badge/Inglés-English-blue)](readme.md)
[![Alemán](https://img.shields.io/badge/Alemán-German-blue)](readme_de.md)
[![Español](https://img.shields.io/badge/Español-Spanish-blue)](readme_es.md)

Bienvenido a la documentación de **Cosmos**, un versátil y potente Bot de Discord diseñado para mejorar la experiencia en tu servidor. Este manual proporciona una visión general de las características del bot y cómo utilizarlas eficazmente.

## Contenidos

- [Introducción](#introducción)
- [Primeros pasos](#primeros-pasos)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
- [Configuración](#configuración)
- [Comandos del bot](#comandos-del-bot)
- [Colaboración](#colaboración)

## Introducción

**Cosmos** es un Bot de Discord desarrollado para hacer que tu servidor sea más interactivo y divertido. Está equipado con una serie de características que permiten la moderación, entretenimiento, recuperación de información y mucho más. Ya sea que administres una comunidad de juegos, un grupo de estudio u otro tipo de servidor, **Cosmos** tiene algo que ofrecer.

## Primeros pasos

### Requisitos

- Una cuenta en [Discord](https://discord.com/)
- Acceso a un servidor de Discord donde tengas permisos de administrador

### Instalación

#### Paso 1: Portal de Desarrolladores de Discord

1. Ve al [Portal de Desarrolladores de Discord](https://discord.com/developers/applications/).
2. Inicia sesión con tu cuenta de Discord.

#### Paso 2: Crear una nueva aplicación

1. Haz clic en el botón "New Application" (Nueva Aplicación).
2. Ingresa un nombre para tu aplicación (este será el nombre de tu bot).
3. Haz clic en "Create" (Crear).

#### Paso 3: Crear el bot

1. Selecciona "Bot" en el menú izquierdo.
2. Haz clic en "Add Bot" (Agregar Bot).
3. Confirma la acción haciendo clic en "Yes, do it!" (Sí, hazlo).

#### Paso 4: Copiar el token del bot

1. En la sección "TOKEN" encontrarás el token de tu bot. Haz clic en "Copy" (Copiar) para copiar el token al portapapeles. Nota: Mantén este token en secreto, ya que proporciona acceso a tu bot.

#### Paso 5: Invitar al bot a un servidor

1. Regresa a la página de tu aplicación haciendo clic en el nombre de la aplicación en la esquina superior izquierda.
2. Selecciona "OAuth2" en el menú izquierdo.
En "OAuth2 URL Generator", selecciona "bot" y "applications.commands" en los Scopes.
Elige los permisos que deseas otorgar a tu bot (por ejemplo, "Leer Mensajes", "Enviar Mensajes", etc.). El bot debe tener permisos de administrador.
Copia el enlace generado por OAuth2 y pégalo en tu navegador web.
Selecciona un servidor al que quieras invitar a tu bot y confirma la invitación.

#### Paso 6: Configuración del bot

# Configuración

El archivo `config.json` te permite personalizar varios aspectos de **Cosmos** para adaptarlo a las necesidades de tu servidor. Aquí tienes una descripción de las opciones de configuración:

- **nombre:** El nombre que se mostrará en el servidor para el bot.
- **id:** La ID del bot.
- **actividad:** El estado de actividad que se mostrará para el bot (por ejemplo, "Observando el universo").
- **propietario:** La ID del propietario del bot, con privilegios especiales.

### Canales

- **log_channel:** El canal donde se enviarán los registros de actividad y notificaciones del bot.
- **announcement_channel:** El canal para anuncios importantes del equipo en el servidor.
- **suggestion_channel:** El canal donde los usuarios pueden enviar sugerencias.
- **ticket_category:** La categoría para crear canales de soporte.
- **closed_category:** La categoría a la que se trasladarán los canales de tickets cerrados o completados.

### Roles

- **verify_role:** El rol que se asigna a los usuarios después de verificar.
- **ticket_role:** El rol otorgado a los usuarios que tienen acceso para moderar los tickets de soporte.
- **double_xp_role:** El rol que otorga a los usuarios experiencia doble en el servidor.

Además, el archivo principal del bot permite asignar roles a niveles específicos para un sistema de niveles. El diccionario `roles` asigna IDs de roles a niveles específicos. Los usuarios recibirán estos roles cuando alcancen los niveles especificados. Puedes editar este diccionario para agregar o eliminar roles y niveles.

```py
roles = {
    0:   1127584577683202148,
    5:   1127584523702521916,
    10:  1127584455456981002,
    15:  1127584401342091314,
    20:  1127584356777599047,
    25:  1127584304713695323,
    30:  1127584248652627999,
    35:  1127584186715353098,
    40:  1127584121418416178,
    45:  1127584069883019375,
    50:  1127583980565299273,
    60:  1127583919001313450,
    70:  1127583602851446814,
    80:  1127583573856239627,
    90:  1127583535272820737,
    115: 1127583507514929294,
    130: 1127583471947235338,
    160: 1127583438690603079,
    200: 1127579753663172608
}
```

### Token

1. Crea un archivo llamado `.env` en la misma carpeta donde se encuentra `index.py`.
2. Escribe la siguiente línea: `TOKEN = "TuToken"`, reemplazando "TuToken" por el token real del bot.

#### Paso 7: Ejecutar el código

1. Asegúrate de tener Python instalado. Si no lo tienes, puedes descargarlo [aquí](https://www.python.org/downloads/).
2. Instala los paquetes de Python: `pip install -r requirements.txt`
3. Ejecuta tu código.
Tu bot debería conectarse a Discord y responder a comandos o eventos.

## Comandos del bot

Aquí tienes algunos de los comandos más importantes admitidos por **Cosmos**:

### Ban

- **Descripción:** Prohíbe a un usuario en el servidor.
- **Uso:** `/ban [usuario] [razón]`

### Kick

- **Descripción:** Expulsa a un usuario del servidor.
- **Uso:** `/kick [usuario] [razón]`

### Mute

- **Descripción:** Silencia a un usuario (no podrá escribir después).
- **Uso:** `/mute [usuario] [razón]`

### Unmute

- **Descripción:** Desmutear a un usuario.
- **Uso:** `/unmute [usuario] [razón]`

### Limpiar

- **Descripción:** Elimina una cantidad de mensajes en un canal.
- **Uso:** `/clear [cantidad]`

### Información

- **Descripción:** Muestra el historial de sanciones de un usuario guardado en `users.db`.
- **Uso:** `/info [usuario]`

### Advertencia

- **Descripción:** Advierte a un usuario.
- **Uso:** `/warn [usuario] [razón]`

### Restablecer

- **Descripción:** Restablece la información (historial de sanciones, nivel) de un usuario. También se puede utilizar para agregar usuarios a la base de datos.
- **Uso:** `/unmute [usuario] [razón]`

### Información del servidor

- **Descripción:** Muestra información sobre el servidor.
- **Uso:** `/serverinfo`

### Avatar

- **Descripción:** Muestra el avatar (imagen de perfil) de un usuario.
- **Uso:** `/avatar [usuario]`

### Sugerencia

- **Descripción:** Los usuarios pueden usarlo para enviar sugerencias al equipo.
- **Uso:** `/suggest [mensaje]`

### Anunciar

- **Descripción:** El equipo puede usarlo para enviar anuncios uniformes a los usuarios.
- **Uso:** `/announce [mensaje]`

### Ping

- **Descripción:** Muestra el ping del bot.
- **Uso:** `/ping`

### Rango

- **Descripción:** Muestra tu nivel.
- **Uso:** `/rank`

### Establecer nivel

- **Descripción:** Establece el nivel de un usuario.
- **Uso:** `/level [usuario] [nivel]`

### Verificar

- **Descripción:** Permite a los usuarios verificar su cuenta.
- **Uso:** `/verify`

### Reglas

- **Descripción:** Envía las reglas del servidor (deben modificarse manualmente en `index.py` en las líneas 526-536).
- **Uso:** `/rules`

### Ticket

- **Descripción:** Permite a los usuarios crear un ticket.
- **Uso:** `/ticket`

## Colaboración

¡Agradecemos las contribuciones de la comunidad! Si deseas contribuir a **Cosmos**, sigue estos pasos:

1. Haz un "Fork" del repositorio.
2. Crea una nueva rama.
3. Agrega tus mejoras o correcciones de errores.
4. Envía una solicitud de extracción.

¡Gracias por elegir **Cosmos**! Esperamos que este bot brinde mucho valor y diversión a tu servidor de Discord. Si tienes sugerencias o solicitudes de funciones, ¡no dudes en hacérnoslo saber!
