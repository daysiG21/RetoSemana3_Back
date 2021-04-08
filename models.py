from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Creando el modelo de Tarea
class Alumno(db.Model):
  __tablename__ = 'alumno'

  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(70))
  apellido = db.Column(db.String(100))
  codigo = db.Column(db.String(10))

  def __init__(self, nombre, apellido, codigo):
    self.nombre = nombre
    self.apellido = apellido
    self.codigo=codigo