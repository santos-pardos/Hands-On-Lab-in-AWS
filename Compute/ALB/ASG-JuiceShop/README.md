# LAB - Despliegue de una aplicación con ASG y ALB

En este laboratorio crearemos una web con contenedores con un balanceador de carga y un grupo de autoescalado.

## Creación del Launch Template

* Desde EC2 lanza un Launch Template y dale nombre

![](images/01.png)

* Elige una AMI Linux 2023

![](images/02.png)

* Elige un tipo de instancia t2.micro que es capa gratuita

![](images/03.png)

* Elige SGALB para las máquinas que lance el Launch Template, no elegimos red, lo haremos en las opciones del ASG

![](images/04.png)

* En opciones avanzadas edita el user data y agrega el siguiente código.

```bash
#!/bin/bash 
sudo dnf update -y 
sudo dnf install -y docker 
service docker start 
systemctl enable docker.service
docker pull santospardos/upc:juiceshop
docker run -d -p 80:3000 santospardos/upc:juiceshop
```


## Crea el balanceador ASG

* Desde el menú EC2 en la parte inferior elegimos ASG y creamos uno

![](images/05.png)


* Le damos nombre y elegimos la Launch Template que hemos creado antes

![](images/06.png)


* Elegimos el VPC y las redes en donde se podrán lanzar EC2, en este caso todas AZ.

![](images/07.png)


* Elegimos crear un ALB nuevo y que tenga salida a internet (internet-facing)

![](images/08.png)


* Eligimos crear un Target Group, lo renombrará utomáticamente, y meterá todas las instancias que cree el ASG en este TG

![](images/09.png)


* Configuramos las opciones de tamaño de grupo

![](images/10.png)


* Elegimos una politica de autoescalado. En este caso promedio de CPU y lo dejamos en 50%

![](images/11.png)


* No añadimos notificación por SNS

![](images/12.png)


* Agregamos una etiqueta para facturación

![](images/13.png)


* Revisamos la configuraicón y le damos crear el ASG

![](images/14.png)


* Comprobamos la creación del ASG

![](images/14.png)


* Revisamos las EC2 creadas

![](images/14.png)


## RETO

Instalar la aplicación stress en ambas EC2, lanzamos 10 procesos de cpu y comprobamos que cuando lleguen a 50% ambas máquinas se lanza una tercera EC2 al aplicarse la politica de autoescalado