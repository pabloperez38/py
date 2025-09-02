from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Configuración de la base de datos
DATABASE = 'productos.db'

def init_db():
    """Inicializar la base de datos y crear la tabla productos"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Obtener conexión a la base de datos"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Página principal - Lista de productos"""
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM productos ORDER BY fecha_creacion DESC').fetchall()
    conn.close()
    return render_template('index.html', productos=productos)

@app.route('/producto/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    """Crear nuevo producto"""
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria = request.form['categoria']
        
        if not nombre or not precio or not stock or not categoria:
            flash('Todos los campos obligatorios deben estar completos', 'error')
            return redirect(url_for('nuevo_producto'))
        
        try:
            conn = get_db_connection()
            conn.execute('''
                INSERT INTO productos (nombre, descripcion, precio, stock, categoria)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, descripcion, precio, stock, categoria))
            conn.commit()
            conn.close()
            flash('Producto creado exitosamente', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al crear el producto: {str(e)}', 'error')
            return redirect(url_for('nuevo_producto'))
    
    return render_template('nuevo_producto.html')

@app.route('/producto/<int:id>')
def ver_producto(id):
    """Ver detalles de un producto"""
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if producto is None:
        flash('Producto no encontrado', 'error')
        return redirect(url_for('index'))
    
    return render_template('ver_producto.html', producto=producto)

@app.route('/producto/<int:id>/editar', methods=['GET', 'POST'])
def editar_producto(id):
    """Editar producto existente"""
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if producto is None:
        flash('Producto no encontrado', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria = request.form['categoria']
        
        if not nombre or not precio or not stock or not categoria:
            flash('Todos los campos obligatorios deben estar completos', 'error')
            return redirect(url_for('editar_producto', id=id))
        
        try:
            conn = get_db_connection()
            conn.execute('''
                UPDATE productos 
                SET nombre = ?, descripcion = ?, precio = ?, stock = ?, categoria = ?
                WHERE id = ?
            ''', (nombre, descripcion, precio, stock, categoria, id))
            conn.commit()
            conn.close()
            flash('Producto actualizado exitosamente', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al actualizar el producto: {str(e)}', 'error')
            return redirect(url_for('editar_producto', id=id))
    
    return render_template('editar_producto.html', producto=producto)

@app.route('/producto/<int:id>/eliminar', methods=['POST'])
def eliminar_producto(id):
    """Eliminar producto"""
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    
    if producto is None:
        flash('Producto no encontrado', 'error')
        return redirect(url_for('index'))
    
    try:
        conn.execute('DELETE FROM productos WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('Producto eliminado exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar el producto: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/buscar')
def buscar_productos():
    """Buscar productos por nombre o categoría"""
    query = request.args.get('q', '')
    if not query:
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    productos = conn.execute('''
        SELECT * FROM productos 
        WHERE nombre LIKE ? OR categoria LIKE ? OR descripcion LIKE ?
        ORDER BY fecha_creacion DESC
    ''', (f'%{query}%', f'%{query}%', f'%{query}%')).fetchall()
    conn.close()
    
    return render_template('buscar.html', productos=productos, query=query)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
