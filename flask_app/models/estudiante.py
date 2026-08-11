from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    DB = "esquema_estudiantes_cursos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.curso_id = data['curso_id']

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, created_at, updated_at, curso_id) VALUES(%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW(), %(curso_id)s);"
        return connectToMySQL(cls.DB).query_db(query, datos)

    @classmethod
    def get_estudents_for_course(cls, datos):
        query = """SELECT estudiantes.*
                   FROM estudiantes
                   WHERE estudiantes.curso_id = %(id)s
                   ORDER BY estudiantes.edad ASC;
                """
        results = connectToMySQL(cls.DB).query_db(query, datos)
        estudiantes = []
        if results:
            for r in results:
                estudiantes.append(cls(r))
        return estudiantes