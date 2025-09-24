
import streamlit as st


# Configuración general
st.set_page_config(page_title="Presupuesto Geotécnico", page_icon="📊")


#titulo y descripción de la app
st.set_page_config(page_title="GTN | GEOEXPLO GDL", page_icon=":material/sort:", layout="centered")
st.markdown("<center><h2>📊 CALCULADORA DE EXPLORACIÓN GEOTÉCNICA </h2></center>", unsafe_allow_html=True)
st.markdown("<center><h5>Made by Geotecniapps.com</h5></center>", unsafe_allow_html=True)




#st.title("📊 Cálculadora de Exploración Geotécnica")
#st.markdown("Para proyectos de hasta 2000 m2 y 10 niveles")
#st.markdown("<center><h5>Made by Geotecniapps</h5></center>", unsafe_allow_html=True)
#st.warning("⚠️ **Descargo de Responsabilidad:** Esta aplicación es una herramienta educativa y no reemplaza la evaluación de un ingeniero geotecnico calificado. Siempre consulta a un profesional para el diseño final.")
#st.link_button("Volver a Geotecniapps", url="https://geotecniapps.com/", type='primary')

st.image("anunciate_aqui.gif", use_container_width=True)

# Ingreso de datos del proyecto
st.header("📝 Datos del Proyecto")
nombre_proyecto = st.text_input("Nombre del proyecto")
ubicacion = st.selectbox("Ubicación", ["Guadalajara", "Zapopan"])
st.divider()

st.write("El número de sondeos está en función del área de desplante de la construcción")
area = st.number_input("Área de construcción (m²)", min_value=0)
st.divider()

st.write("La profundidad de los sondeos está en función del número de niveles")
niveles = st.number_input("Número de niveles", min_value=1)
st.info("El número de niveles considera solo niveles superiores a nivel de calle. En este dato no considerar sótanos.")
nivel_PB = st.number_input("Nivel de de planta baja o desde el nivel inferior del último sótano cuando existan medido desde el nivel de terreno natural (m)", max_value=0)


BTN_calc = st.button("CALCULAR", type='primary')


# Cálculos simples
if BTN_calc:
    
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
        profundidad = 16
    elif niveles > 10:
        profundidad = ">10"
    else:
        profundidad = 'error'   

    
    #Numero de sondeos
    if 0 < area <= 100:
        num_sondeos = 1
    elif 100 < area <= 250:
        num_sondeos = 2
    elif 250 < area <=1000:
        num_sondeos = 3
    elif area > 1000 :
        num_sondeos = ">4"
    else:
        num_sondeos = 'error'

    


    #Tipo de sondeo
    tipo_sondeo = "SPT"
    

    # Mostrar resultados
    st.header("🔍 Recomendación Técnica")
    st.write(f"Tipo de sondeo sugerido: {tipo_sondeo}")
    
    st.write(f"Número de sondeos: {num_sondeos}")
    if num_sondeos == ">4":
        st.warning("Para áreas de construcción mayores a 1000 m2, el número de sondeos estará determinado en función de la variabilidad del terreno , y tocará al especialista geotécnico determinar el número de sondeos y a la Dirección General de Obras Públicas aprobarlo.")
    
    
    st.write(f"Profundidad estimada por sondeo: {profundidad} m")
    st.info("Esta profundidad es desde el nivel de planta baja o desde el nivel inferior del último sótano cuando existan")
    st.success(f"La profundidad total del sondeo debe ser de : {profundidad - nivel_PB} m desde el nivel de terreno natural")

    if profundidad == ">10":
        st.warning("Para proyectos mayores de 10 niveles, la profundidad de los sondeos deberá ser tal que el incremento de esfuerzos no sea mayor de aproximadamente el 10% de los esfuerzos efectivos iniciales. Tocará al geotécnico determinar esas profundidades, y a la Dirección General de Obras Públicas aprobarlas.")
    
    st.divider()

    st.warning("⚠️ **Nota Importante:** En caso de encontrarse roca antes de alcanzar la profundidad mínima requerida, en construcciones de diez o más niveles deberá perforarse al menos 3 m dentro de la roca para verificar que el manto sea continuo. Si la construcción será menor de diez niveles, en vez de perforar en roca se podrá optar por realizar sondeos adicionales para constatar la continuidad del manto rocoso.")
   

    st.header("💰 Si desea una Cotizacion")
    st.write("📩Contácte a proyectos@geotecniaterranova.com")
    st.write("✅o por Whatsapp https://wa.link/vai3cy") 





st.warning("⚠️ **Descarga de Responsabilidad:** Esta aplicación es una herramienta educativa y no reemplaza la evaluación de un ingeniero geotecnico calificado. Siempre consulta a un profesional para el diseño final.")

st.write("Agradecemos a los usuarios su retroalimentación para mejorar esta herramienta. Si tienes sugerencias o encuentras errores, por favor contáctanos a través de nuestras redes sociales o correo electrónico geotecniapps@gmail.com")

st.link_button("Volver a Geotecniapps", url="https://geotecniapps.com/", type='primary', icon=":material/home:")
