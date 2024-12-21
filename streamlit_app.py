import streamlit as st
import random

def main():
    st.set_page_config(page_title="Aprende Python con Codey", page_icon="🤖", layout="centered")

    # Título y bienvenida
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f8ff;
            color: #333;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .main-title {
            text-align: center;
            color: #1E90FF;
            font-size: 3em;
            margin-bottom: 10px;
        }
        .sub-title {
            text-align: center;
            color: #4682B4;
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        .map-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .map-section {
            width: 120px;
            height: 120px;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 1.2em;
            background-color: #FFB6C1;
            color: #fff;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            cursor: pointer;
        }
        .map-section.locked {
            background-color: #d3d3d3;
            color: #a9a9a9;
            cursor: not-allowed;
        }
        </style>
        <h1 class="main-title">🤖 Aprende Python con Codey</h1>
        <h2 class="sub-title">¡Explora el mapa y desbloquea misiones divertidas!</h2>
        """,
        unsafe_allow_html=True
    )

    # Misiones del mapa
    mapa = {
        "Misión 1": "Hola, Mundo",
        "Misión 2": "Crea un Nombre Divertido",
        "Misión 3": "Ayuda a Codey a Contar",
        "Misión 4": "Próximamente...",
        "Misión 5": "Próximamente...",
        "Misión 6": "Próximamente...",
        "Misión 7": "Próximamente...",
        "Misión 8": "Próximamente...",
        "Misión 9": "Próximamente...",
        "Misión 10": "Próximamente...",
    }

    # Desbloquear misiones dinámicamente
    misiones_desbloqueadas = 3

    st.markdown("<div class='map-container'>", unsafe_allow_html=True)

    for i, (clave, valor) in enumerate(mapa.items(), start=1):
        clase = "map-section locked" if i > misiones_desbloqueadas else "map-section"
        if st.button(f"{clave}", key=f"mision-{i}"):
            if i <= misiones_desbloqueadas:
                iniciar_mision(valor)
            else:
                st.warning("¡Completa las misiones anteriores para desbloquear esta!")

        st.markdown(f"<div class='{clase}'>{clave}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def iniciar_mision(desafio):
    st.markdown(f"<h3 style='color: #FF4500;'>Desafío: {desafio}</h3>", unsafe_allow_html=True)

    if desafio == "Hola, Mundo":
        st.write("Completa el código para que Codey diga '¡Hola, Mundo!' en la pantalla.")

        code = st.text_area("Escribe tu código aquí:", "print('¡Hola, mundo!')", help="Escribe print('¡Hola, mundo!') para completar el desafío.")

        if st.button("Ejecutar Código"):
            try:
                exec(code)
            except Exception as e:
                st.error(f"Error: {e}")

    elif desafio == "Crea un Nombre Divertido":
        st.write("Codey necesita ayuda para crear nombres para tus animales favoritos.")

        code = st.text_area("Escribe tu código aquí:", """# Completa el código\nanimal = input('¿Cuál es tu animal favorito? ')
nombre = input('¿Qué nombre quieres darle? ')
print(f'Tu {animal} se llama {nombre}.')""", help="Usa las variables 'animal' y 'nombre' para completar.")

        if st.button("Ejecutar Código"):
            try:
                exec(code)
            except Exception as e:
                st.error(f"Error: {e}")

    elif desafio == "Ayuda a Codey a Contar":
        st.write("Completa el código para que Codey cuente hasta 10.")

        code = st.text_area("Escribe tu código aquí:", """# Completa el código\nfor i in range(1, 11):
    print(f'Estoy contando: {i}')""", help="Usa un bucle for para contar del 1 al 10.")

        if st.button("Ejecutar Código"):
            try:
                exec(code)
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
