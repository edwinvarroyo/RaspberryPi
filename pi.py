from random import randint
salida= False
entrada= False
while entrada==False:
	pregunta= input();
	if pregunta == "charly charly ar iu jir?":
		res= randint(0,1)
		if res==1 :
			print ("si")
			entrada=True	
while salida==False:
	pregunta= input();
	res= randint(0,1)
	if res==0 :
		print ("no")
	if res==1 :
		print ("si")
	if pregunta == "Puedo salir?":
		if res==1:
			salida=True