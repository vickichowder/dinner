import random

amount = raw_input("How much did we gather today? \nPlease enter amount ($): ")

where = ("Kerr Street Ministries", "Community Food Centres Canada", "Open Door")

choice = random.choice(where)

final = 'You will be donating $'+amount+' to '+choice +'!'

print final
