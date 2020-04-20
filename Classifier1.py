#clasificador
def lista_palabras(texto):
    palabras=[]
    palabras_tmp=texto.lower().split()

    for p in palabras_tmp:
        if p not in palabras and len(p)>2:
            palabras.append(p)

            return palabras



def casificar(texto,c_palabras,c_categorias,c_textos,c_tot_palabras):
    categoria=""
    prob_categoria=0
    for c in c_categorias:
        #probabilidad de la categoria
        prob_categoria=float(c_categorias[c])/float(c_textos)
        palabras=lista_palabras(texto)
        prob_total_c=prob_c
        for p in palabras:
            # probabilidad de la palabra
            if p in c_palabras:
                 prob_p=float(c_palabras[p][c])/float(c_tot_palabras)
                 # probabilidad p(categoria|palabra)
                 prob_cond=prob_p/prob_c
                 # probabilidad p(palabra|categoria)
                 prob=(prob_cond*prob_p)/prob_c
                 prob_total_c=prob_total_c*prob

    if prob_categoria <prob_total_c:
        categoria=c
        prob_categoria=prob_total_c

        return(categoria,prob_categoria)

        if __name__ == "__main__":
            textos={
                ["viadra a buen precio","spam"],
            ["quedamos manana lunues ir a cine","nospam"],
             ["replicas de relojes y viagra a presions de riza","spam"],
              ["disponga de sus productos farmaceuticos en 24 horas","spam"],
               ["La inteligencia artificial es una disciplina muy interesante","nospam"],
            }
        clase=str(lista_palabras(textos))

#p,c,t,tp = entrenar(textos)
#clase=clasificar("pedidos online de viagra servicios en 24 horas",p,c,t,tp)
         print "texto clasificado"