

#clasificador
def lista_palabras(texto):
    palabras=[]
    palabras_tmp=texto.lower().split()
    #print ("palabras_tmp= " + str(palabras_tmp))
    for p in palabras_tmp:
        #print ("p= " + str(p))
        if p not in palabras and len(p)>2:
            palabras.append(p)
            #print ("palabras= " + str(palabras))
            
    return palabras

def entrenar(textos):
  c_palabras={}
  c_categorias={}
  c_textos=0
  c_tot_palabras=0
  #anadir al dicionario de categorias
  for t in textos:
    c_textos=c_textos+1
    #print ("c_textos= " + str(c_textos))
    if t[1] not in c_categorias:
      c_categorias[t[1]]=1
    else:
      c_categorias[t[1]]=c_categorias[t[1]]+1
      #print ("c_categorias= " + str(c_categorias))


  #anadir palabras al vocabulario
  for t in textos:
    palabras=lista_palabras(t[0])
    for p in palabras:
      if p not in c_palabras:
        c_tot_palabras=c_tot_palabras+1
        c_palabras[p]={}
        for c in c_categorias:
   
          c_palabras[p][c]=0
       
      c_palabras[p][t[1]]=c_palabras[p][t[1]]+1
      
    #if c_palabras[p][t[1]]>1000:
     # print ("Palabra: " + str(p) +" Cantidad:"+ str(c_palabras[p][t[1]]))

  return (c_palabras,c_categorias,c_textos,c_tot_palabras)

def clasificar(texto,c_palabras,c_categorias,c_textos,
c_tot_palabras):
  categoria=""
  prob_categoria=0
  for c in c_categorias:
   #probabilidad de la categoria
   prob_c=float(c_categorias[c])/float(c_textos)
   #print ("probabilidad de la categoria= " + str(prob_c))
   palabras=lista_palabras(texto)
   #print ("palabras= " + str(palabras))
   prob_total_c=prob_c
   for p in palabras:
     #print ("palabra:" + str(p))
     # probabilidad de la palabra
     if p in c_palabras:
       prob_p=float(c_palabras[p][c])/float(c_tot_palabras)
       #print ("p: " + str(p))
       #print ("c_palabras[p][c]: " + str(c_palabras[p][c]))
       #print ("c_tot_palabras: " + str(c_tot_palabras))
       # print ("probabilidad p(palabra|categoria): " + str(prob_p))
       # probabilidad p(categoria|palabra)
       prob_cond=prob_p/prob_c
       # print ("probabilidad p(categoria|palabra): " + str(prob_cond))
       # probabilidad p(palabra|categoria)
       prob=(prob_cond*prob_p)/prob_c
       # print ("probabilidad p(palabra|categoria): " + str(prob))
       prob_total_c=prob_total_c*prob
       #print ("prob_total_c: " + str(prob_total_c))

   if prob_categoria <prob_total_c:
     categoria=c
     #print ("categoria: " + str(categoria))
     prob_categoria=prob_total_c
     #print ("prob_categoria: " + str(prob_categoria))
  return (categoria,1-prob_categoria)

def loadfile():
  textos=[]
  file1 = open('intrusion.txt', 'r') 
  Lines = file1.readlines()  
  for line in Lines: 
      intrusion = [line.strip(), 'Sqlinjection']
      textos.append(intrusion)
  file2 = open('bueno', 'r') 
  Lines = file2.readlines()  
  for line in Lines: 
      intrusion = [line.strip(), 'NOTSqlinjection']
      textos.append(intrusion)

  return textos

if __name__ == "__main__":
  texto=loadfile()
   #c_palabras,c_categorias,c_textos,c_tot_palabras
#print ("c_palabras= " + str(p))

p,c,t,tp = entrenar(texto) 
print ("c_categorias=  " + str(c))
print ("c_textos=  " + str(t))
print ("c_tot_palabras=  " + str(tp))
clase=clasificar("GET http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1,pass,cc FROM users WHERE uname='test' HTTP/1.1 Host: testphp.vulnweb.com",p,c,t,tp)
print ("texto clasificado: " + str(clase))