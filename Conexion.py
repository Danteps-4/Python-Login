import psycopg2 as bd
import sys

class Conexion():
    _DB = "khokdvpo"
    _USERNAME = "khokdvpo"
    _HOST = "kesavan.db.elephantsql.com"
    _PASSWORD = "OVQpLp83Mrs5KbKn1bltCzWZTvXLyK_n"
    _PORT = "5432"
    _conexion = None

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


if __name__ == "__main__":
    Conexion.obtener_conexion()
