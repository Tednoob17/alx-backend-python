#!/usr/bin/env python3

# add = __import__('0-add').add

# print(add(1.11, 2.22) == 1.11 + 2.22)
# print(add.__annotations__)

# concat = __import__('1-concat').concat

# str1 = "egg"
# str2 = "shell"

# print(concat(str1, str2) == "{}{}".format(str1, str2))
# print(concat.__annotations__)

# import math

# floor = __import__('2-floor').floor

# ans = floor(3.14)

# print("{}".format(fun(2.22)))

# element_length =  __import__('9-element_length').element_length

# print(element_length.__annotations__)

# safe_first_element =  __import__('100-safe_first_element').safe_first_element

# print(safe_first_element.__annotations__)

safely_get_value = __import__('101-safely_get_value').safely_get_value
annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))
