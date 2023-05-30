import random
import matplotlib.pyplot as plt

# Lista de equipos de la liga Colombiana
equipos = ["Junior", "Nacional", "Medellin", "Cali", "Millonarios", "Santa Fe", "America", "Pereira", "Envigado", "Once Caldas"]

# Listas para almacenar los equipos locales y visitantes, y los goles de cada equipo
equipos_local = []
equipos_visitante = []
goles_local = []
goles_visitante = []

# Generar datos aleatorios para cada partido
for i in range(len(equipos)):
    for j in range(len(equipos)):
        if i != j:
            equipos_local.append(equipos[i])
            equipos_visitante.append(equipos[j])
            goles_local.append(random.randint(0, 5))
            goles_visitante.append(random.randint(0, 5))

# 1. Calcular la cantidad de partidos por equipo
partidos_jugados = {}
for equipo in equipos:
    partidos_jugados[equipo] = equipos_local.count(equipo) + equipos_visitante.count(equipo)
print("Cantidad de partidos jugados por equipo:", partidos_jugados)

# 2. Calcular la cantidad de partidos ganados por equipo
partidos_ganados = {}
for equipo in equipos:
    partidos_ganados[equipo] = 0
for i in range(len(equipos_local)):
    if goles_local[i] > goles_visitante[i]:
        partidos_ganados[equipos_local[i]] += 1
    elif goles_visitante[i] > goles_local[i]:
        partidos_ganados[equipos_visitante[i]] += 1
print("Cantidad de partidos ganados por equipo:", partidos_ganados)

# 3. Calcular la cantidad de partidos perdidos por equipo
partidos_perdidos = {}
for equipo in equipos:
    partidos_perdidos[equipo] = 0
for i in range(len(equipos_local)):
    if goles_local[i] < goles_visitante[i]:
        partidos_perdidos[equipos_local[i]] += 1
    elif goles_visitante[i] < goles_local[i]:
        partidos_perdidos[equipos_visitante[i]] += 1
print("Cantidad de partidos perdidos por equipo:", partidos_perdidos)

# 4. Calcular la cantidad de partidos empatados por equipo
partidos_empatados = {}
for equipo in equipos:
    partidos_empatados[equipo] = 0
for i in range(len(equipos_local)):
    if goles_local[i] == goles_visitante[i]:
        partidos_empatados[equipos_local[i]] += 1
        partidos_empatados[equipos_visitante[i]] += 1
print("Cantidad de partidos empatados por equipo:", partidos_empatados)

# 5. Calcular la cantidad de goles de los equipos locales y graficar
goles_locales = {}
for equipo in equipos:
    goles_locales[equipo] = 0
for i in range(len(equipos_local)):
    goles_locales[equipos_local[i]] += goles_local[i]
plt.bar(goles_locales.keys(), goles_locales.values())
plt.title("Cantidad de goles de los equipos locales")
plt.show()

# 6. Calcular la cantidad de goles de los equipos visitantes y graficar
goles_visitantes = {}
for equipo in equipos:
    goles_visitantes[equipo] = 0
for i in range(len(equipos_local)):
    goles_visitantes[equipos_visitante[i]] += goles_visitante[i]
plt.bar(goles_visitantes.keys(), goles_visitantes.values())
plt.title("Cantidad de goles de los equipos visitantes")
plt.show()

# 7. Calcular la cantidad total de goles de todos los partidos
total_goles = sum(goles_local) + sum(goles_visitante)
print("Cantidad total de goles:", total_goles)

# 8. Calcular la cantidad de puntos por equipo
puntos = {}
for equipo in equipos:
    puntos[equipo] = partidos_ganados[equipo]*3 + partidos_empatados[equipo]
print("Cantidad de puntos por equipo:", puntos)

# 9. Calcular la cantidad de puntos por equipo
goles_totales = {}
for equipo in equipos:
    goles_totales[equipo] = [0, 0] # [goles de local, goles de visitante]
