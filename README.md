# Python Simple Login

Login for an application written on Python using **tkinter** and **Postgresql**.

###Connect to Database
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

###Actions
On the login-app you can execute the following actions:

1. **Login**: the user will enter his username and password. If the user exists, it will log in, but if the user does not exists, it will show a messagebox.showerror saying that the user do not exist so it is not possible to log in.
2. **Register**: the user will enter his username and password. The user will be registered in the database and will be asked to log in.
3. **Delete user (not added)**
4. **Exit**: this action will terminate the program completely.

###Images
Main window:

![ventana_login](https://user-images.githubusercontent.com/77952824/144790426-6d8955db-361f-4c27-8e80-a5611e72ca38.png)

Login window:

![iniciar_sesion](https://user-images.githubusercontent.com/77952824/144790612-0a5f148d-1844-4d29-a1b7-3751ac5d86bb.png)

Register window:

![registrarse](https://user-images.githubusercontent.com/77952824/144790616-d816274b-c598-458b-91f2-09392983c99c.png)



Different features and improvements will be added in the future for a better user experience.