import streamlit as st

# Configuración de la página web
st.set_page_config(
    page_title="Matriz de Decisión - Metodología de Valoración",
    page_icon="📊",
    layout="centered",
)

st.title("Asistente de Selección de Metodología de Valoración")
st.markdown("---")

# Inicializar el estado de la pregunta actual en la sesión del navegador
if "nodo_actual" not in st.session_state:
  st.session_state.nodo_actual = "Q1"


def reiniciar():
  st.session_state.nodo_actual = "Q1"


# Diccionario de preguntas originales del diagrama
nodos = {
    "Q1": {"texto": "¿Solo se requieren Valores de uso?"},
    "Q2": {"texto": "¿El SE se relaciona con la recreación y requiere un desplazamiento?"},
    "Q3": {
        "texto": (
            "¿El SE se relaciona con el precio de un bien inmueble y los"
            " salarios en mercados consolidados?"
        )
    },
    "Q4": {
        "texto": (
            "¿El SE se relaciona directa o indirectamente con la producción de"
            " un bien o servicio que cuente con un mercado consolidado?"
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

# Lógica de navegación según el nodo actual
nodo = st.session_state.nodo_actual

if nodo in nodos:
  st.subheader(nodos[nodo]["texto"])
  st.write("")

  # Botones de Sí / No usando columnas para organizarlos lado a lado
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
  st.success("¡Evaluación completada!")
  st.markdown(f"### Resultado: \n **{resultados[nodo]}**")
  st.write("")
  if st.button("Reiniciar Evaluación", use_container_width=True):
    reiniciar()
    st.rerun()