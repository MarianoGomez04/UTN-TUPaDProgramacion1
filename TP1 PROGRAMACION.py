#Ejercicio 1— “Caja del Kiosco”
#Objetivo: Simular una compra con validaciones y cálculo de total.
#Requisitos
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
#2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#.isdigit() en while).
#3. Por cada producto (usar for):
#o Pedir precio (entero, validar .isdigit()).
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#cualquier mayuscula/minuscula).
#o Si tiene descuento: aplicar 10% al precio de ese producto.
#4. Al final mostrar:
#o Total sin descuentos
#o Total con descuentos
#o Ahorro total
#o Promedio por producto (usar float y formatear con :.2f, ejem:
#x = 3.14159
#print(f"{x:.2f}"))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Ejercicio 1 - Caja del Kiosco

# 1. Pedir nombre del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")

while not nombre_cliente.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre_cliente = input("Ingrese nuevamente el nombre: ")


# 2. Pedir cantidad de productos
cantidad_productos = input("Ingrese la cantidad de productos: ")

while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Error: ingrese un número entero positivo.")
    cantidad_productos = input("Ingrese nuevamente la cantidad: ")

cantidad_productos = int(cantidad_productos)


# Variables para acumular los totales
total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0


# 3. Pedir información de cada producto
for i in range(cantidad_productos):

    print(f"\nProducto {i + 1}")

    # Pedir precio
    precio = input("Ingrese el precio: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input("Ingrese nuevamente el precio: ")

    precio = int(precio)

    # Preguntar si tiene descuento
    descuento = input("¿Tiene descuento? (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    # Acumular total sin descuentos
    total_sin_descuentos += precio

    # Aplicar descuento
    if descuento == "s":
        monto_descuento = precio * 10 / 100
        precio_final = precio - monto_descuento

        ahorro_total += monto_descuento
    else:
        precio_final = precio

    # Acumular total con descuentos
    total_con_descuentos += precio_final


# 4. Mostrar resultados

promedio = float(total_con_descuentos / cantidad_productos)

print("\n----- RESUMEN DE LA COMPRA -----")
print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos}")
print(f"Ahorro total: ${ahorro_total}")
print(f"Promedio por producto: ${promedio:.2f}")
        
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Objetivo: Login con intentos + menú de acciones con validación estricta.
#Requisitos
#1. Definir credenciales fijas en el código:
#o usuario correcto: "alumno"
#o clave correcta: "python123"
#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#1. Ver estado de inscripción (mostrar “Inscripto”)
#2. Cambiar clave (pedir nueva clave y confirmación; deben
#coincidir)
#3. Mostrar mensaje motivacional (1 frase)
#4. Salir
#5. Validación del menú:
#o Debe ser número (.isdigit())
#o Debe estar entre 1 y 4
#Cambio de clave
#• La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
#rechazar.
#Salida esperada
#Intento 1/3 - Usuario: alumno
#Clave: xxx
#Error: credenciales inválidas.
#Intento 2/3 - Usuario: alumno
#Clave: python123
#Acceso concedido.
#1) Estado 2) Cambiar clave 3) Mensaje 4) Salir
#Opción: a
#Error: ingrese un número válido.
#Opción: 5
#Error: opción fuera de rango.
#3
#Opción: 2
#Nueva clave: 123
#Error: mínimo 6 caracteres.



# Ejercicio 2 - Acceso al Campus y Menú Seguro

# 1. Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

# Contador de intentos
intentos = 0


# 2. Máximo 3 intentos
while intentos < 3:

    print(f"\nIntento {intentos + 1}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    # Verificar credenciales
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1


# 3. Si falló 3 veces, bloquear cuenta
if intentos == 3:

    print("Cuenta bloqueada.")

else:

    # 4. Menú repetitivo
    while True:

        print("\n1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        # 5. Validar que sea un número
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        # Validar que esté entre 1 y 4
        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")

            opcion = int(opcion)


        # Opción 1
        if opcion == 1:
            print("Inscripto.")


        # Opción 2
        elif opcion == 2:

            nueva_clave = input("Nueva clave: ")

            # Validar mínimo 6 caracteres
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")

            else:

                confirmacion = input("Confirmar nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")

                else:
                    print("Error: las claves no coinciden.")


        # Opción 3
        elif opcion == 3:
            print("¡Seguí adelante, cada día estás más cerca de tu objetivo!")


        # Opción 4
        elif opcion == 4:
            print("Usted salió del campus.")
            break

#////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercicio 3 (Alta) — “Agenda de Turnos con
#Nombres (sin listas)”
#Contexto
#Hay 2 días de atención: Lunes y Martes.
#Cada día tiene cupos fijos:
#• Lunes: 4 turnos
#• Martes: 3 turnos
#Reglas
#1. Pedir nombre del operador (solo letras).
#2. Menú repetitivo hasta salir:
#1. Reservar turno
#2. Cancelar turno (por nombre)
#3. Ver agenda del día
#4. Ver resumen general
#5. Cerrar sistema
#3. Reservar:
#o Elegir día (1=Lunes, 2=Martes).
#o Pedir nombre del paciente (solo letras).
#o Verificar que no esté repetido en ese día (comparando con las variables
#ya cargadas).
#o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#4. Cancelar:
#o Elegir día.
#o Pedir nombre del paciente (solo letras).
#o Si existe, cancelar y dejar el espacio vacío ("").
#5. Ver agenda del día:
#4
#Programación 1
#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
#o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
#está vacío.
#6. Resumen general:
#o Turnos ocupados y disponibles por día.
#o Día con más turnos (o empate).
#Restricciones
#• ❌ No listas, no diccionarios, no sets, no tuplas.
#• ✅ Se permite usar "" como “vacío”.
#• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).



# ==========================================
# AGENDA DE TURNOS - SIN LISTAS
# ==========================================


print("=== AGENDA DE TURNOS ===")


# 1. Pedir nombre del operador
operador = input("Ingrese nombre del operador: ")


while not operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    operador = input("Ingrese nombre del operador: ")




# ==========================================
# VARIABLES DE LOS TURNOS
# ==========================================


# Lunes tiene 4 turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""


# Martes tiene 3 turnos
martes1 = ""
martes2 = ""
martes3 = ""




# ==========================================
# MENÚ PRINCIPAL
# ==========================================


opcion = ""


while opcion != "5":


    print("\n==============================")
    print("        MENÚ PRINCIPAL")
    print("==============================")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    print("==============================")


    opcion = input("Seleccione una opción: ")


    while not opcion.isdigit():
        print("Error: debe ingresar un número.")
        opcion = input("Seleccione una opción: ")


    # ======================================
    # OPCIÓN 1 - RESERVAR TURNO
    # ======================================


    if opcion == "1":


        print("\n--- RESERVAR TURNO ---")
        print("1. Lunes")
        print("2. Martes")


        dia = input("Seleccione el día: ")


        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: seleccione 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione el día: ")


        paciente = input("Ingrese nombre del paciente: ")


        while not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")


        # -------------------------------
        # RESERVAR LUNES
        # -------------------------------


        if dia == "1":


            # Verificar si el paciente ya existe
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente:


                print("Ese paciente ya tiene un turno el lunes.")


            # Buscar primer espacio libre
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente.")
                print("Turno 1 - Lunes")


            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente.")
                print("Turno 2 - Lunes")


            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente.")
                print("Turno 3 - Lunes")


            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente.")
                print("Turno 4 - Lunes")


            else:
                print("No hay turnos disponibles para el lunes.")


        # -------------------------------
        # RESERVAR MARTES
        # -------------------------------


        else:


            # Verificar si el paciente ya existe
            if paciente == martes1 or paciente == martes2 or paciente == martes3:


                print("Ese paciente ya tiene un turno el martes.")


            # Buscar primer espacio libre
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente.")
                print("Turno 1 - Martes")


            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente.")
                print("Turno 2 - Martes")


            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente.")
                print("Turno 3 - Martes")


            else:
                print("No hay turnos disponibles para el martes.")




    # ======================================
    # OPCIÓN 2 - CANCELAR TURNO
    # ======================================


    elif opcion == "2":


        print("\n--- CANCELAR TURNO ---")
        print("1. Lunes")
        print("2. Martes")


        dia = input("Seleccione el día: ")


        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: seleccione 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione el día: ")


        paciente = input("Ingrese nombre del paciente: ")


        while not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")


        encontrado = False


        # -------------------------------
        # CANCELAR LUNES
        # -------------------------------


        if dia == "1":


            if paciente == lunes1:
                lunes1 = ""
                encontrado = True


            elif paciente == lunes2:
                lunes2 = ""
                encontrado = True


            elif paciente == lunes3:
                lunes3 = ""
                encontrado = True


            elif paciente == lunes4:
                lunes4 = ""
                encontrado = True


        # -------------------------------
        # CANCELAR MARTES
        # -------------------------------


        else:


            if paciente == martes1:
                martes1 = ""
                encontrado = True


            elif paciente == martes2:
                martes2 = ""
                encontrado = True


            elif paciente == martes3:
                martes3 = ""
                encontrado = True


        if encontrado:
            print("Turno cancelado correctamente.")
        else:
            print("No se encontró un turno para ese paciente.")




    # ======================================
    # OPCIÓN 3 - VER AGENDA
    # ======================================


    elif opcion == "3":


        print("\n--- AGENDA DEL DÍA ---")
        print("1. Lunes")
        print("2. Martes")


        dia = input("Seleccione el día: ")


        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: seleccione 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione el día: ")


        print()


        if dia == "1":


            print("=== AGENDA DEL LUNES ===")


            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)


            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)


            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)


            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)


        else:


            print("=== AGENDA DEL MARTES ===")


            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)


            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)


            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)




    # ======================================
    # OPCIÓN 4 - RESUMEN GENERAL
    # ======================================


    elif opcion == "4":


        print("\n--- RESUMEN GENERAL ---")


        # Contar turnos ocupados del lunes
        ocupados_lunes = 0


        if lunes1 != "":
            ocupados_lunes += 1


        if lunes2 != "":
            ocupados_lunes += 1


        if lunes3 != "":
            ocupados_lunes += 1


        if lunes4 != "":
            ocupados_lunes += 1


        disponibles_lunes = 4 - ocupados_lunes




        # Contar turnos ocupados del martes
        ocupados_martes = 0


        if martes1 != "":
            ocupados_martes += 1


        if martes2 != "":
            ocupados_martes += 1


        if martes3 != "":
            ocupados_martes += 1


        disponibles_martes = 3 - ocupados_martes




        # Mostrar resumen
        print("\nLUNES")
        print("Ocupados:", ocupados_lunes)
        print("Disponibles:", disponibles_lunes)


        print("\nMARTES")
        print("Ocupados:", ocupados_martes)
        print("Disponibles:", disponibles_martes)




        # Determinar qué día tiene más turnos
        if ocupados_lunes > ocupados_martes:


            print("\nEl día con más turnos es Lunes.")


        elif ocupados_martes > ocupados_lunes:


            print("\nEl día con más turnos es Martes.")


        else:


            print("\nHay empate entre Lunes y Martes.")




    # ======================================
    # OPCIÓN 5 - CERRAR SISTEMA
    # ======================================


    elif opcion == "5":


        print("\nSistema cerrado.")
        print("Operador:", operador)




    # ======================================
    # OPCIÓN INCORRECTA
    # ======================================


    else:


        print("Opción incorrecta. Seleccione una opción del 1 al 5.")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////

