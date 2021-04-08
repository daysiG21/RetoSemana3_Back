from flask_marshmallow import Marshmallow

ma = Marshmallow()

class AlumnoSchema(ma.Schema):
  class Meta:
    fields = ('id','nombre','apellido','codigo')

alumno_schema = AlumnoSchema()
alumnos_schema = AlumnoSchema(many=True)