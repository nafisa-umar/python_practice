class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        
        try:
            card_num = [int(num) for num in list(self.card_num.replace(" ", ""))]
        except:
            return False

        no_digits = len(card_num)
        
        if no_digits > 1:
            if no_digits % 2 == 0:
                indexes_to_double = range(0, no_digits, 2)
            else:
                indexes_to_double = range(1, no_digits, 2)
            
            for i in indexes_to_double:
                card_num[i] = (card_num[i] * 2) if (card_num[i] * 2 <= 9) else (card_num[i] * 2 - 9)
            
            if sum(card_num) % 10 == 0:
                return True
            return False
            
        return False
            

