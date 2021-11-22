#ex 2 : 20 minutes

import random

# import unittest

def lottery_game():
    """
    The function will create a lottery draw of 10 balls out of 50 (in a range from 1 to 50) 
    The output list is in ascending order.

    """

    lottery_list = random.sample(range(1,51), 10)
    lottery_list.sort()

    return lottery_list

print('The lottery result is : ', lottery_game())

################################################################################

# To test the output of my function I could implement a unit test to test that :
# - I do have a list in output
# - Check that each element of the list is an int
# - The length of the output list is 10
# - The list is ordered
# - There aren't any duplicates in the list
# - Each element of the list is between 1 and 50

###############################################################################

# class TestLotteryGame(unittest.TestCase):
#      """
#       Classe de test permettant de valider le bon fonctionnement de lottery_game

#      """

#      def test_lottery_game(self):
#          """
#          This function checks that we have in output a list of 10 elements, all different and ordered (asc)      

#          """
#          res = lottery_game()

#          list_range = [k for k in range(1,51)]

#          self.assertIsInstance(res,list) #check that we have a list in output
#          self.assertEqual(len(lottery_game()), 10) #check that the length of the list is 10
#          for i in range(0, len(res)) :
#             number = res[i]
#             self.assertIsInstance(number,int) #check that the elements are integer
#             self.assertIn(number,list_range) #check that each element is between 0 and 50
#             for j in range(i+1, len(res)):
#                 number_of_superior_idx = res[j]
#                 self.assertTrue(number<number_of_superior_idx) #check that the list is ordered and that there are no duplicates

# if __name__ == '__main__':
#      unittest.main()
