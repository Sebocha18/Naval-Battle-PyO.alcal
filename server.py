import socket
 
# creamos el socket
serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# usamos esta funcion para mantener en eschucha el puerto que queramos este caso 8000
serversocket.bind(('localhost', 8000))
# mantenemos en escucha el servidor
serversocket.listen(1)
# aceptamos la conexion
clientsocket, clientaddress = serversocket.accept()
print 'Conexion desde: ', clientaddress # escribimos la ip del cliente
# mientras estamos conectados hace lo que este dentro del bucle
while 1:
        data = clientsocket.recv(1024) # recibimos datos del cliente
        print 'cliente %s' % data # ponemos en pantalla lo que nos a dicho el cliente
        newdata = raw_input('>') # escribimos lo que queramos enviar
        clientsocket.send(newdata) # enviamos lo que hemos escrito
        if not newdata: break # si no hay datos no lo enviamos
clientsocket.close() # cerramos el socket