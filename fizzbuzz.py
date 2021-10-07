'''
FizzBuzz challenge: 
- For multiples of 3 print "Fizz"
- for multiples of 5 print "Buzz"
- If the number is a multiple of 3 and 5 print "FizzBuzz"
'''

class FizzBuzz: 
    def fizz_buzz(self, num):
        if num % 3 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0: 
            print("Buzz")
        

fb = FizzBuzz()
fb.fizz_buzz(3)
fb.fizz_buzz(5)
fb.fizz_buzz(15)
        
