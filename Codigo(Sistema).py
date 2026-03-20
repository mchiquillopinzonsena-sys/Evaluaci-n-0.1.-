def sistema_asistencia_cronologico():
    print("══════════════════════════════════════════")
    print("   CENTRO DE CONTROL ACADÉMICO            ")
    print("══════════════════════════════════════════\n")

    try:
        nombre_alumno = input("Nombre completo del alumno: ").strip().title()

        pregunta_total = "Total de clases programadas para {}: ".format(nombre_alumno)
        total_clases = int(input(pregunta_total))
        clases_asistidas = int(input("Clases a las que asistió: "))

        if total_clases <= 0:
            print("\n[!] Error: El total de clases debe ser mayor a cero.")
            return
        if clases_asistidas < 0 or clases_asistidas > total_clases:
            print("\n[!] Error: Las asistencias no coinciden con el total.")
            return

        clases_faltadas = total_clases - clases_asistidas
        porcentaje_asistencia = (clases_asistidas / total_clases) * 100


        detalle_fechas = ""
        if clases_faltadas == 0:
            detalle_fechas = "⭐ ASISTENCIA PERFECTA ⭐"
        else:

            mensaje_faltas = "\nSe han detectado {} inasistencias.".format(clases_faltadas)
            print(mensaje_faltas)

            entrada_fechas = input("Ingrese las fechas de las faltas (ej: 05/Mar, 10/Mar): ")
            lista_fechas = [elemento.strip() for elemento in entrada_fechas.split(",")]
            detalle_fechas = " | ".join(lista_fechas)


        advertencia = "⚠️ ALERTA: El alumno está en riesgo por baja asistencia."
        advertenciaM = "✅ El alumno cumple con los requisitos de asistencia."

        if porcentaje_asistencia >= 80:
            estado = "Aprobado"
            mensaje_notificacion = advertenciaM
        else:
            estado = "En riesgo"
            mensaje_notificacion = advertencia

        print("\n╔" + "═" * 48 + "╗")
        print("║             FICHA ACADÉMICA INDIVIDUAL          ║")
        print("╠" + "═" * 48 + "╣")


        print("║ ESTUDIANTE: {}║".format(nombre_alumno.ljust(35)))
        print("║ ESTADO: {}║".format(estado.upper().ljust(39)))
        print("╟" + "─" * 48 + "╢")

        texto_asistencia = str(porcentaje_asistencia) + "%"
        print("║ > Asistencia Total : {}║".format(texto_asistencia.ljust(26)))

        resumen_clases = "{}/{}/{}".format(total_clases, clases_asistidas, clases_faltadas)
        print("║ > Clases (T/A/F)   : {}║".format(resumen_clases.ljust(25)))

        print("╟" + "─" * 48 + "╢")
        print("║ DETALLE DE INASISTENCIAS:                      ║")
        print("║ {}║".format(detalle_fechas[:45].ljust(47)))
        print("╠" + "═" * 48 + "╣")
        print("║ {}║".format(mensaje_notificacion.ljust(47)))
        print("╚" + "═" * 48 + "╝")

    except ValueError:
        print("\n[!] Error: Por favor, ingresa valores numéricos válidos.")

    sistema_asistencia_cronologico()