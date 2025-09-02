# Sistema de Gestión de Productos

Una aplicación web completa para gestionar productos con operaciones CRUD (Crear, Leer, Actualizar, Eliminar) desarrollada con Python Flask y SQLite.

## Características

- ✅ **CRUD Completo**: Crear, Leer, Actualizar y Eliminar productos
- ✅ **Base de Datos SQLite**: Almacenamiento local de datos
- ✅ **Interfaz Moderna**: Diseño responsive con Bootstrap 5
- ✅ **Búsqueda**: Buscar productos por nombre, categoría o descripción
- ✅ **Validación**: Validación de formularios en el servidor
- ✅ **Mensajes Flash**: Notificaciones de éxito y error
- ✅ **Diseño Responsive**: Funciona en dispositivos móviles y desktop

## Campos del Producto

1. **Nombre** (obligatorio)
2. **Descripción** (opcional)
3. **Precio** (obligatorio)
4. **Stock** (obligatorio)
5. **Categoría** (obligatorio)
6. **Fecha de Creación** (automática)

## Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   ```bash
   python app_productos.py
   ```

4. **Abrir en el navegador**:
   ```
   http://localhost:5000
   ```

## Estructura del Proyecto

```
├── app_productos.py          # Aplicación principal Flask
├── requirements.txt          # Dependencias de Python
├── README.md                # Este archivo
├── productos.db             # Base de datos SQLite (se crea automáticamente)
└── templates/               # Plantillas HTML
    ├── base.html            # Plantilla base con Bootstrap
    ├── index.html           # Página principal (lista de productos)
    ├── nuevo_producto.html  # Formulario para crear productos
    ├── editar_producto.html # Formulario para editar productos
    ├── ver_producto.html    # Vista detallada de un producto
    └── buscar.html          # Resultados de búsqueda
```

## Funcionalidades

### 📋 Lista de Productos
- Vista en tarjetas con información resumida
- Indicadores visuales de stock (verde: >10, amarillo: 1-10, rojo: 0)
- Botones de acción para cada producto

### ➕ Crear Producto
- Formulario con validación
- Campos obligatorios marcados
- Categorías predefinidas

### 👁️ Ver Producto
- Vista detallada completa
- Información de estado del stock
- Acciones rápidas

### ✏️ Editar Producto
- Formulario pre-llenado con datos actuales
- Misma validación que crear

### 🗑️ Eliminar Producto
- Confirmación mediante modal
- Prevención de eliminación accidental

### 🔍 Buscar Productos
- Búsqueda en tiempo real
- Busca en nombre, categoría y descripción
- Resultados con las mismas opciones CRUD

## Tecnologías Utilizadas

- **Backend**: Python Flask
- **Base de Datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5
- **Iconos**: Bootstrap Icons

## Personalización

### Agregar Nuevas Categorías
Edita el archivo `templates/nuevo_producto.html` y `templates/editar_producto.html` para agregar más opciones en el selector de categorías.

### Modificar Campos
Para agregar o modificar campos, necesitas:
1. Actualizar la tabla en `app_productos.py` (función `init_db()`)
2. Modificar los formularios en los templates
3. Actualizar las rutas de creación y edición

## Notas Importantes

- La base de datos se crea automáticamente al ejecutar la aplicación
- Los datos se almacenan localmente en `productos.db`
- La aplicación está configurada para desarrollo (debug=True)
- Para producción, cambiar la configuración de seguridad

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
