import numpy as np



def list_factors(num):
	list = []
	for i in range(1,num+1):
		if num % i == 0:
			list.append(i)
	return list

def equation(x):
	#need to add equation automation
	e = np.poly1d([3,-2,-7,-2])
	value = e(x)
	return value
#get list of factors for each number
p = input("Enter p as positive value: ")
q = input("Enter q as positive value: ")
p_list=list_factors(int(p))
q_list=list_factors(int(q))
#create a list of p/q values used for eval
eval_list = []
for q in q_list:
	for p in p_list:
		if p%q == 0: #evaluate if the fractor results in whole number
			eval_list.append(str(p/q)) #add whole number
		else:
			eval_list.append('%d/%d'%(p,q)) #add fraction

#create negitive variations of factors
for i in range(len(eval_list)):
	factor = eval_list[i]
	eval_list.append('-'+factor)


#remove similar  elements from eval list
eval_list = list(dict.fromkeys(eval_list))
zero_list = []
#add the decimal form of each number for use in euqation
for x in eval_list:
	zero_list.append(eval(x+'.00'))

#loop through 
for i in range(len(zero_list)):
	if equation(zero_list[i]) == 0:
		print eval_list[i]
