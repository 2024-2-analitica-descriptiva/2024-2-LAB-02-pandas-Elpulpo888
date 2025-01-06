"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import  pandas as pd 

tbl0= pd.read_csv("files/input/tbl0.tsv", sep= "\t")
tbl1= pd.read_csv("files/input/tbl1.tsv", sep= "\t")
tbl2= pd.read_csv("files/input/tbl2.tsv", sep= "\t")


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    list0= sorted(list(tbl1["c4"].unique()))
    list0 = [i.upper() for i in list0]
    return list0