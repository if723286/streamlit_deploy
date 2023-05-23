import streamlit as st
import pandas as pd
import random

def asignar_tasa_interes(monto_prestamo, periodos, primera_vez):
    if primera_vez:
        if periodos <= 6:
            return random.uniform(7.0, 7.6)
        else:
            return random.uniform(7.7, 8.3)
    else:
        #Monto de 2,000
        if monto_prestamo <= 2000 and periodos <= 6:
            return random.uniform(6.5, 6.7)
        elif monto_prestamo <= 2000 and periodos <= 12:
            return random.uniform(6.8, 7.0)
        #Monto de 4,000
        elif monto_prestamo <= 4000 and periodos <= 6:
            return random.uniform(6.0, 6.2)
        elif monto_prestamo <= 4000 and periodos <= 12:
            return random.uniform(6.3, 6.5)
        #Monto de 6,000
        elif monto_prestamo <= 6000 and periodos <= 6:
            return random.uniform(5.5, 5.7)
        elif monto_prestamo <= 6000 and periodos <= 12:
            return random.uniform(5.8, 6)
        #Monto de 8,000
        elif monto_prestamo <= 8000 and periodos <= 6:
            return random.uniform(5.0, 5.2)
        elif monto_prestamo <= 8000 and periodos <= 12:
            return random.uniform(5.3, 5.5)
        #Monto de 10,000
        elif monto_prestamo <= 10000 and periodos <= 6:
            return random.uniform(4.5, 4.7)
        else:
            return random.uniform(4.7, 5)


def calcular_tabla_amortizacion(monto_prestamo, periodos, primera_vez):
    if primera_vez:
        monto_prestamo = 1000
    tasa_interes = asignar_tasa_interes(monto_prestamo, periodos, primera_vez)
    tasa_interes_mensual = tasa_interes / 100 
    pago_mensual = monto_prestamo * (tasa_interes_mensual / (1 - (1 + tasa_interes_mensual) ** -periodos))
    
    saldo_restante = monto_prestamo
    tabla_amortizacion = []
    
    for i in range(1, periodos + 1):
        pago_interes = saldo_restante * tasa_interes_mensual
        pago_principal = pago_mensual - pago_interes
        saldo_restante -= pago_principal
        
        tabla_amortizacion.append((i, pago_mensual, pago_principal, pago_interes, saldo_restante))
    
    return tabla_amortizacion, tasa_interes

def mostrar_tabla_amortizacion(tabla_amortizacion):
    df = pd.DataFrame(tabla_amortizacion, columns=["Pago", "Monto", "Principal", "Interés", "Saldo"])
    df["Monto"] = df["Monto"].map("${:,.2f}".format)
    df["Principal"] = df["Principal"].map("${:,.2f}".format)
    df["Interés"] = df["Interés"].map("${:,.2f}".format)
    df["Saldo"] = df["Saldo"].map("${:,.2f}".format)
    st.table(df)

# Aplicación de Streamlit
st.title("Calculadora de Préstamos")

monto_prestamo = st.slider("Seleccione el monto del préstamo:", min_value=0, max_value=10_000, step=100, value=1000, format="$%d")
periodos = st.slider("Seleccione Duración de préstamo (en meses):", min_value=1, max_value=12, step=1, value=6, key="periodos_slider")
primera_vez = st.radio("¿Es la primera vez que solicita un préstamo a Moonetaes?", ("Sí", "No")) == "Sí"

st.write('---')

if st.button("Calcular"):
    if primera_vez:
        st.write("Esta vez podemos prestarte hasta $1,000 pesos por ser la primera vez que solicitas un préstamo con nosotros")
        st.write("Aqui esta tu tabla de pagos. ¡Se puntual con todos los pagos y podrías obtener un monto de credito mayor la próxima vez!")
        monto_prestamo = 1000
    tabla_amortizacion, tasa_interes = calcular_tabla_amortizacion(monto_prestamo, periodos, primera_vez)
    mostrar_tabla_amortizacion(tabla_amortizacion)

    # Resumen de la tabla de amortización
    total_intereses = sum(row[3] for row in tabla_amortizacion)
    total_pagos = sum(row[1] for row in tabla_amortizacion)
    st.info(f"**Monto de prestamo:** ${monto_prestamo:,.2f}")
    st.info(f"**Tasa de interés asignada:** {tasa_interes:.2f}%")
    st.info(f"**Total de intereses pagados:** ${total_intereses:,.2f}")
    st.info(f"**Total de pagos realizados:** ${total_pagos:,.2f}")









