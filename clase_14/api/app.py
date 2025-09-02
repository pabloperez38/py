from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Configuración de la base de datos (SQLite en la raíz del proyecto)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Modelo Item ---
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

# Crear las tablas
with app.app_context():
    db.create_all()

# --- Manejo global de errores ---
@app.errorhandler(Exception)
def handle_exception(e):
    """Manejo global de errores en JSON"""
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({
            "success": False,
            "error": e.name,
            "description": e.description
        }).get_data()
        response.content_type = "application/json"
        return response
    else:
        return jsonify({
            "success": False,
            "error": "Internal Server Error",
            "description": str(e)
        }), 500

# --- Función de validación ---
def validate_item_data(data, is_update=False):
    """Valida los campos de entrada para crear o actualizar un item"""
    if not data:
        return False, "Debes enviar datos en el body"
    if not is_update and 'name' not in data:
        return False, "El campo 'name' es obligatorio"
    if 'price' in data:
        try:
            if float(data['price']) < 0:
                return False, "El campo 'price' no puede ser negativo"
        except:
            return False, "El campo 'price' debe ser un número"
    if 'quantity' in data:
        try:
            if int(data['quantity']) < 0:
                return False, "El campo 'quantity' no puede ser negativo"
        except:
            return False, "El campo 'quantity' debe ser un número entero"
    return True, None

# --- Endpoints CRUD ---

# Listar todos los items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify({"success": True, "items": [item.to_dict() for item in items]})

# Crear un item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    valid, error = validate_item_data(data)
    if not valid:
        return jsonify({"success": False, "error": error}), 400
    new_item = Item(
        name=data['name'],
        description=data.get('description'),
        price=float(data.get('price', 0.0)),
        quantity=int(data.get('quantity', 0)),
        is_active=bool(data.get('is_active', True))
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"success": True, "item": new_item.to_dict()}), 201

# Obtener un item por ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({"success": True, "item": item.to_dict()})

# Actualizar un item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    valid, error = validate_item_data(data, is_update=True)
    if not valid:
        return jsonify({"success": False, "error": error}), 400

    if 'name' in data:
        item.name = data['name']
    if 'description' in data:
        item.description = data['description']
    if 'price' in data:
        item.price = float(data['price'])
    if 'quantity' in data:
        item.quantity = int(data['quantity'])
    if 'is_active' in data:
        item.is_active = bool(data['is_active'])

    db.session.commit()
    return jsonify({"success": True, "item": item.to_dict()})

# Eliminar un item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"success": True, "message": f"Item {item_id} eliminado"}), 200

if __name__ == '__main__':
    app.run(debug=True)
