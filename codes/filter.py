
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing=filter(lambda x: ("w" in x), lst_check)
print(list(filter_testing))