for i in range(len(equipos_local)):
    goles_totales[equipos_local[i]][0] += goles_local[i]
    goles_totales[equipos_visitante[i]][1] += goles_visitante[i]
for equipo in equipos:
    print(equipo, " - Goles locales:", goles_totales[equipo][0], ", Goles visitantes:", goles_totales[equipo][1])

# 10. Equipo que más goles realizo
max_goles = 0
equipo_max_goles = ""
for equipo in equipos:
    goles_equipo = goles_totales[equipo][0] + goles_totales[equipo][1]
    if goles_equipo > max_goles:
        max_goles = goles_equipo
        equipo_max_goles = equipo
print("Equipo con más goles realizados:", equipo_max_goles)

# 11. Equipo que menos goles realizo
min_goles_recibidos = float('inf')
equipo_min_goles_recibidos = ""
for equipo in equipos:
    goles_recibidos = goles_totales[equipo][1]
    if goles_recibidos < min_goles_recibidos:
        min_goles_recibidos = goles_recibidos
        equipo_min_goles_recibidos = equipo
print("Equipo que menos goles recibió:", equipo_min_goles_recibidos)

# 12. Leer por teclado el nombre del equipo y listar los partidos en los que ha participado y sus marcadores
equipo = input("Ingrese el nombre del equipo: ")
if equipo in equipos:
    print("Partidos de", equipo)
    for i in range(len(equipos_local)):
        if equipos_local[i] == equipo or equipos_visitante[i] == equipo:
            print(equipos_local[i], goles_local[i], "-", goles_visitante[i], equipos_visitante[i])
else:
    print("El equipo ingresado no se encuentra en la lista de equipos")

# 13. Armar la tabla de posiciones y crear una nueva lista con los puntos por equipo
tabla_posiciones = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
print("Tabla de posiciones")
for i in range(len(tabla_posiciones)):
    print(i+1, "-", tabla_posiciones[i][0], ":", tabla_posiciones[i][1], "puntos")

# 14. Imprimir la tabla de posiciones de mayor a menor por puntaje
tabla_posiciones = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
print("Tabla de posiciones")
for i in range(len(tabla_posiciones)):
    print(i+1, "-", tabla_posiciones[i][0], ":", tabla_posiciones[i][1], "puntos")

# 15. Articular todo en un menu
import random
import matplotlib.pyplot as plt

equipos = ["Atlético Nacional", "Millonarios", "Deportivo Cali", "Independiente Santa Fe",
           "América de Cali", "Junior", "Once Caldas", "Deportivo Pasto", "Envigado",
           "Atlético Bucaramanga"]

partidos_jugados = {}
partidos_ganados = {}
partidos_perdidos = {}
partidos_empatados = {}

goles_local = []
goles_visitante = []

for equipo in equipos:
    partidos_jugados[equipo] = 0
    partidos_ganados[equipo] = 0
    partidos_perdidos[equipo] = 0
    partidos_empatados[equipo] = 0

for i in range(len(equipos)):
    equipo_local = equipos[i]
    for j in range(len(equipos)):
        if i != j:
            equipo_visitante = equipos[j]
            partidos_jugados[equipo_local] += 1
            partidos_jugados[equipo_visitante] += 1
            goles_local.append(random.randint(0, 5))
            goles_visitante.append(random.randint(0, 5))
            if goles_local[-1] > goles_visitante[-1]:
                partidos_ganados[equipo_local] += 1
                partidos_perdidos[equipo_visitante] += 1
            elif goles_local[-1] < goles_visitante[-1]:
                partidos_perdidos[equipo_local] += 1
                partidos_ganados[equipo_visitante] += 1
            else:
                partidos_empatados[equipo_local] += 1
                partidos_empatados[equipo_visitante] += 1