#Ejercicio 4 — “Escape Room: La Bóveda”
#Historia
#Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
#limitados.
#Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
#Variables iniciales (NO se piden por teclado)
#• energia = 100
#• tiempo = 12
#• cerraduras_abiertas = 0
#• alarma = False
#• codigo_parcial = ""
#Validaciones obligatorias
#• No usar try/except.
#• Pedir nombre del agente y validar con .isalpha() en un while.
#• Validar opciones del menú y cualquier número pedido con .isdigit() en un
#while.
#• El juego debe funcionar con estructuras secuenciales, condicionales y
#repetitivas (puede usar funciones propias del lenguaje como .lower(), len(),
#formateo, etc.).
#Regla anti-spam (muy importante)
#Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al
#iniciar:
#✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#• se cobra el costo normal (-20 energía, -2 tiempo),
#• NO abre cerradura, y
#• se activa la alarma automáticamente (alarma = True) porque “la cerradura se
#trabó”.
#Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
#Menú de acciones (se repite mientras el juego siga)
#El juego continúa mientras:
#• energia > 0, tiempo > 0, cerraduras_abiertas < 3
#• y no esté bloqueado por alarma.
#En cada turno mostrar el estado y el siguiente menú:
#1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#o Si la energía está por debajo de 40, hay “riesgo de alarma”:
#▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#o Si no hay alarma, abre 1 cerradura.
#o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y
#no abre.
#2. Hackear panel (costo: -10 energía, -3 tiempo)
#o Debe usar un for de 4 pasos mostrando progreso.
#o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
#o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
#todavía faltan.
#3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
#energía extra)
#Regla de bloqueo por alarma
#• Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
#se bloquea y se pierde.
#Condiciones de fin
#• Si cerraduras_abiertas == 3 → VICTORIA
#• Si energia <= 0 o tiempo <= 0 → DERROTA
#• Si se bloquea por alarma → DERROTA (bloqueo)


