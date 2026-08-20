import streamlit as st

# Configuración de la página web
st.set_page_config(
    page_title="MADMeva26 - Matriz de Decisión",
    page_icon="📊",
    layout="centered",
)

# Inicializar el estado de la aplicación si no existe
if "paso" not in st.session_state:
  st.session_state.paso = "bienvenida"

if "nodo_actual" not in st.session_state:
  st.session_state.nodo_actual = "Q1"


def reiniciar():
  st.session_state.nodo_actual = "Q1"
  st.session_state.paso = "bienvenida"


# ==========================================
# 1. PANTALLA DE BIENVENIDA / PRESENTACIÓN
# ==========================================
if st.session_state.paso == "bienvenida":
  # Título muy vistoso y grande en la pantalla de inicio
  st.markdown(
      "<h1 style='text-align: center; color: #1f3a60;'>🚀 MADMeva26</h1>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<h3 style='text-align: center; color: #555555;'>Asistente de Selección"
      " de Metodología de Valoración</h3>",
      unsafe_allow_html=True,
  )
  st.markdown("---")

  st.write(
      "Esta herramienta interactiva está diseñada para guiar de forma rápida y"
      " estructurada en la selección del método de valoración adecuado según"
      " las características de su caso de estudio en servicios ecosistémicos."
  )

  # Tarjeta dedicada a los autores
  st.success(
      "**Autores:**\n"
      "- **José Pérez Roas**\n"
      "- **José Pérez Bracho**"
  )

  st.write("")
  if st.button(
      "Comenzar Evaluación", use_container_width=True, type="primary"
  ):
    st.session_state.paso = "matriz"
    st.rerun()

