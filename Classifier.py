#clasificador
def lista_palabras(texto):
palabras=[]
palabras_tmp=texto.lower().split()

    for p in palabras_tmp:
        if p not palabras an len()>2:
            palabras.append(p)

            return palabras

def entrenar(textos):
    c_palabras={}
    c_categorias={}
    c_textos=0
    c_tot_palabras=0
    #añadir al dicionario de categorias
    for t in textos:
        c_textos=c_textos+1
        if t[1] not in c_categorias:
            c_categorias[t[1]]=1
            else:
                 c_categorias[t[1]]= c_categorias[t[1]]+1

                 
