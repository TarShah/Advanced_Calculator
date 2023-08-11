from stack import Stack
ints = ['0','1','2','3','4','5','6','7','8','9']
class SimpleCalculator:
	def __init__(self):
		self.his = [] 
		pass

	def evaluate_expression(self, input_expression):
		lt = input_expression.replace(" ","")
		ls = []
		i=0
		while i<len(lt):
			if lt[i] in ints:
				st = ""
				while i<len(lt) and lt[i] in ints: 
					st = st + lt[i]
					i+=1
				ls = ls + [st]
			elif lt[i] != " ":
				ls = ls + [lt[i]]
				i+=1
		if len(ls)!=3:
			self.his = [(input_expression,"Error")] + self.his
			return "Error"
		else:
			if ls[1]=='/' and ls[2]=='0':
				self.his = [(input_expression,"Error")] + self.his
				return "Error" 
			if ls[1]=='+':
				self.his = [(input_expression,float(ls[0])+float(ls[2]))] + self.his
				return float(ls[0])+float(ls[2])
			if ls[1]=='/':
				self.his = [(input_expression,float(ls[0])/float(ls[2]))]+ self.his
				return float(ls[0])/float(ls[2])
			if ls[1]=='*':
				self.his = [(input_expression,float(ls[0])*float(ls[2]))] + self.his
				return float(ls[0])*float(ls[2])
			if ls[1]=='-':	
				self.his = [(input_expression,float(ls[0])-float(ls[2]))] + self.his
				return float(ls[0])-float(ls[2])	 
		pass

	def get_history(self):
		return self.his
		pass
		



