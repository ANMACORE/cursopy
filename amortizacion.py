def amortizacion_1(monto, periodo, t_interes):
    '''
    Geneate calculation of payments
    :params: monto monto a prestar. Ie, 1000000
    :params: periodo tiempo de plazos. Ie, 24
    :params: t_interes tasa de interes. Ie, 0.1
    '''

    mensaje = '''Vamos a calcular la amortizacion de {monto}
    a un plazo de {periodo} con una tasa de interes de {t_interes} %'''.format(
        monto=monto,
        periodo=periodo,
        t_interes=t_interes*100,
    )
    print(mensaje)

    deuda_inicial = monto
    amortizacion = monto/periodo

    print('deuda_inicial', deuda_inicial)
    print('amortizacion', amortizacion)

    interes_generado = deuda_inicial * t_interes
    pago = amortizacion + interes_generado
    deuda_final = deuda_inicial + interes_generado - pago

    print ('deuda_inicial, interes_generado, pago, deuda_final')
    while deuda_final > 0:
        print(round(deuda_inicial, 3), round(interes_generado,3), round(pago,3), round(deuda_final,3))
        deuda_inicial = deuda_final
        interes_generado = deuda_inicial * t_interes
        pago = amortizacion + interes_generado
        if (deuda_inicial + interes_generado - pago) < 0:
            pago = deuda_inicial + interes_generado

        deuda_final = deuda_inicial + interes_generado - pago

    print(round(deuda_inicial, 3), round(interes_generado,3), round(pago,3), round(deuda_final,3))
    print('-esto se acabo!')

monto = 1000000
periodo = 24
t_interes = 0.1

amortizacion_1(monto, periodo, t_interes)