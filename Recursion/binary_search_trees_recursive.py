#Caso base: la lista de entrada está vacía
#  Devuelve "No Child" para representar la falta de nodo.
#Paso recursivo: la lista de entrada debe dividirse en dos mitades
#1.Encuentra el índice medio de la lista.
#2. Almacene el valor ubicado en el índice medio.
#3. Cree un nodo de árbol con una clave de "data" establecida en el valor.
#4. Asigne el "hijo izquierdo" del nodo del árbol a una llamada recursiva usando la mitad izquierda de la lista. 
#5. Asigne el "hijo derecho" del nodo del árbol a una llamada recursiva usando la mitad derecha de la lista 
#6. Devolver el nodo del árbol

# Define build_bst() below...
def build_bst(my_list):
  #caso base
  if len(my_list) == 0:
    return "No Child"
  #caso recursivo
  #declaramos middle_idx y le asignamos en el indice medio de my_list
  middle_idx = len(my_list)//2
  #declaramos middle_value y lo establecemos en el valor de my_list ubicado en middle_idx
  middle_value = my_list[middle_idx]
  print("Middle index: {0}".format(middle_idx))
  print("Middle value: {0}".format(middle_value))
  #variable tree_node que apunta a un diccionario de python con clave "data" que apunta a "middle_value", tree_node representa el árbol que se crea en esta llamada de función. Queremos que se cree un tree_node para cada elemento de la lista, así que repetiremos este proceso en los subárboles izquierdo y derecho usando la mitad apropiada de la lista de entrada.
  tree_node ={"data": middle_value}
  #Configure la clave de "left_child" en tree_node para que sea una llamada recursiva a build_bst() con la mitad izquierda de la lista sin incluir el valor medio(middle value) como argumento. 
  tree_node["left_child"] = build_bst(my_list[:middle_idx])
  #Configure la clave de "right_child" en tree_node para que sea una llamada recursiva a build_bst() con la mitad derecha de la lista sin incluir el valor medio como argumento.
  tree_node["right_child"] = build_bst(my_list[middle_idx +1:])
  return tree_node






# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
