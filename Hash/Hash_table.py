class HashMap:
  def __init__(self,array_size):
    self.array_size = array_size
    #variable de instancia llamada .array, que es una lista de tamaño array_size. Haga que cada elemento de .array sea igual a Ninguno
    self.array = [None for i in range(self.array_size)]
    #funcion Hash

  def hash(self,key):
    key_bytes = key.encode()
    #Convertimos el objeto de bytes en un código hash llamando a sum() en key_bytes
    hash_code = sum(key_bytes)
    return hash_code

    #Crear la función de compresión int to indices
  def compressor(self,hash_code):
    return hash_code % self.array_size

    #Definición del colocador: Necesitamos juntar todos los otros pasos que hemos tomado: conectar la clave en la función hash, conectar el código hash en la función de compresión, usar el índice de matriz para encontrar el lugar en la matriz y finalmente establecer el valor de la matriz al valor que queremos.
  def assign(self,key,value):
    #Guarde el value en la matriz del mapa en el índice determinado al ingresar la key en el método .hash() y el código hash en el método .compressor().
    array_index = self.compressor(self.hash(key))
    self.array[array_index] = value


  #Definición del getter
  def retrieve(self,key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]













# #creando una instancia
# hash_map = HashMap(20)
# hash_map.assign("gneiss","metamorphic")
# print(hash_map.retrieve("gneiss"))
