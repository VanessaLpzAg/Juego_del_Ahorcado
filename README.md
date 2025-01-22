# 🕹️ Juego del Ahorcado 

¡Bienvenido al clásico **Juego del Ahorcado**, implementado en Python! Adivina la palabra oculta antes de quedarte sin vidas. 🚀

## 📖 Descripción 

1. El objetivo del juego es sencillo:
    - Comienza con una palabra oculta representada por guiones bajos (`_`), donde cada guion corresponde a una letra de la palabra.
    - El jugador debe introducir una letra en cada turno:
        - **Acierto**: Si la letra está en la palabra, se revela en las posiciones correspondientes.
        - **Error**: Si la letra no está en la palabra, pierdes una vida.
    - El juego termina cuando:
    - Adivinas correctamente toda la palabra (🎉 ¡Victoria!).
    - Te quedas sin vidas (💀 Derrota).



## 🚀 ¿Cómo jugar?

1. **Clona el repositorio** en tu computadora:
   
   ```bash
   git clone https://github.com/VanessaLpzAg/Juego_del_Ahorcado.git
   cd juego-del-ahorcado

2. **Ejecuta el script en Python**:

    main.py

Sigue las instrucciones en pantalla:

    - Introduce letras una por una.
    - Descubre la palabra antes de que se acaben las vidas.



## 📋 Reglas del juego:

1. La palabra a adivinar se inicializa al comienzo del script. Por defecto, es python.

2. El jugador tiene un número limitado de vidas (puedes ajustar este valor en el código).

3. Cada letra introducida será evaluada:
    - Si es correcta, se revela en la palabra.

    - Si es incorrecta, se pierde una vida y se muestra el número de vidas restantes.

4. El juego termina cuando:
    - Todas las letras son adivinadas (ganas 🎉).

    - Las vidas llegan a cero (pierdes 💀).



## ✨ Personalización:

1. Si quieres modificar el juego, aquí tienes algunas opciones:

2. Cambiar la palabra a adivinar:

    - Modifica la variable palabra_adivinar:

    - Ajustar el número de vidas:

3. Cambia el valor de vidas al inicio de la función:



## 🚀 Posibles mejoras futuras:

1. Ideas para expandir el juego:

    - Implementar un sistema de puntuación.

    - Añadir un archivo externo (palabras.txt) para cargar palabras automáticamente.

    - Mejorar la interfaz con gráficos ASCII que representen el ahorcado.

    - Soportar frases completas con espacios y caracteres especiales.