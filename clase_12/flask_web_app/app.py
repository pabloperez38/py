from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Formulario de contacto
class ContactForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Datos de ejemplo para el blog
posts = [
    {
        'id': 1,
        'titulo': 'Introducción a Flask',
        'contenido': 'Flask es un microframework web para Python que permite crear aplicaciones web de forma rápida y sencilla.',
        'autor': 'Admin',
        'fecha': '8/5/2025'
    },
    {
        'id': 2,
        'titulo': 'Bootstrap en Flask',
        'contenido': 'Bootstrap es un framework CSS que facilita el diseño responsive y moderno de aplicaciones web.',
        'autor': 'Admin',
        'fecha': '8/5/2025'
    }
]

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/servicios')
def servicios():
    servicios_lista = [
        {
            'titulo': 'Desarrollo Web',
            'descripcion': 'Creamos sitios web modernos y responsivos',
            'icono': 'fas fa-code'
        },
        {
            'titulo': 'Diseño UI/UX',
            'descripcion': 'Diseños intuitivos y atractivos para tu negocio',
            'icono': 'fas fa-paint-brush'
        },
        {
            'titulo': 'Consultoría IT',
            'descripcion': 'Asesoramiento especializado en tecnología',
            'icono': 'fas fa-laptop-code'
        }
    ]
    return render_template('servicios.html', servicios=servicios_lista)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        # Aquí procesarías el formulario (enviar email, guardar en BD, etc.)
        flash('¡Mensaje enviado con éxito!', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html', form=form)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return redirect(url_for('blog'))
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True) 