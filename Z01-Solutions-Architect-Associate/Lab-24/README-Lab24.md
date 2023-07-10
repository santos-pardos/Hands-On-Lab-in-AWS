# AWS Solutions Architect Associate - Laboratorio 24

<br>

### Objetivo: 
* Entendimiento de OU (Organizational Unit) en AWS Organizations
* Entendimiento de SCPs (Service Control Policies) en AWS Organizations

### Tópico:
* Management & Governance

### Dependencias:
* Implementación del Laboratorio 22

<br>

---

### A - Entendimiento de OU (Organizational Unit) en AWS Organizations

<br>

1. Ingresamos a la cuenta AWS desde donde administramos AWS Organizations. Seleccionamos la carpeta Root y luego damos clic en la opción "Actions". Seguido, damos clic en la opción Create New (Organizational Unit). Ingresamos el nombre "PROD" a nuestro "Organizational unit name" y damos clic en la opción "Create Organizational Unit". Validamos la creación de nuestra OU.

<br>

<img src="images/Lab24_01.jpg">

<br>

<img src="images/Lab24_02.jpg">

<br>

<img src="images/Lab24_03.jpg">

<br>

2. Seleccionamos nuestra cuenta "awstraining-01", damos clic en "Actions", luego en "Move (AWS Account)". Seleccionamos como destino "PROD" y damos clic en "Move AWS Account". Accedemos al OU "PROD" y validamos que nuestra cuenta forma parte del OU "PROD" 

<br>

<img src="images/Lab24_04.jpg">

<br>

3. Ingresamos a la sección de "Policies", luego damos clic en la opción "Service Control policies". Seguidamente damos clic en el botón "Enable service control policies". Habilito los "Service Control Policies", damos clic en el botón "Create Policy". 

<img src="images/Lab24_05.jpg">

<br>

<img src="images/Lab24_06.jpg">

<br>

<img src="images/Lab24_07.jpg">

<br>

<img src="images/Lab24_08.jpg">

<br>

4. Ingresamos los siguientes valores. Luego, dar clic en el botón "Create Policy"

    * Policy name: Virginia
    * Policy: Copiar el contenido del archivo "1_lab24_awsorganizations_scp" almacenado en la ruta Lab-24/code de este repositorio y pegarlo en la sección "Statement". Analizar la política.

<br>

<img src="images/Lab24_09.jpg">

<br>

<img src="images/Lab24_10.jpg">

<br>

<img src="images/Lab24_11.jpg">

<br>

5. Seleccionamos la SCP "Virginia", damos clic en el botón "Actions" y seleccionamos la opción "Attach Policy". Luego, desde la estructura en forma de árbol de AWS Organizations, seleccionamos nuestra cuenta AWS generada en pasos anterior ("awstraining-01") y damos clic en "Attach Policy". Si accedemos al detalle de la nueva cuenta AWS, validaremos que esta cuenta tiene asociada varias SCPs (FullAWSAccess), una de ellas será el SCP "Virginia"

<br>

<img src="images/Lab24_12.jpg">

<br>

<img src="images/Lab24_13.jpg">

<br>

<img src="images/Lab24_14.jpg">

<br>

6. Accedemos a la cuenta "awstraining-01" e ingresamos al servicio EC2 en la región de N.Virginia. Asimismo, accedemos a la región Ohio. Validaremos que no se cuenta con permisos en la región de Ohio. La política SCP "Virginia" asociada, a nivel de AWS Organizations, a la cuenta "awstraining-01" sólo permite el uso de servicios en la región N. Virginia, todo lo demás se negará (no se incluye los servicios de naturaleza Global).

<br>

<img src="images/Lab24_15.jpg">

<br>

<img src="images/Lab24_16.jpg">

<br>

---

### Eliminación de recursos

```bash
#Eliminar SCP
#Deshabilitar "Policies - Service control policies"
```
