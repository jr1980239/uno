import pyrebase

DB_URL="https://practic26-b9d90.firebaseio.com"

config = {
  "apiKey": "AIzaSyCB_8ftoJBEYjTy22oWrxwLdll5gCSkbLo",
  "authDomain": "practic26-b9d90.firebaseapp.com",
  "databaseURL": "https://practic26-b9d90.firebaseio.com/",
  "storageBucket": "practic26-b9d90.appspot.com"
}

firebase = pyrebase.initialize_app(config)


# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("jr198023@gmail.com", 123456)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Luis Rodriguezsss", "edad":50, "correo":None, "lista":["rojo","azul","blanco"]
}
db.child("users").child("Morty").set(data)
# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])

data = {
    "name": "Jose Rodriguezx", "edad":36, "correo":"jr198023@gmail.com", "lista":["rojo","azul","blanco"]
}
db.child("users").child("Morty").set(data)
# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])


