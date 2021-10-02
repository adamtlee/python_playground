class Calculator:
    def add_nums(self, n1, n2):
        sum_result = n1 + n2
        print("The sum is: ", sum_result)
    
    def sub_nums(self, n1, n2):
        difference_result = n1 - n2
        print("The difference is: ", difference_result)
    
    def div_nums(self, n1, n2):
        quotient_result = n1 / n2
        print("The quotient is: ", quotient_result)
    
    def mul_nums(self, n1, n2):
        product_result = n1 * n2
        print("The product is: ", product_result)

c1 = Calculator()
c1.add_nums(4, 2)
c1.sub_nums(4, 2)
c1.div_nums(4, 2)
c1.mul_nums(4, 2)

