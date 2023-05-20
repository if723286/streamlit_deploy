import streamlit as st
import pandas as pd

def calcular_tabla_amortizacion(monto_prestamo, periodos, tasa_interes):
    tasa_interes_mensual = tasa_interes / 100 / 12
    pago_mensual = monto_prestamo * (tasa_interes_mensual / (1 - (1 + tasa_interes_mensual) ** -periodos))
    
    saldo_restante = monto_prestamo
    tabla_amortizacion = []
    
    for i in range(1, periodos + 1):
        pago_interes = saldo_restante * tasa_interes_mensual
        pago_principal = pago_mensual - pago_interes
        saldo_restante -= pago_principal
        
        tabla_amortizacion.append((i, pago_mensual, pago_principal, pago_interes, saldo_restante))
    
    return tabla_amortizacion

def mostrar_tabla_amortizacion(tabla_amortizacion):
    df = pd.DataFrame(tabla_amortizacion, columns=["Pago", "Monto", "Principal", "Interés", "Saldo"])
    df["Monto"] = df["Monto"].map("${:,.2f}".format)
    df["Principal"] = df["Principal"].map("${:,.2f}".format)
    df["Interés"] = df["Interés"].map("${:,.2f}".format)
    df["Saldo"] = df["Saldo"].map("${:,.2f}".format)
    st.table(df)

# Aplicación de Streamlit
st.title("Calculadora de Amortización de Préstamos")

monto_prestamo = st.slider("Seleccione el monto del préstamo:", min_value=0, max_value=10_000, step=100, value=1000, format="$%d")
periodos = st.slider("Seleccione el número de períodos:", min_value=1, max_value=60, step=1, value=6, key="periodos_slider")
tasa_interes = st.slider("Seleccione la tasa de interés:", min_value=0.0, max_value=20.0, step=0.1, value=7.0, format="%f%%", key="tasa_slider")

st.write('---')

if st.button("Calcular"):
    tabla_amortizacion = calcular_tabla_amortizacion(monto_prestamo, periodos, tasa_interes)
    mostrar_tabla_amortizacion(tabla_amortizacion)

    # Resumen de la tabla de amortización
    total_intereses = sum(row[3] for row in tabla_amortizacion)
    total_pagos = sum(row[1] for row in tabla_amortizacion)
    st.info(f"**Total de intereses pagados:** ${total_intereses:,.2f}")
    st.info(f"**Total de pagos realizados:** ${total_pagos:,.2f}")







