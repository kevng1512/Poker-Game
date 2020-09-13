def evaluate(hand):
    cards = hand
    count = 1
    count1 = 1

    for i in range (0, 10, 2):      #this part check for how many pairs or none in the deck by comparing the even indexes
        for j in range (0, 10, 2):
            if (ord(cards[i]) == ord(cards[j])): 
                count += 1 

    for i in range (1, 10, 2):      #this part check if it's flush by comparing the odd indexes
        for j in range (1, 10, 2):
            if (ord(cards[i]) == ord(cards[j])): 
                count1 += 1 

    if (count == 18):                    #this part return the answer for each case counted
        return 'four of a kind'
    elif (count == 14):
        return 'full house'
    elif (count1 == 26):
        return 'flush'
    elif (count == 12):
        return 'three of a kind'
    elif (count == 8):
        return 'pair'
    else:                           #this part check for the highest card by using the ASCII table
        temp = 0
        jqk = 0
        for i in range (0, 10, 2):
            if (ord(cards[i]) == 65):   #this is a special case for A since it have different rank in poker comparing to alphabetically
                return 'A high'
            elif (ord(cards[i]) > temp and ord(cards[i]) != 84):        #this is a special case for 10 since it is called as 'T' which have different  rank in alphabetical order comparing to the it's rank in poker
                temp = ord(cards[i])

            if (cards[i] == 'J' or cards[i] == 'Q' or cards[i] == 'K'):         #this count how many cards higher than 10 and smaller than A
                jqk = 1
        
        if (jqk == 1):              #this part return the highest rank even if there are 10 in the deck 
            return chr(temp) + ' high'
        else:
            return '10 high'        #this part return 10 if 10 is the highest value in the deck

import unittest                                         #check if the code work
class test(unittest.TestCase):
    def testFourOfaKind1(self):
        self.assertTrue(evaluate('KsKhKc8sKd'))
    def testFourOfaKind2(self):
        self.assertTrue(evaluate('2c3h2d2d2s'))
    def testFourOfaKind3(self):
        self.assertTrue(evaluate('Jh6CJsJdJs'))
    def testFourOfaKind4(self):
        self.assertTrue(evaluate('8h8c8sAs8d'))
    def testFullHouse1(self):
        self.assertTrue(evaluate('2hAs2cAd2s'))
    def testFullHouse2(self):
        self.assertTrue(evaluate('1h7c7d7s1s'))
    def testFullHouse3(self):
        self.assertTrue(evaluate('As2h2cAd2s'))
    def testFullHouse4(self):
        self.assertTrue(evaluate('2h2cAsAd2s'))
    def testFlush1(self):
        self.assertTrue(evaluate('3s4s5s6sAs'))
    def testFlush2(self):
        self.assertTrue(evaluate('4h7hKhAhJh'))
    def testFlush3(self):
        self.assertTrue(evaluate('7d2d9dAd3d'))
    def testFlush4(self):
        self.assertTrue(evaluate('9c4c6cQcJc'))
    def testThreeOfaKind1(self):
        self.assertTrue(evaluate('2sKd2c2dAs'))
    def testThreeOfaKind2(self):
        self.assertTrue(evaluate('2sKdAc2c2d'))
    def testThreeOfaKind3(self):
        self.assertTrue(evaluate('2sKd2cAc2d'))
    def testThreeOfaKind4(self):
        self.assertTrue(evaluate('Kd2s2cAs2d'))
    def testPair1(self):
        self.assertTrue(evaluate('2sTcKdAs2h'))
    def testPair2(self):
        self.assertTrue(evaluate('Ac2hTc2sKd'))
    def testPair3(self):
        self.assertTrue(evaluate('AcTc2s2hKd'))
    def testPair4(self):
        self.assertTrue(evaluate('Kd2s2cTsAs'))
    def testHigh1(self):
        self.assertTrue(evaluate('2s8hThQs9d')) #q high
    def testHigh2(self):
        self.assertTrue(evaluate('7c8d3s4cKd')) #k high
    def testHigh3(self):
        self.assertTrue(evaluate('AcTc2hQsKd')) #a high
    def testHigh4(self):
        self.assertTrue(evaluate('Jc7s9dTc3h')) #j high
    def testHigh5(self):
        self.assertTrue(evaluate('5cTc2h4d7s')) #10 high

if __name__ == '__main__':
    unittest.main(exit=False)