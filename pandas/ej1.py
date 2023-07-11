import pandas as pd

inicio = int(input("Cual es el año de inicio? \n"))
fin = int(input("Cual es el año del fin? \n"))
ventas = {}

for año in range(inicio,fin+1):
    venta_año = int(input(f"Cuál fue la venta del año {año}? \n"))
    ventas[año] = venta_año

ventas_serie = pd.Series(ventas)
print(ventas_serie)
print("---------------")
print(ventas_serie * 0.9)