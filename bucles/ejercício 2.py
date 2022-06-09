"""
escribir un programa que pregunte al usuario su edad y muestre por
pantalla todos los años que ha cumplido (desde 1 hasta su edad.
"""

edad_actual = int(input("informe su edad actual. "))
i = 1
#while i <= edad_actual:
for i in range(edad_actual):
    print(f"sua idade já foi {i} e agora é {edad_actual}")
    i+=1