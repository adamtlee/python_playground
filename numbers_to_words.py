'''
convert a given number to a word
ex. 1 = "one", 2 = "two", etc..
'''

class NumToWord: 
    def num_to_word_v1(self, num):
        num_to_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 
            90: 'Ninety', 0: 'Zero'}

        try:
            print(num_to_words[num])
        except KeyError:
            print("Number is out of range")
            

n2w = NumToWord()
n2w.num_to_word(2)
n2w.num_to_word(50)