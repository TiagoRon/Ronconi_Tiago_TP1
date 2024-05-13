def mochila_jedi(mochila, cantidad=0):
    if len(mochila) == 0:
        return cantidad, False  
    
    objeto = mochila.pop(0)
    cantidad += 1

    if len(mochila) > -1:
        print(objeto)

    if objeto == "sable de luz":
        return cantidad, True  
    else:
        return mochila_jedi(mochila, cantidad) 

mochila = []
cantidad, encontrado = mochila_jedi(mochila)

if encontrado:
    print(f"Se encontró el sable de luz después de sacar {cantidad-1} objetos.")
else:
    print("No se encontró el sable de luz en la mochila.")
