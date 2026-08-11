from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route('/')
def index():
    cursos = Curso.get_courses()
    return render_template("index.html", cursos = cursos)

@app.route('/crear_curso',methods=['POST'])
def crear_curso():
    datos = {
        "nombre": request.form['nombre'],
    }
    Curso.save(datos)
    return redirect('/')

@app.route('/cursos/<int:curso_id>')
def obtener_estudiantes_del_curso(curso_id):
    datos = { 
        'id': curso_id
    }
    nombre_curso = Curso.get_one(datos).nombre
    estudiantes = Estudiante.get_estudents_for_course(datos)
    return render_template("mostrar_curso.html", nombre_curso = nombre_curso, estudiantes = estudiantes)