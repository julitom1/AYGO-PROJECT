# Diseño de un sistema de clasificación NLP dirigido por eventos para la asignación de trabajo por áreas

## Arquitectura Propuesta

![arquitectura-aygo-propuesta](https://github.com/user-attachments/assets/c9ed83c5-80af-4f5e-acb0-211fc6bd97f3)

## Flujo del Prototipo
En el presente prototipo, ilustrado en la figura, los usuarios interactúan con la **aplicación** a través de Amazon API Gateway, el cual redirige las solicitudes hacia una cola SQS de ingesta *ingestion-sqs*. Desde esta cola, los mensajes son procesados por una función Lambda que determina el área correspondiente y gestiona su envío vía correo electrónico.

![arquitectura-aygo-prototipo-v2](https://github.com/user-attachments/assets/f7c064d6-0c64-4e09-8432-cbdc253b79b5)

**Sección de Inferencia y Asignación**

El flujo de la aplicación en la **etapa de inferencia** está conectado a una función Lambda que actúa como *endpoint de inferencia*, encargada de clasificar los mensajes recibidos. Tras la clasificación, los mensajes se envían a la **sección de asignación**, donde son procesados y dirigidos a la cola SQS del área correspondiente.

Una segunda función Lambda toma estos mensajes y los utiliza para generar notificaciones, las cuales se publican en un tema de SNS *notification-topic*. Esto habilita la notificación automática de las áreas correspondientes a través de correo electrónico.

Este esquema aprovecha al máximo los servicios de AWS para garantizar un flujo eficiente, escalable y automatizado.


### Video Demostrativo

A continuación se realiza un PoC para visualizar la sección de aplicación, inferencia y asignación de la solución propuesta.

https://youtu.be/M_RX_Jdc0gg
