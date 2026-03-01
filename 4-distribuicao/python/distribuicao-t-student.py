import math

# show how the t-curve approaches the standart normal curve as it approaches 30
n=16
while n<40:
	vari = (n-1)/(n-3) # variation in t-distribution
	print("VALOR: " + str(n))
	print("variancia: "+ str(vari))
	print("desvio: "+ str(math.sqrt(vari))) # for n=30 the std is closest to 1 as in the standart normal curve
	print("---------")
	n+=2