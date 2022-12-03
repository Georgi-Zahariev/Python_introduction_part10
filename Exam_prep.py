#1
def create_botton(dim, val):
	final_list = []
	current_list = []
	for i in range(1,dim+1):
		for j in range(1,i+1):
			current_list.append(val)
		final_list.append(current_list)
		current_list = []
	return final_list

#2	
def sum_even(xs):
	num_sum = 0
	for i in range(1,len(xs)):
		for j in range(1,len(xs[i])):
			if xs[i][j]%2 == 0:
				num_sum+= xs[i][j]			
	return num_sum

#3	
def pos_summation(xs):
	num_sum = 0
	for i in range(0,len(xs)-1):
		for j in range(0,len(xs[i])-1):
			if xs[i][j]< 10:
				num_sum+= xs[i][j]			
	return num_sum

#4
def total_neg(xs):
	num_sum = 0
	for i in range(0,len(xs)-1):
		for j in range(1,len(xs[i])):
			if xs[i][j]< 0 and xs[i][j]>-100:
				num_sum+= xs[i][j]			
	return num_sum
	
#5
def check_flour(customers, flour_amt):
	bake_min = customers * 2 * 3
	if customers > 50 :
		bake_max = (customers - 50)//10 + bake_min	
		if bake_max <= flour_amt:
			return "bake the max"
		elif bake_min <= flour_amt:
			return "bake the min"
		else:
			return "not enough"
	else:
		if bake_min <= flour_amt:
			return "bake the max"
		else:
			return "not enough"

#6
def remove_evens(xs):
	dct = {}
	for i in range(len(xs)):
		if xs[i] in dct:
			dct[xs[i]] = dct[xs[i]] + 1
		else:
			dct[xs[i]] = 1
	new_lst =[]
	for j,k in dct.items():
		if k%2 ==1:
			new_lst.append(j)
	temp = []	
	for el in xs:
		if el  in new_lst:
			temp.append(el)
	xs.clear()
	
	for el2 in temp:
		xs.append(el2)
	
	
#7
def average_grade(grades, student):
	dct_sum = 0
	if student not in grades:
		return "False"
	else:
		temp = grades[student]
		for i in temp.values():
			dct_sum += i
	return round(dct_sum/len(temp),2)
	
#8
def missing_chars(filename, chars):
	file = open(filename)
	string = file.read()
	string = string.replace(" ","")
	cnt = 0
	
	for i in range(len(string)):
		if string[i] not in chars:
			cnt+=1
			
	return cnt
	
#9
def pattern2file(filename, dim, char1, char2):
	new_file = open(filename, "w")
	str_len = 1
	for i in range(dim):
		str_len += str_len
	file_str=""
	temp_len=1
	for i in range(dim):
		for i in range(temp_len):
			file_str += char1
		for i in range(str_len - temp_len):
			file_str += char2
		new_file.write(file_str + "\n")
		file_str = ""
		temp_len += temp_len
	new_file.close()
	
#10
def counter(xs):
	if len(xs) == 0:
		return 0
	elif len(xs) == 1:
		if xs[0]==0:
			return 1
		else:
			return 0
	else:
		if xs[0] == 0:
			return 1 + counter(xs[1:])
		else:
			return counter(xs[1:])
			
#11
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	
	def __str__(self):
		return f'Make: {self.make}, Model: {self.model}, Year: {self.year}'
	
	def __eq__(self, other):
		if (self.make == other.make and self.model == other.model and self.year == other.year):
			return True
		else:
			return False
#12
def sum_list(filename):
	try:
		int_sum = 0
		file = open(filename)
		lst = file.readlines()
		
		for i in range(len(lst)):
			integer = int(lst[i].strip())
			int_sum += integer
		return int_sum
	except ValueError:
		return "Wrong value"
	except FileNotFoundError:
		return "File does not exists"
		

	
	

		
		
		 
	
































