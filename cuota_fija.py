def simulador_cuotas(valorprestado, tasa_interes, tiempo_limite):
    """
    Calcular cuota fija
    """
    CuotaFija=(valorprestado*((tasa_interes/100)*(1+(tasa_interes/100))**tiempo_limite))/(((1+(tasa_interes/100))**tiempo_limite)-1)
    print("Cuotas Fija $ %5.1f" % float(CuotaFija))
    saldo=valorprestado
    for i in range(int(tiempo_limite)):
       interes_generado= saldo * (tasa_interes/100)
       abono=(CuotaFija - interes_generado)
       saldo=saldo-abono
       i+=1
       print("Mes %d - Saldo Capital $ %5.1f - Cuota Fija Mensual $ %5.1f - Interes Generado $ %5.1f - Abono a Capital $ %5.1f" % (int(i), float(saldo),  float(CuotaFija), float(interes_generado), float(abono)))
    
valorprestado=float(input("Ingrese Valor a prestar : "))
tasa_interes=float(input("Interes Mensual: "))
tiempo_limite=int(input("Tiempo a prestar en Meses: "))

simulador_cuotas(valorprestado, tasa_interes, tiempo_limite)
    