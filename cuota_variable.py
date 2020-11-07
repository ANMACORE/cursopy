valorprestado=float(input("Ingrese Valor a prestar : "))
tasa_interes=float(input("Interes Mensual: "))
tiempo_limite=int(input("Tiempo a prestar en Meses: "))

amortizacion=valorprestado/tiempo_limite
saldo=valorprestado
print("Cuotas Variables")
for i in range(int(tiempo_limite)):
    interes_generado= saldo * (tasa_interes/100)
    valorpagar=interes_generado+amortizacion
    saldo=(saldo+interes_generado)-valorpagar
    deudainicial=saldo+amortizacion
    i+=1
    print("Mes %d - Deuda Inicial $ %5.1f - Interes Generado $ %5.1f - Amortización $ %5.1f - Valor a pagar $ %5.1f - Deuda Final $ %5.1f" % (int(i), float(deudainicial), float(interes_generado), float(amortizacion), float(valorpagar), float(saldo)))