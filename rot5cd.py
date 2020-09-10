def rot5c(mensaje):
    letras=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    MensajeLista = mensaje.split(" ")
    MensajeEncriptado=[]
    for Palabra in MensajeLista:
        PalabraAuxiliar=''
        for Letra in range(0,len(Palabra)):
            if Palabra[Letra].isalpha() == False:
                    PalabraAuxiliar+=Palabra[Letra]
            for Comparador in range(0,len(letras)):
                if Palabra[Letra].islower() == True:
                    if Palabra[Letra] == letras[Comparador]:
                        if (Comparador + 5) >= len(letras):
                            aux = len(letras)- Comparador
                            aux2 = 5 - aux 
                            PalabraAuxiliar+=letras[aux2]
                        else:
                            PalabraAuxiliar+=letras[Comparador + 5]
                else:
                    if Palabra[Letra].lower() == letras[Comparador]:
                        if (Comparador + 5) >= len(letras):
                            aux = len(letras)- Comparador
                            aux2 = 5 - aux 
                            PalabraAuxiliar+=letras[aux2].upper()
                        else:
                            PalabraAuxiliar+=letras[Comparador + 5].upper()
        MensajeEncriptado.append(PalabraAuxiliar)
    FraseEncriptada = " ".join(MensajeEncriptado)
    return FraseEncriptada       

def rot5d(mensaje):
    letras=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    MensajeLista = mensaje.split(" ")
    MensajeEncriptado=[]
    for Palabra in MensajeLista:
        PalabraAuxiliar=''
        for Letra in range(0,len(Palabra)):
            if Palabra[Letra].isalpha() == False:
                    PalabraAuxiliar+=Palabra[Letra]
            for Comparador in range(0,len(letras)):
                if Palabra[Letra].islower() == True:
                    if Palabra[Letra] == letras[Comparador]: 
                        if (Comparador - 5) < 0:
                            aux = (Comparador - 5) * -1 
                            PalabraAuxiliar+=letras[len(letras)-aux]
                        else:
                            PalabraAuxiliar+=letras[Comparador - 5]
                else:
                    if Palabra[Letra].lower() == letras[Comparador]: 
                        if (Comparador - 5) <= 0:
                            aux = (Comparador - 5) * -1 
                            PalabraAuxiliar+=letras[aux]
                        else:
                            PalabraAuxiliar+=letras[Comparador - 5].upper()
        MensajeEncriptado.append(PalabraAuxiliar)
    FraseEncriptada = " ".join(MensajeEncriptado)
    return FraseEncriptada
