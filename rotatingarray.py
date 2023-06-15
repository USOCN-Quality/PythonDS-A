# alice has some cards with numbers written on them. She arranges the cards in decreasing order and lays them
#  face down in a sequence on a table. Shecallenges bob to pick out the card conaining a given number by turning over as few cards as possible. Write a function to help bob locate the card. 

# 1) problem statement in my words: we have a set of cards in decreasing order which we can show as a list in decreasing order. Our goal is to find a specific value in that list with the least amount of iterations possible.
# 2) An example input would be [5,4,3,2,1]and to find the value 3. The output would be 2.
# for edge cases we may consider if the value in the list, if it is the last or first index of the list, if it occurs multiple times, if the list is empty, if it contains repeating numbers. 
# test case: cards = [5,4,3,2,1]
# query = 3
# expected output = 2
 # make the first function just start as becuase it doesnt do anything as the default function while naming
# function is called locate card because it is descriptive for coding practices
tests = [];
test = {
    'input':{
        'cards':[5,4,3,2,1],
        'query': 3
    },
    'output':2
}
tests.append(test)
tests.append({
    'input':{
        'cards':[3,-1,-9,-127],
        'query': -127
    },
    'output':3
})
tests.append({
    'input':{
        'cards':[6],
        'query': 6
    },
    'output':0
})
tests.append({
    'input':{
        'cards':[],
        'query': 8
    },
    'output':-1
})
tests.append({
    'input':{
        'cards':[6,5,4,3,2,1],
        'query': 8
    },
    'output':-1
})
# print(tests)
# create var with value 0, check if it == query, 
# if so return, else pos +1 check again,
# repeat until solution or last position reached, if not found return -1
def locate_card(cards, query):
#    loop through each element in array for existing elements
   for x in range(len(cards)):
    #   check if card at index is equal to the query, if so return index
      if cards[x]==query:
         return x
    # if nothing matches, return -1
   return -1
def evaluate_tests(test_cases):
   for x in range(len(test_cases)):
      test_result="Pass" if tests[x]['output']==locate_card(tests[x]['input']['cards'],tests[x]['input']['query']) else "Fail" 
      print("Test Case "+str(x)+":")
      print("Input "+str(tests[x]['input']))
      print("Expected output: "+str(tests[x]['output']))   
      print("My output: "+str(locate_card(tests[x]['input']['cards'],tests[x]['input']['query'])))
      print("Test result: "+test_result)   
      print("=================================")

evaluate_tests(tests)