# EJERCICIO 4 - ESCAPE ROOM: LA BÓVEDA

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0


# Validación del nombre
nombre = input("Ingrese el nombre del agente: ").strip()

while not nombre.isalpha():
    print("Nombre inválido. Ingrese solamente letras.")
    nombre = input("Ingrese el nombre del agente: ").strip()

print(f"\nBienvenido, agente {nombre}.")


# Juego principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:

    print("\n-----------------------------")
    print(f"Agente: {nombre}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print("-----------------------------")

    # Validación del menú
    opcion = input(
        "1. Forzar cerradura\n"
        "2. Hackear panel\n"
        "3. Descansar\n"
        "Seleccione una opción: "
    ).strip()

    while not opcion.isdigit() or 2 < 1 or int(opcion) > 3:
        print("Opción inválida.")
        opcion = input("Seleccione una opción del 1 al 3: ").strip()

    opcion = int(opcion)


    # OPCIÓN 1: FORZAR CERRADURA
    if opcion == 1:

        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        # Regla anti-spam
        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabó.")
            print("¡ALARMA ACTIVADA!")

        # Riesgo de alarma por baja energía
        elif energia < 40:

            riesgo = input(
                "La energía está por debajo de 40."
                " Ingrese un número del 1 al 3: "
            ).strip()

            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                print("Número inválido.")
                riesgo = input("Ingrese un número del 1 al 3: ").strip()

            riesgo = int(riesgo)

            if riesgo == 3:
                alarma = True
                print("¡ALARMA ACTIVADA!")
            else:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

        else:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta!")


    # OPCIÓN 2: HACKEAR PANEL
    elif opcion == 2:

        energia -= 10
        tiempo -= 3

        # Corta la racha de forzar
        forzar_seguidas = 0

        print("\nIniciando hackeo...")

        for paso in range(4):
            codigo_parcial += "A"
            print(f"Paso {paso + 1}: progreso...")

        print(f"Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Se abrió una cerradura.")


    # OPCIÓN 3: DESCANSAR
    elif opcion == 3:

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        # Corta la racha de forzar
        forzar_seguidas = 0

        if alarma == True:
            energia -= 10
            print("La alarma está activa.")
            print("Perdiste 10 de energía extra.")

        print("Descansaste y recuperaste energía.")


    # BLOQUEO POR ALARMA
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nLa alarma bloqueó la bóveda.")
        print("DERROTA.")
        break


# RESULTADO FINAL
if cerraduras_abiertas == 3:
    print("\n¡¡¡VICTORIA!!!")
    print("Lograste abrir las 3 cerraduras.")

elif alarma == True:
    print("\nDERROTA.")
    print("La bóveda quedó bloqueada por la alarma.")

elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA.")
    print("Te quedaste sin energía o sin tiempo.")

#---------------------------------------------------------------------------------------------------------------------

# ==========================================
# EJERCICIO 5 - LA ARENA DEL GLADIADOR
# ==========================================

# ------------------------------------------
# PASO 1: NOMBRE DEL GLADIADOR
# ------------------------------------------

nombre = input("Nombre del Gladiador: ").strip()

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()


# ------------------------------------------
# PASO 2: ESTADÍSTICAS INICIALES
# ------------------------------------------

vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
danio_enemigo = 12

turno_gladiador = True


# ------------------------------------------
# INICIO DEL JUEGO
# ------------------------------------------

print()
print("--- BIENVENIDO A LA ARENA ---")
print()
print("=== INICIO DEL COMBATE ===")


# ------------------------------------------
# PASO 3: CICLO DE COMBATE
# ------------------------------------------

while vida_jugador > 0 and vida_enemigo > 0:

    # --------------------------------------
    # MOSTRAR ESTADO ACTUAL
    # --------------------------------------

    print()
    print(
        nombre,
        "(HP:", vida_jugador,
        ") vs Enemigo (HP:", vida_enemigo,
        ") | Pociones:", pociones
    )

    print()
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # --------------------------------------
    # VALIDACIÓN DE LA OPCIÓN
    # --------------------------------------

    opcion = input("Opción: ").strip()

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ").strip()

    opcion = int(opcion)


    # ======================================
    # ACCIÓN 1: ATAQUE PESADO
    # ======================================

    if opcion == 1:

        # Daño base
        danio_final = ataque_pesado

        # Golpe crítico
        if vida_enemigo < 20:
            danio_final = ataque_pesado * 1.5
            print(">> ¡GOLPE CRÍTICO!")

        vida_enemigo = vida_enemigo - danio_final

        # Evitamos que la vida quede negativa
        if vida_enemigo < 0:
            vida_enemigo = 0

        print(
            "¡Atacaste al enemigo por",
            danio_final,
            "puntos de daño!"
        )


    # ======================================
    # ACCIÓN 2: RÁFAGA VELOZ
    # ======================================

    elif opcion == 2:

        print(">> ¡Inicias una ráfaga de golpes!")

        for golpe in range(3):

            vida_enemigo = vida_enemigo - 5

            # Evitamos que la vida quede negativa
            if vida_enemigo < 0:
                vida_enemigo = 0

            print("> Golpe conectado por 5 de daño")

            # Si el enemigo murió, terminamos
            # los golpes de la ráfaga
            if vida_enemigo <= 0:
                break


    # ======================================
    # ACCIÓN 3: CURAR
    # ======================================

    elif opcion == 3:

        if pociones > 0:

            vida_jugador = vida_jugador + 30
            pociones = pociones - 1

            print("¡Usaste una poción!")
            print("Recuperaste 30 puntos de vida.")

        else:

            print("¡No quedan pociones!")


    # ======================================
    # TURNO DEL ENEMIGO
    # ======================================

    # El enemigo solamente ataca si sigue vivo
    if vida_enemigo > 0:

        vida_jugador = vida_jugador - danio_enemigo

        # Evitamos que la vida quede negativa
        if vida_jugador < 0:
            vida_jugador = 0

        print(
            ">> ¡El enemigo contraataca por",
            danio_enemigo,
            "puntos de daño!"
        )

    print()
    print("=== NUEVO TURNO ===")


# ------------------------------------------
# PASO 4: FIN DEL JUEGO
# ------------------------------------------

print()
print("===================================")
print("           FIN DEL JUEGO")
print("===================================")

if vida_jugador > 0:

    print(
        "¡VICTORIA!",
        nombre,
        "ha ganado la batalla."
    )

else:

    print("DERROTA. Has caído en combate.")






