# ==========================================
# 2. PANTALLA DE LA MATRIZ (PREGUNTAS)
# ==========================================
elif st.session_state.paso == "matriz":
  st.title("MADMeva26 - Matriz de Decisión")
  st.markdown("---")

  nodos = {
      "Q1": {"texto": "¿Solo se requieren Valores de uso?"},
      "Q2": {
          "texto": (
              "¿El SE se relaciona con la recreación y requiere un"
              " desplazamiento?"
          )
      },
      "Q3": {
          "texto": (
              "¿El SE se relaciona con el precio de un bien inmueble y los"
              " salarios en mercados consolidados?"
          )
      },
      "Q4": {
          "texto": (
              "¿El SE se relaciona directa o indirectamente con la producción"
              " de un bien o servicio que cuente con un mercado consolidado?"
          )
      },
      "Q5": {
          "texto": (
              "¿E cantidad o calidad del SE afecta los costos de producción de"
              " un bien o servicio que cuente con un mercado consolidado?"
          )
      },
      "Q6": {"texto": "¿Se dispone de tiempo y recursos?"},
      "Q7": {
          "texto": (
              "¿Se requiere obtener un valor asociado a un cambio marginal del"
              " SE?"
          )
      },
      "Q8": {
          "texto": (
              "¿El cambio del SE puede ser prevenido, restaurado, reemplazado,"
              " mitigado o se puede relocar a la población en un lugar que se"
              " siga beneficiando del mismo en su estado inicial?"
          )
      },
      "Q9": {
          "texto": (
              "¿Se requiere obtener un valor asociado a diferentes niveles de"
              " calidad o cantidad del SE de acuerdo a escenarios de elección?"
          )
      },
      "Q11": {"texto": "¿La Calidad o cantidad del SE afectan a la población?"},
      "Q12": {
          "texto": (
              "¿Existe una valoración del SE en otro estudio y las condiciones"
              " del mismo se parecen a las del caso de interés?"
          )
      },
  }

  resultados = {
      "R_CostosViaje": "APLIQUE COSTOS DE VIAJE",
      "R_PreciosHedonicos": "APLIQUE PRECIOS HEDÓNICOS",
      "R_CambiosProductividad": "APLIQUE CAMBIOS EN LA PRODUCTIVIDAD",
      "R_CostosProduccion": "APLIQUE COSTOS DE PRODUCCIÓN",
      "R_ValoracionContingente": "APLIQUE VALORACIÓN CONTINGENTE",
      "R_ExperimentosEleccion": (
          "APLIQUE EXPERIMENTOS DE ELECCIÓN O VALORACIÓN CONJOINT"
      ),
      "R_GastosActuales": "APLIQUE GASTOS ACTUALES O POTENCIALES",
      "R_CostosSalud": "APLIQUE COSTOS DE SALUD",
      "R_TransferenciaBeneficios": "APLIQUE TRANSFERENCIA DE BENEFICIOS",
      "R_ReplantearObjetivo": "SE DEBE REPLANTEAR EL OBJETIVO DE LA VALORACIÓN",
  }

  nodo = st.session_state.nodo_actual

  if nodo in nodos:
    st.subheader(nodos[nodo]["texto"])
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
      if st.button("Sí", use_container_width=True, type="primary"):
        if nodo == "Q1":
          st.session_state.nodo_actual = "Q2"
        elif nodo == "Q2":
          st.session_state.nodo_actual = "R_CostosViaje"
        elif nodo == "Q3":
          st.session_state.nodo_actual = "R_PreciosHedonicos"
        elif nodo == "Q4":
          st.session_state.nodo_actual = "R_CambiosProductividad"
        elif nodo == "Q5":
          st.session_state.nodo_actual = "R_CostosProduccion"
        elif nodo == "Q6":
          st.session_state.nodo_actual = "Q7"
        elif nodo == "Q7":
          st.session_state.nodo_actual = "R_ValoracionContingente"
        elif nodo == "Q8":
          st.session_state.nodo_actual = "R_GastosActuales"
        elif nodo == "Q9":
          st.session_state.nodo_actual = "R_ExperimentosEleccion"
        elif nodo == "Q11":
          st.session_state.nodo_actual = "R_CostosSalud"
        elif nodo == "Q12":
          st.session_state.nodo_actual = "R_TransferenciaBeneficios"
        st.rerun()

    with col2:
      if st.button("No", use_container_width=True):
        if nodo == "Q1":
          st.session_state.nodo_actual = "Q6"
        elif nodo == "Q2":
          st.session_state.nodo_actual = "Q3"
        elif nodo == "Q3":
          st.session_state.nodo_actual = "Q4"
        elif nodo == "Q4":
          st.session_state.nodo_actual = "Q5"
        elif nodo == "Q5":
          st.session_state.nodo_actual = "Q6"
        elif nodo == "Q6":
          st.session_state.nodo_actual = "Q8"
        elif nodo == "Q7":
          st.session_state.nodo_actual = "Q9"
        elif nodo == "Q8":
          st.session_state.nodo_actual = "Q11"
        elif nodo == "Q9":
          st.session_state.nodo_actual = "Q8"
        elif nodo == "Q11":
          st.session_state.nodo_actual = "Q12"
        elif nodo == "Q12":
          st.session_state.nodo_actual = "R_ReplantearObjetivo"
        st.rerun()

  elif nodo in resultados:
    st.success("¡Evaluación completada con éxito!")
    st.markdown(f"### Resultado recomendado: \n **{resultados[nodo]}**")
    st.write("")

    col_res1, col_res2 = st.columns(2)
    with col_res1:
      if st.button("Finalizar y salir", use_container_width=True, type="primary"):
        st.session_state.paso = "despedida"
        st.rerun()
    with col_res2:
      if st.button("Reiniciar evaluación", use_container_width=True):
        reiniciar()
        st.rerun()

# ==========================================
# 3. PANTALLA DE DESPEDIDA
# ==========================================
elif st.session_state.paso == "despedida":
  st.title("👋 ¡Gracias por usar MADMeva26!")
  st.markdown("---")
  st.write(
      "El proceso de selección de la metodología de valoración ha concluido."
      " Esperamos que este asistente haya sido de gran utilidad para su"
      " investigación."
  )
  st.info(
      "Herramienta desarrollada por **José Pérez Roas** y **José Pérez"
      " Bracho**."
  )

  st.write("")
  if st.button("Volver al Inicio", use_container_width=True, type="primary"):
    reiniciar()
    st.rerun()