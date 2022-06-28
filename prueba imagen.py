import urllib

url = 'https://cdn.pixabay.com/photo/2013/07/12/17/15/boat-151887_960_720.png'

imagen = open("image_descargada.jpg", 'wb')
imagen.write(urllib.urlopen(url).read())
imagen.close()