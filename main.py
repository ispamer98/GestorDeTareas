from flask import Flask, render_template, request, redirect, url_for
import db
from models import Task, Comment

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

# Crear instancias de Task y Comment para datos iniciales
def init_data():
    # Verificar si ya existen tareas y comentarios en la base de datos
    existing_tasks = db.session.query(Task).count()
    existing_comments = db.session.query(Comment).count()

    if existing_tasks == 0 and existing_comments == 0:
        #Si ambas estan vacias, el programa entiende que es la primera vez que se
        #ejecuta, por lo que creará las tareas y comentarios por defecto
        # Creamos instancias de Task
        task1 = Task(content="Seguir aprendiendo python",completed=False)
        task2 = Task(content="Aprender Flask",completed=False)
        task3 = Task(content="Aprender HTML y CSS",completed=False)
        task4 = Task(content="Terminar esta tarea",completed=True)

        # Creamos instancias de Comment
        comment1 = Comment(name="Ana",
                           comment="¡Increible apicación, "
                                   "me ha gustado mucho tanto el diseño como la funcionalidad!",
                           date="24 / 09 / 2020  -  10:45")
        comment2 = Comment(name="Pedro",
                           comment="Creo que necesita algunos cambios,"
                                   "como un inicio de sesión, por lo demás es una pagina web estupenda.",
                           date="06 / 10 / 2021  -  15:20")
        comment3 = Comment(name="María",
                           comment="Me parece estupendo y muy acertado "
                                   "el enfoque que se le ha dado a esta página web, es ¡ INCREIBLE !",
                           date="29 / 06 / 2022  -  09:10")
        comment4 = Comment(name="Juan",
                           comment="Quería aprovechar esta caja de comentarios para "
                                   "felicitar a Rubén Salazar Diaz por su esfuerzo en este curso y su gran trabajo, "
                                   "reflejado en esta página web tan bonita y práctica",
                           date="15 / 03 / 2023  -  14:00")

        # Agregamos instancias en la base de datos
        db.session.add_all([task1, task2, task3, task4, comment1, comment2, comment3, comment4])
        try:
            db.session.commit()  # Ejecutar la operación pendiente de la base de datos
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error en la transacción: {e}")
        db.session.close()



#Endpoint referido a la raid "/"
@app.route('/')
def home():
    all_tasks = db.session.query(Task).all()  # Consulta todas las tareas desde la base de datos
    return render_template('index.html', tasks_list=all_tasks)
    #Busca en el archivo Index para proporcionar la info que se encuentre en el.
    #Envia además la info de la base de datos al HTML

#Endpoint referido a la pagina de comentarios
@app.route('/comentarios')
def comments():
    all_comments = db.session.query(Comment).order_by(Comment.id.desc()).all()
    return render_template('comentarios.html',comments_list=all_comments)
    #Busca en el archivo Comentarios para proporcionar la info que se encuentre en el.
    #Envia además la info de la base de datos al HTML

#Endpoint referido a pagina del formulario de comentarios
@app.route('/formulario-comentarios')
def comments_form():
    return render_template('formulario-comentarios.html')
    #Busca en el archivo Formulario Comentarios para proporcionar la info que se encuentre en el.



#El endpoint se encarga de crear la tarea con la info del action del html con el metodo post
@app.route("/create_task",methods=["POST"])
def create_task():
    task=Task(content=request.form["content_task"],completed=False)
    db.session.add(task)
    try:
        db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error en la transacción: {e}")
    db.session.close()
    return redirect(url_for("home"))

#El endpoint se encarga de crear el comentario con la info del action del html con el metodo post
@app.route("/create_comment",methods=["POST"])
def create_comment():
    comment=Comment(name=request.form["name"],comment=request.form["comment"])
    db.session.add(comment)
    try:
        db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error en la transacción: {e}")
    db.session.close()
    return redirect(url_for("comments"))

@app.route("/completed_task/<int:task_id>")
def completed_task(task_id):
    task = db.session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = not task.completed  # Invertir el estado completado
        try:
            db.session.commit()  # Ejecutar la operación pendiente de la base de datos
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error en la transacción: {e}")
        db.session.close()
    return redirect(url_for("home"))


@app.route('/delete_comment/<id>')
def delete_comment(id):
    comment=db.session.query(Comment).filter_by(id=int(id)).delete()
    # Se busca dentro de la base de datos, aquel registro cuyo id coincida
    # con el aportado por el parametro de la ruta. Cuando se encuentra se elimina
    try:
        db.session.commit() # Ejecutar la operación pendiente de la base de datos
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error en la transacción: {e}")
    db.session.close()
    return redirect(url_for("comments")) # Esto nos redirecciona a la función comments()
    # y si ha ido bien, al refrescar, el comentario eliminado ya no aparecera en el listado

@app.route('/delete_task/<id>')
def delete(id):
    task = db.session.query(Task).filter_by(id=int(id)).delete()
    # Se busca dentro de la base de datos, aquel registro cuyo id coincida
    # con el aportado por el parametro de la ruta. Cuando se encuentra se elimina

    try:
        db.session.commit() # Ejecutar la operación pendiente de la base de datos
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error en la transacción: {e}")
    db.session.close()
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()
    # y si ha ido bien, al refrescar, la tarea eliminada ya no aparecera en el listado

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)  # Creamos el modelo de datos
    init_data()
    app.run()
