# Sitio Web con Flask y Bootstrap

Un sitio web completo desarrollado con Python Flask y Bootstrap 5, que incluye navegación, formularios, blog y diseño responsivo.

## 🚀 Características

-   **Framework**: Flask (Python)
-   **Frontend**: Bootstrap 5 + Font Awesome
-   **Formularios**: Flask-WTF con validación
-   **Diseño**: Responsivo y moderno
-   **Páginas**: Inicio, Acerca, Servicios, Blog, Contacto

## 📁 Estructura del Proyecto

```
flask_web_app/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── inicio.html       # Página de inicio
│   ├── acerca.html       # Página "Acerca de"
│   ├── servicios.html    # Página de servicios
│   ├── blog.html         # Lista del blog
│   ├── post.html         # Post individual
│   └── contacto.html     # Página de contacto
└── README.md            # Este archivo
```

## 🛠️ Instalación

### Prerrequisitos

-   Python 3.7 o superior
-   pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona o descarga el proyecto**

    ```bash
    cd python/flask_web_app
    ```

2. **Instala las dependencias**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ejecuta la aplicación**

    ```bash
    python app.py
    ```

4. **Abre tu navegador**
    - Ve a: `http://localhost:5000`

## 📋 Dependencias

-   **Flask**: Framework web para Python
-   **Flask-WTF**: Integración de formularios
-   **Werkzeug**: Utilidades WSGI

## 🎨 Páginas Incluidas

### 🏠 Inicio (`/`)

-   Sección hero con llamadas a la acción
-   Características principales
-   Tecnologías utilizadas
-   CTA final

### ℹ️ Acerca (`/acerca`)

-   Historia de la empresa
-   Misión, visión y valores
-   Equipo de trabajo
-   Tecnologías y herramientas

### ⚙️ Servicios (`/servicios`)

-   Lista de servicios ofrecidos
-   Proceso de trabajo
-   Planes y precios
-   CTA personalizado

### 📝 Blog (`/blog`)

-   Lista de artículos
-   Paginación
-   Categorías
-   Newsletter

### 📄 Post Individual (`/post/<id>`)

-   Contenido completo del artículo
-   Navegación entre posts
-   Comentarios
-   Sidebar con artículos relacionados

### 📧 Contacto (`/contacto`)

-   Formulario funcional con validación
-   Información de contacto
-   Mapa integrado
-   Preguntas frecuentes

## 🔧 Personalización

### Cambiar Colores

Edita el archivo `templates/base.html` y modifica las variables CSS:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
}
```

### Agregar Nuevas Páginas

1. Crea una nueva plantilla en `templates/`
2. Agrega la ruta en `app.py`
3. Actualiza la navegación en `base.html`

### Modificar Contenido

-   **Datos del blog**: Edita la lista `posts` en `app.py`
-   **Servicios**: Modifica la lista `servicios_lista` en la función `servicios()`
-   **Información de contacto**: Actualiza en `contacto.html`

## 🚀 Despliegue

### Opciones de Despliegue

1. **Heroku**

    ```bash
    # Crear Procfile
    echo "web: gunicorn app:app" > Procfile

    # Instalar gunicorn
    pip install gunicorn
    ```

2. **PythonAnywhere**

    - Sube los archivos
    - Configura WSGI
    - Activa el entorno virtual

3. **VPS/Dedicado**
    ```bash
    # Instalar nginx + gunicorn
    sudo apt install nginx
    pip install gunicorn
    ```

## 📚 Recursos Adicionales

### Documentación Oficial

-   [Flask Documentation](https://flask.palletsprojects.com/)
-   [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
-   [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)

### Tutoriales Recomendados

-   [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
-   [Bootstrap 5 Tutorial](https://www.w3schools.com/bootstrap5/)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes preguntas o necesitas ayuda:

-   📧 Email: soporte@misitioweb.com
-   💬 Issues: Crea un issue en GitHub
-   📖 Documentación: Revisa los comentarios en el código

## 🎯 Próximas Mejoras

-   [ ] Sistema de autenticación
-   [ ] Panel de administración
-   [ ] Base de datos integrada
-   [ ] API REST
-   [ ] Sistema de comentarios
-   [ ] Optimización SEO
-   [ ] Cache y CDN
-   [ ] Tests automatizados

---

**¡Disfruta desarrollando con Flask y Bootstrap!** 🚀
