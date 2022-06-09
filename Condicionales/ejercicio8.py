"""
en una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienza en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras
mencionadas. A continuación se muestra una tabla con los niveles correspondientes a
cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400 multiplicada
por la puntuación del nivel
"""

evaluacion = input("Cual es la evaluacion final del funcionario? ")
evaluacion = float(evaluacion)
calculo = evaluacion * 2400
if evaluacion == 0.0:
    print(f"inaceptable, su bônus es igual a {calculo}")
elif evaluacion == 0.4:
    print(f"Aceptable, su bônus es igual a {calculo}")
elif evaluacion >= 0.6:
    print(f"Meritorio, su bônus es igual a {calculo}")