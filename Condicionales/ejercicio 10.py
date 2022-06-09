"""
La pizzería bella napoli ofrece pizzas vegetarianas o no vegetarianas a sus clientes.
los ingredientes para cada tipo de pizza aparecen a continuación.

ingredientes vegetarianos: pimiento y tofu.
ingredientes no vegetarianos: peperoni, jamón y salmón.

escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
funcion de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. solo se puede eligir un ingrediente además de la mozzarella y el tomate que están
en todas las pizzas. Al final se debe mostrar por pantalla si la pizza eligida es
vegetariana o no y todos los ingredientes que lleva.
"""
vegetariana = input("quieres una pizza vegetariana? (S) o (N) ")
vegetariana = vegetariana.upper()
if vegetariana == "S":
    ingredientes = input("Cuales ingredientes quieres eligir? (pimiento) o (tofu)")
    print(f"pizza vegetariana con {ingredientes}")
elif vegetariana == "N":
    ingredientes = input("Cuales ingredientes quieres eligir? (peperoni), (Jamón) o (salmón)")
    print(f"pizza no vegetariana con {ingredientes}")
else:
    print("no entendí el zabor.")
