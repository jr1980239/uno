import pyrebase

DB_URL = "https://practic26-b9d90.firebaseio.com"
CONTENEDOR = "sismos"

config = {
    "apiKey": "AIzaSyCB_8ftoJBEYjTy22oWrxwLdll5gCSkbLo",
    "authDomain": "practic26-b9d90.firebaseapp.com",
    "databaseURL": "https://practic26-b9d90.firebaseio.com",
    "storageBucket": "practic26-b9d90.appspot.com"
}
firebase = pyrebase.initialize_app(config)


def obtenerBaseDatos():
    #auth = firebase.auth()
    #user = auth.sign_in_with_email_and_password("frankmalo86@gmail.com", "p.123456")
    db = firebase.database()
    return db


def grabarEvento(evento):
    registro = {"magnitud":11, "lugar": evento["properties"]["place"],
                "tiempo": evento["properties"]["time"], "longitud":evento["geometry"]["coordinates"][0],
                "latitud":evento["geometry"]["coordinates"][1]}
    db = obtenerBaseDatos()
    results = db.child(CONTENEDOR).child(evento["id"]).set(registro)


def leerEventos():
    db = obtenerBaseDatos()
    return db.child("sismos").order_by_child("tiempo").get()

def eliminarEvento(id):
    db = obtenerBaseDatos()
    return db.child("sismos").child(id).remove()


def actualizarEvento(id, campo_actualizar): #id que voy a actualizar
    db = obtenerBaseDatos()
    db.child("sismos").child(id).update(campo_actualizar)


