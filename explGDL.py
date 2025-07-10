
import streamlit as st
import pdfkit
import tempfile


# Configuración general
st.set_page_config(page_title="Presupuesto Geotécnico", page_icon="📊")

st.title("📊 Cálculo de Presupuesto Geotécnico")
st.markdown("Para proyectos de hasta 2000 m2 y 10 niveles")

# Ingreso de datos del proyecto
st.header("📝 Datos del Proyecto")
nombre_proyecto = st.text_input("Nombre del proyecto")
ubicacion = st.selectbox("Ubicación", ["Guadalajara", "Zapopan"])
area = st.number_input("Área de construcción (m²)", min_value=0)
niveles = st.number_input("Número de niveles", min_value=1)

# Cálculos simples
if area and niveles:
    
            #Determinar la profundidad de sondeos
       # NumeroDeNiveles = float(input('¿Cual es el NÚMERO DE NIVELES del proyecto? '))

    if niveles == 1:
        profundidad = 4
    elif niveles == 2:
        profundidad = 5
    elif niveles == 3:
        profundidad = 7
    elif niveles == 4 or 5:
        profundidad = 9
    elif niveles == 6 or 7:
        profundidad = 12
    elif niveles == 8 or 9:
        profundidad = 14
    elif niveles == 10:
        profundidad = 14
    else:
        profundidad = 'error'   

    
    #Numero de sondeos
    if 0 < area <= 100:
        num_sondeos = 1
    elif 100 < area <= 250:
        num_sondeos = 2
    elif 250 < area <=1000:
        num_sondeos = 3
    elif 1000 < area <=2000:
        num_sondeos = 4
    else:
        num_sondeos = 'error'

    
    #Tipo de sondeo
    tipo_sondeo = "SPT"
    
    st.header("🔍 Recomendación Técnica")
    st.write(f"Tipo de sondeo sugerido: {tipo_sondeo}")
    st.write(f"Número de sondeos: {num_sondeos}")
    st.write(f"Profundidad estimada por sondeo: {profundidad} m")

    # Precios base
    precio_por_m = 1000
    pu_laboratorio = 500
    laboratorio = num_sondeos * profundidad * pu_laboratorio
    movilizacion = 4000
    informe = 5000
    total_sondeo = num_sondeos * profundidad * precio_por_m
    total = total_sondeo + laboratorio + movilizacion + informe

    st.header("📄 Cotizacion Estimada")
    st.write(f"Total sondeos: ${total_sondeo:,.0f} MXN, considerando {precio_por_m} MXN por m de profundidad")
    st.write(f"Laboratorio: ${laboratorio:,.0f} MXN, considerando {pu_laboratorio} MXN por m de profundidad")
    st.write(f"Movilizacion: ${movilizacion:,.0f} MXN")
    st.write(f"Informe: ${informe:,.0f} MXN")
    st.subheader(f"💰 Total: ${total:,.0f} MXN")

    # Botón para generar PDF
    if st.button("📄 Generar PDF"):
        html = f"""
        <h1>Presupuesto Geotecnico</h1>
        <p><strong>Proyecto:</strong> {nombre_proyecto}</p>
        <p><strong>Ubicacion:</strong> {ubicacion}</p>
        <p><strong>Area:</strong> {area} m2</p>
        <p><strong>Niveles:</strong> {niveles}</p>
        <p><strong>Tipo de sondeo:</strong> {tipo_sondeo}</p>
        <p><strong>Numero de sondeos:</strong> {num_sondeos}</p>
        <p><strong>Profundidad por sondeo:</strong> {profundidad} m</p>
        <p><strong>Total estimado:</strong> ${total:,.0f} MXN</p>
        """

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdfkit.from_string(html, tmp_file.name)
            with open(tmp_file.name, "rb") as file:
                st.download_button(
                    label="⬇️ Descargar PDF",
                    data=file.read(),
                    file_name="cotizacion_geotecnica.pdf",
                    mime="application/pdf"
                )


if ubicacion == "Guadalajara":
    st.write("Ubicación: Guadalajara")

