from simple_calculator import SimpleCalculator
from stack import Stack
ints = ['0','1','2','3','4','5','6','7','8','9']
oprs = ['+','/','-','*']
def calc(exp):
	i=0
	while i<len(exp):
		if exp[i]=="(":
			b = 1
			j=i+1
			while b>0:
				if exp[j]=='(':
					b+=1
				elif exp[j]==')':
					b-=1
				j+=1
			try:
				exp = exp[0:i] + [str(calc(exp[i+1:j-1]))] + exp[j:] 	 
			except:
				return "Error"
		elif exp[i]=='{':
			b = 1
			j=i+1
			while b>0:
				if exp[j]=='{':
					b+=1
				elif exp[j]=="}":
					b-=1
				j+=1
			try:	
				exp = exp[0:i] + [str(calc(exp[i+1:j-1]))] + exp[j:]
			except:
				return "Error"
		i+=1
	
	i=1
	while i < len(exp):
		if exp[i]=='*':
			try:
				exp = exp[0:i-1] + [str(float(exp[i-1])*float(exp[i+1]))] + exp[i+2:]
			except:
				return "Error"
		elif exp[i]=='/':
			try:
				exp = exp[0:i-1] + [str(float(exp[i-1])/float(exp[i+1]))] + exp[i+2:]	
			except:
				return "Error"
		else:
			i+=1
	i=1
	while i < len(exp):
		if exp[i]=='+':
			try:
				exp = exp[0:i-1] + [str(float(exp[i-1])+float(exp[i+1]))] + exp[i+2:]
			except:
				return "Error"
		elif exp[i]=='-':
			try:
				exp = exp[0:i-1] + [str(float(exp[i-1])-float(exp[i+1]))] + exp[i+2:]
			except:
				return "Error"
		else:
			i+=1
	if len(exp)!=1:
		return "Error"
	try:
		return float(exp[0]) 
	except:
		return "Error"
		
class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		self.his = []
		pass

	def evaluate_expression(self, input_expression):
		if self.check_brackets(self.tokenize(input_expression)) == False:
			self.his = [(input_expression,"Error")] + self.his
			return "Error"
		else:
			ls = self.tokenize(input_expression)
			for i in range(len(ls)-1):
				if ls[i]=='/' and ls[i+1]=='0':
					self.his = [(input_expression,"Error")] + self.his
					return "Error" 
			self.his = [(input_expression,calc(ls))] + self.his 
			return calc(ls)
		pass

	def tokenize(self, input_expression):
		ls = []
		lt = input_expression
		i=0
		while i<len(lt):
			if lt[i] in ints:
				st = ""
				while i<len(lt) and lt[i] in ints: 
					st = st + lt[i]
					i+=1
				ls = ls + [float(st)]
			else:
				if lt[i] != " ":
					ls = ls + [lt[i]]
				i+=1
		return ls
		pass		

	def check_brackets(self, list_tokens):
		lb=0
		sb=0
		for i in list_tokens:
			if i=='{':
				lb+=1
			if i=='}':
				lb-=1
			if i=='(':
				sb+=1
			if i==')':
				sb-=1
			if sb>0 and i=='{':
				return False
			if sb<0 or lb<0:
				return False	
		if sb!=0 or lb!=0:
			return False
		return True
		pass

	def evaluate_list_tokens(self, list_tokens):
		if self.check_brackets(list_tokens) == False:
			self.his = [(list_tokens,"Error")] + self.his
			return "Error"
		else:
			for i in range(len(list_tokens)-1):
				if list_tokens[i]=='/' and list_tokens[i+1]=='0':
					self.his = [(list_tokens,"Error")] + self.his
					return "Error"
			self.his = [(list_tokens,calc(list_tokens))] + self.his
			return calc(list_tokens)
		pass

	def get_history(self):
		return self.his
		pass
		
		
		
		
		
