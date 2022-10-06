from conversor import *
print("CONVERSOR")
x=int(input("para transformar centimetros em polegadas digite 1, caso seja o inverso digite 2: "))
y=float(input("digite o valor para conversão: "))
conversionador(y,x)
#o python não arredonda os numeros por isso as vezes ele pode dar um numero aproximado ex: 3.6 pol = 9.23 cm
#mas o certo seria 3.6 pol = 10cm arredondando o valor