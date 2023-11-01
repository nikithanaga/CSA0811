import math 
class TechNo :
	def isTechNo(self, number) :
		length = 0
		temp = number
		lhs = 0
		rhs = 0
		result = 0
	
		while (temp != 0) :
			temp = int(temp / 10)
			length += 1
		
		if ((length % 2) == 0) :
			lhs = int(number / ((10 ** int(length / 2))))
			rhs = number % ((10 ** int(length / 2)))
			if (((lhs + rhs) * (lhs + rhs)) == number) :
				result = 1
		if (result == 1) :
			print(" ", number ," is tech number")
		else :
			print(" ", number ," is not tech number")
def main() :
	task = TechNo()
	task.isTechNo(3025)
	

if __name__ == "__main__": main()

