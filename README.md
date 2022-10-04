# Naval-Battle-PyO.alcal
Proyecto empezado el 7/6/22 por Pianetti Sebastian y Oviedo Fernando


MODULOS
	Tkinter
	Socket
	Json
	Functools/Partial
	PyoServerserver
	PyoServerCliente


PROYECTOS
	Creación de Servidores
	
	Conexión de Servidor y Cliente

	Imagen en Menú

	Creación de Tableros
	
	Colocación de Barcos


FUNCIONES
	transformar
		El objetivo de esta función es trasladar todas las listas de campo y cambiar su formato a texto para cuando se recibe este formatearlo en lista.

	pulsar
		Esta función pulsa un boton del tablero y muestra su ubicación/coordenadas.
	
	limpiar_tablero
		Como dice el nombre cuando se coloca un barco este modulo limpia las partes que no se tendrian que pintar.

	cambiar_sentido
		Si el usuario quiere cambiar el sentido de los barcos con este modulo.

	apretar
		Analiza el espacio del tablero y segun las medidas pinta en vertical y/o horizontal en un rango de 5x1 hasta 1x1 haciendo asi la forma de los barcos.	

	on_enter
		Esta funciòn es para que cuando el cursor este dentro del tablero, nos deje pintar los barcos.

	on_leave
		Esta seria lo contrario de on_enter, que cuando el cursor este fuera del tablero, no nos deje pintar.
