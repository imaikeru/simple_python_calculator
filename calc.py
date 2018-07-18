OPERATORS = ['+','-','/','*']
MULT_OP = '*'
SUBT_OP = '-'
DIV_OP = '/'
ADD_OP = '+'

def op_plus(a,b):
	return a+b

def op_minus(a,b):
	return a-b

def op_multiply(a,b):
	return a*b

def op_divide(a,b):
 	return a/b

def parse_input(myinput):
	parsed = []
	tmp = ''

	while ' ' in myinput:
		myinput = myinput.replace(' ','')

	for c in myinput:
		if c in OPERATORS: # TODO FIX LATER
			if tmp != '':
				parsed.append(tmp)
				tmp=c
				parsed.append(tmp)
				tmp=''
			else:
				tmp+=c
				parsed.append(tmp)
				tmp=''
		else:
			tmp += c

	if tmp != '':
		parsed.append(tmp)

	for index,element in enumerate(parsed):
		if element not in OPERATORS:
			parsed[index] = float(element)

	return parsed

def calc_multipl_div(array):

	if MULT_OP not in array and DIV_OP not in array:
		raise ValueError('No multiplication or division operators')
	for index,element in enumerate(array):
		if element in (MULT_OP,DIV_OP):
			break
	
	start = index - 1
	number = array[start]
	end = start
	count = 0

	for index in range(start+1,len(array)-1):
		if array[index] in (SUBT_OP,ADD_OP): 
			break
		elif array[index] == MULT_OP:
			tmp = array[index+1]
			count+=1
			number=op_multiply(number,tmp)
		elif array[index] == DIV_OP:
			tmp=array[index+1]
			count+=1
			number=op_divide(number,tmp)
	end+=count*2

	return start, end, number

def remove_multiplication_division(parsed):
	for index in range(len(parsed)):
		try:
			start,end,num = calc_multipl_div(parsed)
		except ValueError:
			# print('No multiplication or division operators')
			break
		parsed = parsed[:start] + [num] + parsed[end+1:]
	return parsed

def calculate_sum_dif(parsed): # - 3 + 4	
	if not parsed:
		return 0
	
	if parsed[0] == SUBT_OP:
		parsed[0]=-parsed[1]
		del parsed[1]
	
	result = parsed[0]
	
	for k in range(1,len(parsed) - 1):
		if parsed[k] == '+':
			result = op_plus(result,parsed[k+1])
		elif parsed[k] == '-':
			result = op_minus(result,parsed[k+1])
	return result

print('Enter number -> operation -> number .. and so on.')
print('Operations to choose from:',OPERATORS)
parsed = parse_input(input())
parsed = remove_multiplication_division(parsed)
print('Result =',calculate_sum_dif(parsed))