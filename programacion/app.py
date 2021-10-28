import requests  
from datetime import datetime

######################### 1.-conectarse al enlace ########################################################
def consulta_data():
    url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    response = requests.get(url)
    return response.json()
data = consulta_data()

########################### 2.-obtener numero de respuestas contestadas y no ################################################################
countRespuestaContestada   = 0
countRespuestaNoContestada = 0
for i in  data["items"]:
    respuestaContestada = i["is_answered"]
    if respuestaContestada == True:
        countRespuestaContestada += 1
    else:
        countRespuestaNoContestada += 1
totalDeRegistros = len(data["items"])
############################## 3.-obtener la respuesta de menor número de vistas ##############################################################
listVistas = []
for i in  data["items"]:
    vista = i["view_count"]
    listVistas.append(vista)
listVistas.sort()
cantidadMenorNumVistas = listVistas[0]

for i in  data["items"]:
    vista = i["view_count"]
    if vista == cantidadMenorNumVistas:
        responseMenorVistas = i["link"]
########################### 4.-obtener la respuesta más vieja y más actual ################################################################
listFechas = []
for i in  data["items"]:
    fecha = i["creation_date"]
    fechaTransformada = datetime.utcfromtimestamp(fecha).strftime('%Y-%m-%d')
    listFechas.append(fechaTransformada)   
listFechas.sort()

fechaMasVieja = listFechas[0]
fechaMasActual = listFechas[len(listFechas)-1]
epoch = datetime.strptime(fechaMasVieja, "%Y-%m-%d").timestamp()
print(epoch)
#################### 5.-obtener la respuesta del owner que tenga mayor reputación ######################################################################
listReputaciones = []
for i in  data["items"]:
    reputacion = i["owner"]["reputation"]
    listReputaciones.append(reputacion)
listReputaciones.sort()
mayorReputacion = listReputaciones[len(listReputaciones)-1]

for i in  data["items"]:
    reputacion = i["owner"]["reputation"]
    if reputacion == mayorReputacion:
        responseMayorReputacion = i["link"]
################################# 6.-imprimir del punto 2 al 5 ############################################################

print(f"***El número total de registros es {totalDeRegistros}, de los cuales \n {countRespuestaContestada} fueron contestadas y {countRespuestaNoContestada} no fueron contestadas***")
print(f"***el link de la respuesta con menor numero de vistas es:{responseMenorVistas} \n y tiene una cantidad de {cantidadMenorNumVistas} views***")
print(f"***la fecha de la respuesta más vieja es {fechaMasVieja} y la más actual es de {fechaMasActual}***")
print(f"***la respuesta del owner con mayor reputación está en el link: {responseMayorReputacion}\n dicho owner tiene una reputación de {mayorReputacion}***")





