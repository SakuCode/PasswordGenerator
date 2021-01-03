import random

#Random Password Generator
#author: Saku Linnankoski
#version: v1.1

#Exepted characters
salpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lalpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']

#Add characters to one list
keys = []
for x in salpha:
	keys.append(x)
for y in lalpha:
	keys.append(y)
for z in num:
	keys.append(z)
	
passwordMin = 8		#Password length minimum
passwordMax = 15	#Password length maximum

generate = True

while generate:		#Run program while True

	def randomPassword():	#Generates the password
		password = ""
		for x in range(random.randint(passwordMin,passwordMax)):
			password += keys[random.randint(0,(len(keys)-1))]
		print("\nRandom Password: ")
		print(password)
	
	randomPassword()
	
	again = input("\nNew password?\n")
	
	while (again != "yes"):
		if (again == "no"):	#Stops program
			generate = False
			break
		again = input("\nNew password?\n")