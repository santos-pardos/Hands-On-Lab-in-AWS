# Instalación de ONLYOFFICE Workspace Community en AWS

**2MI · Ofimática** | Práctica guiada

*Amazon Linux 2023 · t3.large · Instalación con Docker*

\---

## Parte 1 · Instalación de ONLYOFFICE en AWS

### 1\. Qué vamos a instalar

Vamos a crear una máquina con **Amazon Linux 2023** en AWS e instalar en ella **ONLYOFFICE Workspace Community**.

Una vez instalada, accederemos desde el navegador para:

* Crear documentos de texto, hojas de cálculo y presentaciones.
* Crear usuarios.
* Compartir documentos.
* Trabajar de forma colaborativa.

La instalación mediante **Docker** incluye los componentes necesarios.

### 2\. Requisitos de la máquina

La documentación de ONLYOFFICE establece estos requisitos mínimos:

|Recurso|Requisito mínimo|
|-|-|
|Procesador|4 núcleos|
|Memoria RAM|8 GB|
|Almacenamiento libre|40 GB|
|Memoria de intercambio|6 GB|
|Sistema|Linux de 64 bits, arquitectura **amd64/x86\_64**|

**Para esta práctica** usaremos una instancia **t3.large** (2 vCPU y 8 GB de RAM) con un disco de **30 GB**. Como está por debajo del mínimo de procesador y almacenamiento, el instalador se lanza con la opción `--skiphardwarecheck true` (Paso 8).

### 3\. Crear la instancia en AWS

En la consola de AWS:

1. Entra en **EC2**.
2. Selecciona **Instancias**.
3. Pulsa **Lanzar instancia**.
4. Introduce un nombre, por ejemplo: `PR2-ONLYOFFICE`
5. Selecciona la imagen (AMI) **Amazon Linux 2023** de **64 bits x86**. Evita las imágenes ARM para esta prueba, ya que la guía de ONLYOFFICE especifica arquitectura amd64.
6. Selecciona el tipo de instancia **t3.large**.
7. Selecciona el **par de claves** `vockey`.
8. Configura el almacenamiento con **30 GB**.
9. Comprueba que la instancia tenga asignada una **dirección IPv4 pública**.

Antes de lanzarla, revisa el precio de la instancia, el almacenamiento y la dirección pública, así como los créditos y límites de vuestra cuenta.

### 4\. Permitir las conexiones

En la configuración de red de la instancia, crea o selecciona un **grupo de seguridad** con estas reglas de entrada:

|Tipo|Puerto|Origen recomendado|Finalidad|
|-|-|-|-|
|SSH|22|**Mi IP**|Administrar la instancia desde tu equipo.|
|HTTP|80|IP pública del aula o de los equipos que harán la prueba|Abrir la aplicación desde el navegador.|
|HTTPS|443|IP pública del aula o de los equipos que harán la prueba|Utilizar la aplicación mediante conexión cifrada, una vez configurada.|

Si los alumnos se conectan desde redes diferentes, habrá que añadir sus direcciones autorizadas o acordar cómo se dará acceso.

> \\\[!IMPORTANT]
> Si vas a usar \\\*\\\*EC2 Instance Connect desde el navegador\\\*\\\*, el puerto SSH puede requerir una regla de origen distinta de «Mi IP», según el método de conexión. Si eliges conexión SSH con tu clave desde el equipo, la regla «Mi IP» es apropiada.

Lanza la instancia y espera a que aparezca como **En ejecución** y termine sus comprobaciones.

### 5\. Conectarse a Amazon Linux 2023

Una opción es intentar la conexión desde la propia consola:

1. En **EC2 → Instancias**, selecciona la máquina.
2. Pulsa **Conectar**.
3. Abre la pestaña **EC2 Instance Connect**.
4. Comprueba que el usuario sea: `ec2-user`
5. Pulsa **Conectar**.

Se abrirá una terminal en el navegador. Esta opción requiere que la imagen y la configuración de red admitan EC2 Instance Connect.

Si esta opción no funciona, se puede conectar mediante un cliente SSH y el par de claves `vockey`.

### 6\. Preparar el sistema

En la terminal de Amazon Linux 2023, ejecuta estos comandos en orden:

