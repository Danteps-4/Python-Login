# Python Simple Login

Login for an application written on Python using **tkinter** and **Postgresql**.

### Database
To connect to a **Postgresql database** you will have to head to [Conexion.py](http://github.com/Danteps-4/Python-Login/blob/master/Conexion.py "Conexion.py") and fill the necessary fields for connecting to an existing database.

```python
    _DB = "database"
    _USERNAME = "username"
    _HOST = "host"
    _PASSWORD = "password"
    _PORT = "port"
```
Filling this fields, the function will automatically connect to the specified database by calling `<obtener_conexion>` method.

```python
    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(database=cls._DB, user=cls._USERNAME, host=cls._HOST, password=cls._PASSWORD, port=cls._PORT)
                # print("Conexion exitosa")
                return cls._conexion
            except Exception as e:
                print(f"Error: {e}")
                sys.exit()
        else:
            return cls._conexion
```
This method will return the connection to an object called `<_conexion>` previosly defined in this same class [Conexion.py](http://github.com/Danteps-4/Python-Login/blob/master/Conexion.py "Conexion.py"). If there is an error with the parameters you filled previously, on the console it will display the error and the program will be terminated for itself.

#### Database Query

In the class [UsuarioDAO.py](http://github.com/Danteps-4/Python-Login/blob/master/UsuarioDAO.py "UsuarioDAO.py") are written all the necessary queries to run correctly the program.
```python
    _INSERTAR = "INSERT INTO usuarios(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuarios SET username=%s, password=%s WHERE id_usuario = %s"
    _SELECCIONAR = "SELECT id_usuario FROM usuarios WHERE username=%s AND password=%s"
    _ELIMINAR = "DELETE FROM usuarios WHERE id_usuario=%s"
```
You can modify this queries to make it adaptable for your database requirements.



### Actions

On the login-app you can execute the following actions:

1. **Login**: the user will enter his username and password. If the user exists, it will log in, but if the user does not exists, it will show a messagebox.showerror saying that the user do not exist so it is not possible to log in.
2. **Register**: the user will enter his username and password. The user will be registered in the database and will be asked to log in to get access to the main program.
3. **Delete user**: the user will enter his username and password. If the user exists, it will be deleted from the database, but if the user does not exists it will show a messagebox.showerror saying that the user do not exist so it is not possible to delete it.
4. **Exit**: this action will terminate the program completely.

### Images
Main page:

![ventana_login](https://user-images.githubusercontent.com/77952824/144902782-fcda9478-ca03-4c6a-8196-3394f02f07cb.png)

Login page:

![iniciar_sesion](https://user-images.githubusercontent.com/77952824/144954516-c019ad2a-de2e-49c0-b79d-e0dadd31381f.png)

Register page:

![registrarse](https://user-images.githubusercontent.com/77952824/144954518-e35724f9-d6d3-48b4-b7f1-bfb89cdb14b2.png)

Delete page:

![eliminar](https://user-images.githubusercontent.com/77952824/144954513-b3a36374-987d-47af-84f2-195dc90dc7c8.png)

Different features and improvements  will be added both in the interface and in the logic for a better user experience.