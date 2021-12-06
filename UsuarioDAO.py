from Usuario import Usuario
from Conexion import Conexion

class UsuarioDAO:
    _INSERTAR = "INSERT INTO usuarios(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuarios SET username=%s, password=%s WHERE id_usuario = %s"
    _SELECCIONAR = "SELECT id_usuario FROM usuarios WHERE username=%s AND password=%s"
    _ELIMINAR = "DELETE FROM usuarios WHERE id_usuario=%s"

    @classmethod
    def registrar(cls, usuario):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.username, usuario.password)

                #Comprobacion de si el usuario y contraseña ya existen
                cursor.execute(cls._SELECCIONAR, valores)
                comprobacion = cursor.fetchone()
                if comprobacion:
                    #Ya existe el usuario y contraseña
                    # print("Ya existe el usuario")
                    return 0
                else:
                    #No existe el usuario ni la contraseña
                    # print("No existe el usuario")
                    cursor.execute(cls._INSERTAR, valores)
                    return cursor.rowcount

    @classmethod
    def iniciar_sesion(cls, usuario):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.username, usuario.password)

                # Comprobacion de si el usuario y contraseña existen
                cursor.execute(cls._SELECCIONAR, valores)
                comprobacion = cursor.fetchone()
                if comprobacion:
                    # Existe el usuario y contraseña
                    # print("Existe el usuario")
                    return 1
                else:
                    # No existe el usuario ni la contraseña
                    # print("No existe el usuario")
                    return 0

    @classmethod
    def actualizar(cls, usuario):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                return cursor.rowcount


    @classmethod
    def eliminar(cls, usuario):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._SELECCIONAR, valores)
                comprobacion = cursor.fetchone()
                # print(comprobacion)
                if comprobacion:
                    # Existe el usuario y contraseña
                    # print("Existe el usuario")
                    cursor.execute(cls._ELIMINAR, (comprobacion, ))
                    return cursor.rowcount
                else:
                    # No existe el usuario
                    # print("No existe el usuario")
                    return 0


# if __name__ == "__main__":
    # Registrar usuario
    # usuario = Usuario(username="jorge", password="jorgesito")
    # registrados = UsuarioDAO.registrar(usuario)
    # print(registrados)

    # Actualizar usuario
    # usuario = Usuario(3, "jomalo", "xdlol")
    # actualizados = UsuarioDAO.actualizar(usuario)
    # print(actualizados)

    # Iniciar sesion
    # usuario = Usuario(username="Danteps", password="123456danteps")
    # inicio = UsuarioDAO.iniciar_sesion(usuario)
    # print(inicio)

    #Eliminar usuario
    # usuario = Usuario(username="jorge", password="jorgesito")
    # eliminados = UsuarioDAO.eliminar(usuario)
    # print(eliminados)