28 Herencia de modelos
29 Herencia de vistas
30 Herencia de métodos
31 Herencia por delegacion

- Crear nuevo módulo sale_helpdesk_xxx
  - añadir un listado de tickets en el pedido de venta.
  - añádir el campo etiqueta de helpdesk en el producto y poner un botón que cree ticket desde pedidos con las etiquetas de los productos del pedido.
  - hacer que al cancelar un pedido se cancelen todos los tickets asociados. (Volver a poner el campo state como un selection)

- Crear un nuevo módulo crm_helpdesk_xxx
  Será otra alternativa al primero que hemos hecho, utilizaremos toda la funcionalidad de los leads.

  Crearemos un nuevo modelo crm.lead.ticket con herencia por delegación utilizando como base el lead y añadiendo los campos acciones correctivas y preventivas.


34 Uso de context

Añadir un campo contacto en el ticket, hacer que si creo un contacto desde el ticket se cree como tipo individual y el comercial sea el usuario asignado al ticket.

36 Mixin

Añadir mail.thread y mail.activity.mixin al ticket, en modelo y vista.

38 Test

Hacer un test para comprobar que si intento poner dedicated_time negativo me lanza una excepción.

35 Informes

- Crear un informe de impresión para el ticket. Que muestre nombre, fecha, cliente y listado de acciones, similar a pedido de venta.
- Crear una tarjeta identificativa para el partner con la foto, crear paperformat de tarjeta y ver como el external layout añade la foto.
- En el módulo sale_helpdesk_xxx modificar la impresión del pedido de venta para añádir un listado de los tickets relacionados.

