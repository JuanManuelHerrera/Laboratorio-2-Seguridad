#Juan Manuel Herrera
#Lab 2 Seguridad Informática
import rot5cd as r
import hashlib as h
Entrada = open("mensajedeentrada.txt",'r')
Mensaje = Entrada.readline().replace('\n','')
Entrada.close()
Hash = h.sha1(Mensaje.encode('utf-8'))
Hash1=Hash.hexdigest()

#Main#
print("Bienvenido \nSeleccione (1) para Codificar el Mensaje \nSeleccione (2) para Decodificar el mensaje y verificar la integridad\nSeleccione (0) para finalizar")
a = 1
while a!= 0:
    a = int(input("Seleccione la opción a realizar: "))
    if a == 1:
        MensajeCodificado = r.rot5c(Mensaje)
        Salida = open("Mensajeseguro.txt","w")
        Salida.write(MensajeCodificado)
        Salida.close()
        print("Su mensaje ha sido codificado")
    elif a == 2:
        try:
            Fichero = open("Mensajeseguro.txt","r")
        except:
            print("No existe un fichero con un mensaje codificado")
            break
        MensajeFichero=Fichero.readline().replace('\n','')
        if MensajeFichero == '':
            print("No existe un mensaje codificado dentro de este fichero")
        else:
            Decodificar = r.rot5d(MensajeFichero)
            print("El mensaje decodificado es: ",Decodificar)
            HashD = h.sha1(Decodificar.encode('utf-8'))
            HashDecodificado = HashD.hexdigest()
            if Hash1 == HashDecodificado:
                print("El mensaje no ha sido intervenido")
            else:
                print("El mensaje ha sido intervenido *CUIDADO*")

    elif a == 0:
        print("\nGracias por utilizar este programa")
    
