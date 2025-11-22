import streamlit as st

st.set_page_config(page_title="Scholar AI", layout="wide")

# Mantener historial
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Scholar AI")

# Mostrar mensajes estilo ChatGPT
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="background:#f0f0f0;padding:10px;border-radius:8px;margin-bottom:10px;">
                <strong>Tú:</strong><br>{msg["content"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="background:#e8f3ff;padding:10px;border-radius:8px;margin-bottom:10px;">
                <strong>Asistente:</strong><br>{msg["content"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<hr>", unsafe_allow_html=True)

# Caja de entrada estilo ChatGPT (abajo)
with st.container():
    col1, col2 = st.columns([7, 1])

    with col1:
        user_input = st.text_area(
            "Escribe tu mensaje:",
            "",
            height=80,
            label_visibility="collapsed"
        )

    with col2:
        send = st.button("Enviar", use_container_width=True)

# Lógica
if send and user_input.strip() != "":
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Respuesta temporaria (luego conectás tu modelo)
    response = f"Respuesta de ejemplo a: {user_input}"
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.experimental_rerun()