**Paso 1.** Actualiza todos los paquetes del sistema a su última versión estable.

```bash
sudo dnf update -y
```

**Paso 2.** Instala **Docker** (el motor de contenedores) y **Git** (necesario para clonar recursos).

```bash
sudo dnf install docker git -y
```

**Paso 3.** Arranca el servicio de Docker inmediatamente en el sistema.

```bash
sudo systemctl start docker
```

**Paso 4.** Configura Docker para que se encienda automáticamente si el servidor se reinicia.

```bash
sudo systemctl enable docker
```

**Paso 5.** Agrega tu usuario de AWS (`ec2-user`) al grupo **docker** para manejarlo sin usar `sudo`.

```bash
sudo usermod -aG docker $USER
```

**Paso 6.** Aplica el cambio de grupo en la sesión actual sin necesidad de cerrar la terminal.

```bash
newgrp docker
```

### 7\. Descargar e instalar ONLYOFFICE

**Paso 7.** Descarga el script instalador oficial de ONLYOFFICE.

```bash
curl -O https://download.onlyoffice.com/install/workspace-install.sh
```

**Paso 8.** Lanza la instalación en Docker omitiendo el servidor de correo, para poder usar la IP pública de la instancia, y sin la comprobación de hardware (la t3.large con 30 GB está por debajo del mínimo).

```bash
sudo bash workspace-install.sh -ims false --skiphardwarecheck true
```

Cuando el instalador pregunte:

```text
Select 'Y' to install ONLYOFFICE Workspace using Docker
```

escribe `Y` y pulsa **Intro**. Así seleccionas la instalación mediante **Docker**.

El instalador descargará y configurará los componentes necesarios. Espera a que finalice y revisa los mensajes que muestre antes de cerrar la terminal.

Si aparece algún error, guarda el mensaje completo: servirá para identificar en qué fase se ha detenido.

### 8\. Acceder a ONLYOFFICE

Cuando finalice la instalación:

1. Vuelve a **EC2 → Instancias**.
2. Selecciona la máquina.
3. Copia la **dirección IPv4 pública**.
4. Desde el navegador, accede a:

```text
   http://DIRECCION-IP-PUBLICA
   ```

Por ejemplo:

```text
   http://203.0.113.10
   ```

La dirección del ejemplo es ficticia: debes sustituirla por la de tu instancia.

5. Si aparece la pantalla inicial de ONLYOFFICE, continúa con la configuración del espacio de trabajo y de la cuenta administradora.

Si no carga, comprueba primero:

* Que la instancia siga en ejecución.
* Que utilizas su **IP pública actual**.
* Que el puerto **80** permita el acceso desde tu red.
* Que la instalación haya terminado sin errores.

> \\\[!WARNING]
> \\\*\\\*Para esta primera prueba,\\\*\\\* utiliza \\\*\\\*datos ficticios\\\*\\\*: con `http://` la conexión no está cifrada. Abrir el puerto 443 por sí solo no activa HTTPS; habrá que configurar un certificado y el servidor.

\---

## Parte 2 · Tareas en ONLYOFFICE

### 9\. Configuración y prueba de funcionamiento

Una vez dentro, comprueba estas funciones:

|Paso|Comprobación|
|-|-|
|1|Acceder con la cuenta administradora.|
|2|Crear un usuario de prueba o invitado, según las opciones disponibles.|
|3|Crear un documento de texto.|
|4|Crear una hoja de cálculo.|
|5|Crear una presentación.|
|6|Compartir uno de los archivos con otro usuario.|
|7|Abrir el documento con ambos usuarios y comprobar la edición colaborativa.|

Para probar dos usuarios desde el mismo ordenador, puedes utilizar una ventana normal del navegador y otra privada.

### 10\. Al terminar la prueba

> \\\[!CAUTION]
> Revisa en AWS los recursos creados y el consumo de la cuenta. \\\*\\\*Detener la instancia no elimina necesariamente todos los costes\\\*\\\*, ya que pueden permanecer recursos como el almacenamiento o la IP pública.

Si la prueba ha terminado y no necesitas conservarla, revisa qué recursos debes eliminar según la configuración de tu cuenta.



