from flask_app.config.mysqlconnection import connectToMySQL

class Curso:
    DB = "esquema_estudiantes_cursos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.nombre_curso = data.get('nombre_curso')

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES(%(nombre)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, datos)

    @classmethod
    def get_courses(cls):
        query = "SELECT * FROM cursos;"
        cursos_en_bd = connectToMySQL(cls.DB).query_db(query)
        cursos = []
        for curso in cursos_en_bd:
            cursos.append(cls(curso))
        return cursos

    @classmethod
    def get_one(cls, datos):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        curso_en_db = connectToMySQL(cls.DB).query_db(query, datos)
        return cls(curso_en_db[0])