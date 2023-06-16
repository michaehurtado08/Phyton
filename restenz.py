def ecor1_con_ciclo(seq, enzima):
    resultados = []
    fragmento = seq  
    
    while True:
        corte = fragmento.find(enzima)
        if corte == -1:
            break
        frag1 = fragmento[:corte + len(enzima)]
        frag2 = fragmento[corte + len(enzima):]
        resultados.append(frag1)
        fragmento = frag2
    
    resultados.append(fragmento)
    return ([resultados])