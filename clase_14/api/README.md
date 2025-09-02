# API Flask-SQLite

API RESTful para gestionar items usando Flask y SQLite.

## Instalación

1. Instala dependencias:
   ```bash
   pip install flask flask_sqlalchemy
   ```
2. Ejecuta la app:
   ```bash
   python app.py
   ```

## Endpoints

### Listar todos los items

**GET** `/items`

**Respuesta:**
```json
{
  "success": true,
  "items": [
    {
      "id": 1,
      "name": "Ejemplo",
      "description": "Descripción",
      "price": 10.5,
      "quantity": 5,
      "is_active": true,
      "created_at": "...",
      "updated_at": "..."
    }
  ]
}
```

---

### Crear un item

**POST** `/items`

**Body JSON:**
```json
{
  "name": "Producto",
  "description": "Descripción opcional",
  "price": 12.99,
  "quantity": 10,
  "is_active": true
}
```

**Respuesta:**
```json
{
  "success": true,
  "item": { ... }
}
```

---

### Obtener un item por ID

**GET** `/items/<item_id>`

**Respuesta:**
```json
{
  "success": true,
  "item": { ... }
}
```

---

### Actualizar un item

**PUT** `/items/<item_id>`

**Body JSON:** (solo los campos que quieras actualizar)
```json
{
  "price": 15.0,
  "quantity": 20
}
```

**Respuesta:**
```json
{
  "success": true,
  "item": { ... }
}
```

---

### Eliminar un item

**DELETE** `/items/<item_id>`

**Respuesta:**
```json
{
  "success": true,
  "message": "Item <item_id> eliminado"
}
```

---

## Validaciones

- `name` es obligatorio al crear.
- `price` y `quantity` no pueden ser negativos.
- `price` debe ser numérico, `quantity` entero.

---

## Ejemplo de envío de datos (usando curl)

**Crear:**
```bash
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d "{\"name\":\"Lapiz\",\"price\":1.5,\"quantity\":100}"
```

**Actualizar:**
```bash
curl -X PUT http://localhost:5000/items/1 -H "Content-Type: application/json" -d "{\"price\":2.0}"
```

---

## Errores

Las respuestas de error tienen el formato:
```json
{
  "success": false,
  "error": "Descripción del error"
}
```

---

## Autor

API generada con Flask y