import mysql.connector
import random
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="importada"
)

mycursor = mydb.cursor()

incidencias_arr = ["A","R","I","E","V","F"]
mes = 1
dia = 1

print("Creando incidencias en la base de datos...")

for i in range(500):
  for j in range(365):
    if mes == 1 and dia == 32:
      mes+=1
      dia=1
    if mes == 2 and dia == 29:
      dia=1
      mes+=1
    if mes == 3 and dia == 32:
      dia=1
      mes+=1
    if mes == 4 and dia == 31:
      dia=1
      mes+=1
    if mes == 5 and dia == 32:
      dia=1
      mes+=1
    if mes == 6 and dia == 31:
      dia=1
      mes+=1
    if mes == 7 and dia == 32:
      dia=1
      mes+=1
    if mes == 8 and dia == 32:
      dia=1
      mes+=1
    if mes == 9 and dia == 31:
      dia=1
      mes+=1
    if mes == 10 and dia == 32:
      dia=1
      mes+=1
    if mes == 11 and dia == 31:
      dia=1
      mes+=1
    if mes == 12 and dia == 32:
      dia=1
      mes=1
      j=365
    sql = "INSERT INTO incidencias (fecha, empleado_id, incidencia) VALUES (%s, %s, %s)"
    val = ((f"2018-{mes}-{dia}"), (i+1), incidencias_arr[random.randint(0, 5)])
    mycursor.execute(sql, val)
    mydb.commit()
    dia+=1
    print(f"Empleado numero: {i+1} e incidencia numero: {j+1}")

print("Se ingresarón correctamente 365 incidencias por los 1,000 empleados")