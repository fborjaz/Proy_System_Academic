# 🎓 Sistema de Gestión Académica 🎓

## 🚀 Descripción del Proyecto

Este sistema de gestión académica es una aplicación web desarrollada con Django y Tailwind CSS que permite gestionar información sobre estudiantes, profesores, asignaturas, periodos académicos y notas. El proyecto se basa en el uso del ORM (Object-Relational Mapping) de Django para interactuar con la base de datos de manera eficiente y elegante.

## ✨ Idea del Proyecto

La idea principal es crear una herramienta que facilite la administración de los datos académicos de una institución educativa. El sistema permitirá:

-   Registrar y gestionar información de estudiantes, profesores y asignaturas.
-   Crear y administrar periodos académicos.
-   Registrar notas y detalles de notas para los estudiantes.
-   Realizar consultas y análisis sobre los datos académicos.

## 🛠️ Tecnologías Utilizadas

-   **Lenguaje:** Python
-   **Framework Web:** Django
-   **ORM:** Django ORM
-   **Base de Datos:** SQLite (por defecto, pero se puede configurar para PostgreSQL)
-   **Frontend:** Tailwind CSS (un framework CSS de utilidad)
-   **Otras Dependencias:** django-extensions (para generar gráficos de modelos)

## ⚙️ Guía de Ejecución

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/fborjaz/Proy_System_Academic
    ```

2.  **Crear un entorno virtual:**

    ```bash
    python -m venv entorno_virtual
    ```

3.  **Activar el entorno virtual:**

    -   **Windows:**

        ```bash
        entorno_virtual\Scripts\activate
        ```

    -   **macOS/Linux:**

        ```bash
        source entorno_virtual/bin/activate
        ```

4.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Instalar dependencias de Node.js:**

    ```bash
    npm install -D tailwindcss postcss autoprefixer
    npx tailwindcss init
    ```

6.  **Compilar Tailwind CSS:**

    ```bash
    npx tailwindcss -i ./static/css/input.css -o ./static/css/style.css --watch
    ```

7.  **Aplicar las migraciones:**

    ```bash
    python manage.py migrate
    ```

8.  **Crear un superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

9.  **Iniciar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

10. **Acceder a la aplicación:** Abre tu navegador web y visita `http://127.0.0.1:8000/`.

## 📚 Recursos Adicionales

-   **Documentación de Django:** [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
-   **Documentación de Tailwind CSS:** [https://tailwindcss.com/docs/](https://tailwindcss.com/docs/)

---
**¡Esperamos que este sistema te sea de gran utilidad!** 😊