while True:
    print("1. Calcular la cantidad de partidos por equipo")
    print("2. Calcular la cantidad de partidos ganados por equipo")
    print("3. Calcular la cantidad de partidos perdidos por equipo")
    print("4. Calcular la cantidad de partidos empatados por equipo")
    print("5. Calcular la cantidad de goles de los equipos locales y graficar")
    print("6. Calcular la cantidad de goles de los equipos visitantes y graficar")
    print("7. Calcular la cantidad total de goles de todos los partidos")
    print("8. Listado de los equipos con sus goles de local y de visitante")
    print("9. Equipo que más goles realizó")
    print("10. Equipo que menos goles recibió")
    print("11. Listar los partidos de un equipo")
    print("12. Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        for equipo in equipos:
            print(equipo, "-", partidos_jugados[equipo], "partidos jugados")
            
    elif opcion == 2:
        for equipo in equipos:
            print(equipo, "-", partidos_ganados[equipo], "partidos ganados")
            
    elif opcion == 3:
        for equipo in equipos:
            print(equipo, "-", partidos_perdidos[equipo], "partidos perdidos")
            
    elif opcion == 4:
        for equipo in equipos:
            print(equipo, "-", partidos_empatados[equipo], "partidos empatados")
            
    elif opcion == 5:
        goles_equipo_local = {}
        for equipo in equipos:
            goles_equipo_local[equipo] = 0
        for i in range(len(goles_local)):
            goles_equipo_local[equipos[i % len(equipos)]] += goles_local[i]
        print("Goles de los equipos locales")
        for equipo in equipos:
            print(equipo, "-", goles_equipo_local[equipo], "goles")
        plt.bar(goles_equipo_local.keys(), goles_equipo_local.values())
        plt.show()
        
    elif opcion == 6:
        goles_equipo_visitante = {}
        for equipo in equipos:
            goles_equipo_visitante[equipo] = 0
        for i in range(len(goles_visitante)):
            goles_equipo_visitante[equipos[i % len(equipos)]] += goles_visitante[i]
        print("Goles de los equipos visitantes")
        for equipo in equipos:
            print(equipo, "-", goles_equipo_visitante[equipo], "goles")
        plt.bar(goles_equipo_visitante.keys(), goles_equipo_visitante.values())
        plt.show()
        
    elif opcion == 7:
        total_goles = sum(goles_local) + sum(goles_visitante)
        print("Cantidad total de goles de todos los partidos:", total_goles)
        
    elif opcion == 8:
        for i in range(len(equipos)):
            print(equipos[i], "-", goles_local[i], "goles local /", goles_visitante[i], "goles visitante")
            
    elif opcion == 9:
        goles_equipo = {}
        for equipo in equipos:
            goles_equipo[equipo] = 0
        for i in range(len(goles_local)):
            goles_equipo[equipos[i % len(equipos)]] += goles_local[i] + goles_visitante[i]
        equipo_max_goles = max(goles_equipo, key=goles_equipo.get)
        print("El equipo que más goles realizó fue:", equipo_max_goles, "con", goles_equipo[equipo_max_goles], "goles")
        
    elif opcion == 10:
        goles_recibidos = {}
        for equipo in equipos:
            goles_recibidos[equipo] = 0
        for i in range(len(goles_local)):
            goles_recibidos[equipos[(i+1) % len(equipos)]] += goles_local[i] + goles_visitante[i]
        equipo_min_goles = min(goles_recibidos, key=goles_recibidos.get)
        print("El equipo que menos goles recibió fue:", equipo_min_goles, "con", goles_recibidos[equipo_min_goles], "goles recibidos")
        
    elif opcion == 11:
        equipo = input("Ingrese el nombre del equipo: ")
        if equipo not in equipos:
            print("El equipo ingresado no existe.")
        else:
            print("Partidos de", equipo)
            for i in range(len(equipos)):
                if equipos[i] == equipo:
                    print(equipo, "-", equipos[(i+1) % len(equipos)], goles_local[i], "-", goles_visitante[i])
                elif equipos[(i+1) % len(equipos)] == equipo:
                    print(equipos[(i+1) % len(equipos)], "-", equipo, goles_visitante[i], "-", goles_local[i])
                    
    elif opcion == 12:
        break
        
    else:
        print("Opción inválida. Intente de nuevo.")


