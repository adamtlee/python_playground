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

    def num_to_word_v2(self, num):
        less_than_20 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        less_than_100 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()

        def words(num):
            if num == 0:
                return []
            elif num < 20:
                return [ less_than_20[num-1] ]
            elif num < 100:
                return [ less_than_100[(num//10)-2] ] + words(num%10)
            elif num < 1000:
                return [ less_than_20[(num//100)-1] ] + ["Hundred"] + words(num%100)
            else:
                for i, p in enumerate("Thousand Million Billion".split(), 1):
                    if num < 1000 ** (i+1):
                        return words(num//1000**i) + [p] + words(num%1000**i)

        print(" ".join(words(num)) or "Zero")
        return " ".join(words(num)) or "Zero"



n2w = NumToWord()
n2w.num_to_word_v1(2)
n2w.num_to_word_v1(50)

n2w.num_to_word_v2(167)