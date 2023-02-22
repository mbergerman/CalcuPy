#Esta clase define un termino

class termino:
	val = 0.0
	ter1 = None
	ter2 = None
	operando = None

	def __init__(self, ter1, operando, ter2 = 0):
		self.ter1 = ter1
		self.ter2 = ter2
		self.operando = operando

	def __float__(self):
		return self.val

	def __str__(self):
		if self.operando == '(':
			return "({})".format(str(self.ter1))
		elif self.operando == '=':
			return str(self.ter1)
		elif self.operando == 'a':
			return 'A'
		else:
			return str(self.ter1) + self.operando + str(self.ter2)

	def operar(self, ans):
		if isinstance(self.ter1, termino):
			self.ter1.operar(ans)
		if isinstance(self.ter2, termino):
			self.ter2.operar(ans)

		if self.operando == '+':
			self.val = float(self.ter1) + float(self.ter2)
		elif self.operando == '-':
			self.val = float(self.ter1) - float(self.ter2)
		elif self.operando == '*':
			self.val = float(self.ter1) * float(self.ter2)
		elif self.operando == '/':
			self.val = float(self.ter1) / float(self.ter2)
		elif self.operando == '^':
			self.val = float(self.ter1) ** float(self.ter2)
		elif self.operando == '(':
			self.val = float(self.ter1)
		elif self.operando == 'a':
			self.val = ans
		else:
			self.val = float(self.ter1)

def parseString(string):
	string = string.replace(" ", "")
	longitud = len(string)

	if string[0] == '(' and string[longitud-1] == ')':
		parentesis = True
		contador = 1
		for i in string[1:-1:-1]:
			if i == ')': contador+=1
			if i == '(': contador-=1
			if contador == 0:
				parentesis = False
				break
		if parentesis:
			return termino(parseString(string[1:-1]), '(')

	ops = ( {'+', '-'} , {'*', '/'} , {'^'} )
	for jer in range(len(ops)):
		i = longitud-1
		while string[i] not in ops[jer] and i>=0:
			if string[i] == ')':
				contador = 1
				while contador>0:
					i-=1
					if string[i] == ')': contador+=1
					if string[i] == '(': contador-=1
			i-=1
		if string[i] in ops[jer]:
			return termino(parseString(string[0:i]), string[i], parseString(string[i+1:]))

	if string == 'A' or string == 'a':
		return termino(0, 'a')
	else:
		return termino(float(string), '=')

def printHelp():
	print("Esto es CalcuPy, una simple calculadora programada en Python")
	print("Los simbolos admitidos son:")
	print("\t+\tsuma")
	print("\t-\tresta")
	print("\t*\tproducto")
	print("\t/\tcociente")
	print("\t^\tpotencia")
	print("\t()\tparéntesis")
	print("\tA\trespuesta anterior")

print("Iniciando CalcuPy...")
print("Ingrese sus calculos:")

ter = None
ans = 0

while True:
	cuenta = input()
	if len(cuenta)<1: break
	if cuenta == 'help':
		printHelp()
		continue

	try:
		ter = parseString(cuenta)
	except:
		print("Error de sintaxis!")
		print("Ingrese 'help' para más información")
		continue

	try:
		ter.operar(ans)
	except:
		print("Error matemático!")
		print("Ingrese 'help' para más información")
		continue

	ans = float(ter)

	print("{} = {}".format(ter, ans))
