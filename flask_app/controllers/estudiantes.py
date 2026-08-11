from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso

@app.route('/estudiante')
def mostrar_formulario():
    cursos = Curso.get_courses()
    return render_template("agregar_estudiante.html", cursos = cursos)

@app.route('/crear_estudiante', methods=['POST'])
def crear_estudiante():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso']
    }

    Estudiante.save(datos)
    return redirect('/estudiante')