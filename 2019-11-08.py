'''
Riddler Classic
This week’s Riddler Classic comes to us from Oren, who asked not to be further identified:

Now that Halloween has come and gone, your chances of getting free candy have similarly disappeared. Desperate for sugar, you wander into the candy store, where three kinds of candy are being sold: Almond Soys (yummy, sounds vegan!), Butterflingers and Candy Kernels.

You’d like to buy at least one candy and at most 100, but you don’t care precisely how many you get of each or how many you get overall. So you might buy one of each, or you might buy 30 Almond Soys, six Butterflingers and 64 Candy Kernels. As long as you have somewhere between one and 100 candies, you’ll leave the store happy.

But as a member of Riddler Nation, you can’t help but wonder: How many distinct ways are there for you to make your candy purchase?
'''

# Semi-intelligent method
sum = 0

"""
One type of candy
Three unique candies (A, B, C)
A = 1 --> 1 configuration
A = 2 --> 1 configuration
...
A = 100 --> 1 configuration
This is repeated 3 times for each candy
"""
one_type = 0
for n in range(1, 101):
    one_type += 1
one_type = one_type * 3
sum = sum + one_type

'''
Two types of candy
Three unique candy pairs (A/B, B/C, C/A)
A/B = B/A so we don't count it twice
A = 1 & B = [1:99] --> 99 configurations
A = 2 & B = [1:98] --> 98 configurations
...
A = 99 & B = 1 --> 1 configuration

This is repeated 3 times for each pair
'''

two_types = 0
for A in range(1, 100):
    configs = 100 - A
    two_types += configs
    # print(configs)
two_types = two_types * 3
sum = sum + two_types

'''
Three types of candy
Only 1 unique combination of candies (A/B/C)
BAC = ABC = CAB so we don't count them again
A = 1 & B = 1 & C=[1:98] --> 98 configurations
A = 1 & B = 2 & C=[1:97] --> 97 configurations
...
A = 1 & B = 98 & C = 1   --> 1 configuration
A = 2 & B = 1 & C = [1:97] --> 97 configurations
...
A = 2 & B = 97 & C = 1    --> 1 configuration
A = 3 & B = 1 & C = [1:96] --> 96 configurations
...
A = 3 & B = 96 & C = 1    --> 1 configuration
'''
three_types = 0
# Three types of candy
for A in range(1, 99):
    for B in range(1, 100 - A):
        configs = 100 - A - B
        three_types += configs

sum = three_types + sum
print("I grab only a single candy:", one_type/3)
print("But there are three candies:", one_type)
print("I grab only two types of candies:", two_types/3)
print("But there are three pairs of candies:", two_types)
print("I grab all three types of candy:", three_types)
print("Grand Total: <", sum, ">")


# Brute force method
sum = 0
for A in range(101):
    for B in range(101):
        for C in range(101):
            if ((A+B+C <= 100) and (A+B+C > 0)):
                sum += 1

print("Brute force: <", sum, ">")
