def variantes(concentracion):
  if concentracion >=0 and concentracion < 15.5:
    Il= 0
    Ih=50
    BPl= 0
    BPh= 15.4
  elif concentracion >=15.5 and concentracion < 40.5:
    Il= 51
    Ih=100
    BPl= 15.5
    BPh= 40.4
  elif concentracion >=40.5 and concentracion < 65.5:
    Il= 101
    Ih=150
    BPl= 40.5
    BPh= 65.4
  elif concentracion >=65.5 and concentracion < 150.5:
    Il= 151
    Ih=200
    BPl= 65.5
    BPh= 150.4           
  elif concentracion >=150.5 and concentracion < 250.5:
    Il= 201
    Ih=300
    BPl= 150.5
    BPh= 250.4
  elif concentracion >=250.5 and concentracion < 350.5:
    Il= 301
    Ih= 400
    BPl= 250.5
    BPh= 350.4   
  elif concentracion >=350.5 and concentracion < 500.5:
    Il= 401
    Ih= 500
    BPl= 350.5
    BPh= 500.4
  elif concentracion>= 500.5:
    return "error"  
  return Il, Ih, BPl, BPh
def truncar(f, n):
   return ('%.*f' % (n + 1, f))[:-1]
def ICA(Il, Ih, BPl,BPh, concentracion):
  return (Ih-Il)/(BPh-BPl) * (concentracion-BPl)+Il
def colorICA(ICA):
  if ICA >= 0 and ICA < 50:
    color="verde"
  elif ICA >= 50 and  ICA <100:
    color="amarillo"
  elif  ICA >= 100 and  ICA <150:
    color="naranja"
  elif  ICA >= 150 and  ICA <200:
    color="rojo"
  elif ICA >= 200 and  ICA <300:
    color="morado"
  elif  ICA >300:
    color="marron"   
  return color  
contador = 0
color=""
totalICA=0
contVerde=0
contNaranja=0
contAmarillo=0
contMorado=0
contRojo=0
contMarron=0
while color!="verde":
  concentracion = float(input('Ingrese la concentracion de PM en ug/m^3: '))
  contador = 1 + contador
  variables = variantes(concentracion)
  if(variables!="error"):
    ica=ICA(variables[0], variables[1], variables[2], variables[3], concentracion)
    totalICA = totalICA + ica
    color=colorICA(ica)
    if(color=="verde"):
      contVerde= contVerde+1
    elif color=="naranja":
      contNaranja= contNaranja+1
    elif color=="morado":
      contMorado=contMorado+1
    elif color=="rojo":
      contRojo=contRojo+1
    elif color=="amarillo":
      contAmarillo=contAmarillo+1
    elif color=="marron":
      contMarron= contMarron+1        

def porcentajeColor(contadorColor, contador):
  porcentaje=0
  if contadorColor>=1:
   porcentaje=100/contador*contadorColor
  else:
    porcentaje=0
  return porcentaje      

porcentajeVerde= porcentajeColor(contVerde, contador) 
porcentajeNaranja = porcentajeColor(contNaranja, contador) 
porcentajeMorado = porcentajeColor(contMorado, contador) 
porcentajeRojo = porcentajeColor(contRojo, contador)
porcentajeAmarillo = porcentajeColor(contAmarillo, contador)
porcentajeMarron= porcentajeColor(contMarron, contador) 
promedioICA= totalICA/contador
colorPromedio = colorICA(promedioICA) 
print(contador)
print(truncar(promedioICA,2), colorPromedio)
print("verde",truncar(porcentajeVerde,2)+"%")
print("amarillo",truncar(porcentajeAmarillo,2)+"%")
print("naranja",truncar(porcentajeNaranja,2)+"%")
print("rojo",truncar(porcentajeRojo,2)+"%")
print("morado",truncar(porcentajeMorado,2)+"%")
print("marron",truncar(porcentajeMarron,2)+"%")