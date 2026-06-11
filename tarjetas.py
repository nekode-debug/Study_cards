materia_uno = 'Teoría electromagnética'
materia_dos = 'Procesamiento de señales'
materia_tres = 'Matemáticas especiales II'
tarjetas_materia_uno = [
    ('¿Qué es una carga eléctrica?', 'Es una propiedad física de la materia responsable de las interacciones eléctricas. Puede ser positiva o negativa y se mide en coulombs (C).'),
    ('¿Qué es un campo eléctrico?', 'Es una magnitud vectorial que describe la fuerza que experimentaría una carga positiva de prueba en cada punto del espacio.'),
    ('¿Qué es el potencial eléctrico?', 'La "altura eléctrica". Las cargas positivas tienden a moverse desde potencial alto hacia potencial bajo, como una pelota rueda cuesta abajo.'),
]
tarjetas_materia_dos = [
    ('¿Qué es una señal?', 'Una señal es información representada como una función del tiempo.'),
    ('¿Qué es un sistema?', 'Una máquina matemática que recibe una señal y produce otra.'),
    ('¿Qué revela la Transformada de Fourier?', 'Las frecuencias ocultas dentro de una señal.'),
]
tarjetas_materia_tres = [
    ('¿Qué representa un número complejo?', 'Magnitud y rotación al mismo tiempo.'),
    ('¿Qué es el espectro de una señal?', 'El listado de las frecuencias que la componen.'),
    ('¿Qué significa que una señal tenga energía en altas frecuencias?', 'Cambia rápidamente.'),
]

print("===" + materia_uno + "===")
for pregunta, respuesta in tarjetas_materia_uno:
    print("- " + pregunta + " -> " + respuesta)

print("\n===" + materia_dos + "===")
for pregunta, respuesta in tarjetas_materia_dos:
    print("- " + pregunta + " -> " + respuesta)

print("\n===" + materia_tres + "===")
for pregunta, respuesta in tarjetas_materia_tres:
    print("- " + pregunta + " -> " + respuesta)

print("\n===" + materia_uno + "=== (" + str(len(tarjetas_materia_uno)) + " tarjetas)")
print("\n===" + materia_dos + "=== (" + str(len(tarjetas_materia_dos)) + " tarjetas)")
print("\n===" + materia_tres + "=== (" + str(len(tarjetas_materia_tres)) + " tarjetas)")

total = len(tarjetas_materia_uno) + len(tarjetas_materia_dos) + len(tarjetas_materia_tres)
print("\nHay un total de tarjetas de: " + str(total))
