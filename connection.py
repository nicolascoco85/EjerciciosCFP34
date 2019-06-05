import sqlite3

bd = sqlite3.connect("libros.db")

cursor = bd.cursor()

tablas = [
    """
		CREATE TABLE IF NOT EXISTS libros(
			autor TEXT NOT NULL,
			genero TEXT NOT NULL,
			precio REAL NOT NULL,
			titulo REAL NOT NULL
		);
	"""
]
for tabla in tablas:
    cursor.execute(tabla);

autor = input("\nAutor: ")
genero = input("\nGénero: ")
precio = float(input("\nPrecio: "))
titulo = input("\nTítulo: ")

sentencia = "INSERT INTO libros(autor, genero, precio, titulo) VALUES (?,?,?,?)"

cursor.execute(sentencia, [autor, genero, precio, titulo])

bd.commit()

bd.close()
