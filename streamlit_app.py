import streamlit as st

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
        .challenge-header {
            color: #FF4500;
            font-size: 2em;
        }
        .code-area {
            background-color: #f9f9f9;
            border: 2px solid #87CEEB;
            border-radius: 5px;
            padding: 10px;
            font-family: 'Courier New', Courier, monospace;
        }
        </style>
        <h1 class="main-title">🤖 Aprende Python con Codey</h1>
        <h2 class="sub-title">¡Hola, pequeño programador! Vamos a escribir código y divertirnos juntos.</h2>
        """,
        unsafe_allow_html=True
    )

    # Opciones de desafíos
    desafio = st.selectbox(
        "Elige un desafío:",
        ["Hola, Mundo", "Crea un Nombre Divertido", "Ayuda a Codey a Contar"]
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    if desafio == "Hola, Mundo":
        st.markdown("<h3 class='challenge-header'>Desafío 1: Hola, Mundo</h3>", unsafe_allow_html=True)
        st.write("Completa el código para que Codey diga '¡Hola, Mundo!' en la pantalla.")

        code = st.text_area("Escribe tu código aquí:", "print('¡Hola, mundo!')", help="Escribe print('¡Hola, mundo!') para completar el desafío.")

        if st.button("Ejecutar Código"):
            try:
                exec(code)
            except Exception as e:
                st.error(f"Error: {e}")

    elif desafio == "Crea un Nombre Divertido":
        st.markdown("<h3 class='challenge-header'>Desafío 2: Crea un Nombre Divertido</h3>", unsafe_allow_html=True)
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
        st.markdown("<h3 class='challenge-header'>Desafío 3: Ayuda a Codey a Contar</h3>", unsafe_allow_html=True)
        st.write("Completa el código para que Codey cuente hasta 10.")

        code = st.text_area("Escribe tu código aquí:", """# Completa el código\nfor i in range(1, 11):
    print(f'Estoy contando: {i}')""", help="Usa un bucle for para contar del 1 al 10.")

        if st.button("Ejecutar Código"):
            try:
                exec(code)
            except Exception as e:
                st.error(f"Error: {e}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>¿Quieres aprender más? ¡Sigue explorando con Codey y practica tus superpoderes de programación!</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
