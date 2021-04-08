from flask import Flask,request,jsonify
from flask_cors import CORS

from models import db
from models import Alumno

from schemas import ma
from schemas import alumno_schema
from schemas import alumnos_schema

app = Flask(__name__)
#Configurando CORS
CORS(app)

#Configuración de la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pwsqladmin1@localhost/libreria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Ruta para obtener y agregar tareas
@app.route('/api/alumnos',methods=['GET','POST'])
def manage_alumnos():
  if request.method == 'POST':
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    codigo = request.json['codigo']
    nueva_tarea = Alumno(nombre,apellido, codigo)
    db.session.add(nueva_tarea)
    db.session.commit()
    return alumno_schema.jsonify(nueva_tarea)
  elif request.method == 'GET':
    todos = Alumno.query.all()
    result = alumnos_schema.dump(todos)
    return jsonify(result)

@app.route('/api/alumnos/<id>',methods=['GET','DELETE','PUT'])
def manage_alumno(id):
  if request.method == 'GET':
    tarea = Alumno.query.get(id)
    return alumno_schema.jsonify(tarea)
  elif request.method == 'PUT':
    tarea = Alumno.query.get(id)
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    codigo = request.json['codigo']
    tarea.nombre = nombre
    tarea.apellido = apellido
    tarea.codigo = codigo
    db.session.commit()
    return alumno_schema.jsonify(tarea)
  elif request.method == 'DELETE':
    tarea = Alumno.query.get(id)
    db.session.delete(tarea)
    db.session.commit()
    return alumno_schema.jsonify(tarea)


if __name__ == '__main__':  
  db.init_app(app)
  ma.init_app(app) 
  with app.app_context(): 
    db.create_all()
  app.run(port=5000,debug=True)