g=input("opcion= Hombre(H)-Mujer(M):")
n=input("Introduzca DNI:")

opcion=["20","27","23"]
cuil=0
def calculo_cuil(gen,doc):
       if gen=="H":
       		cuil=int(opcion[0][0])*5+int(opcion[0][1])*4+int(doc[0])*3+int(doc[1])*2+int(doc[2])*7+int(doc[3])*6+int(doc[4])*5+int(doc[5])*4+int(doc[6])*3+(int(doc[7])*2)
        	cuil=11-(cuil%11)
       #return cuil
       print(int(opcion[0]),"-",int(doc),"-",cuil)
       if cuil>9:
       		cuil=int(opcion[2][0])*5+int(opcion[2][1])*4+int(doc[0])*3+int(doc[1])*2+int(doc[2])*7+int(doc[3])*6+int(doc[4])*5+int(doc[5])*4+int(doc[6])*3+(int(doc[7])*2)
        	cuil=11-(cuil%11)
       #return cuil
       		print(int(opcion[2]),"-",int(doc),"-",cuil)
       elif gen=="M":
       		cuil=int(opcion[1][0])*5+int(opcion[1][1])*4+int(doc[0])*3+int(doc[1])*2+int(doc[2])*7+int(doc[3])*6+int(doc[4])*5+int(doc[5])*4+int(doc[6])*3+(int(doc[7])*2)
        	cuil=11-(cuil%11)
       #return cuil
       print(int(opcion[1]),"-",int(doc),"-",cuil)
       if cuil>9:
       		cuil=int(opcion[0][0])*5+int(opcion[0][1])*4+int(doc[0])*3+int(doc[1])*2+int(doc[2])*7+int(doc[3])*6+int(doc[4])*5+int(doc[5])*4+int(doc[6])*3+(int(doc[7])*2)
        	cuil=11-(cuil%11)
       #return cuil
       		print(int(opcion[2]),"-",doc,"-",cuil)



calculo_cuil(g,n)

		