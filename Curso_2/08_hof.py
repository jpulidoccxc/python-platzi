def increment(x):
  return x + 1

response = increment(2)
print(response)

increment_v2 = lambda x: x + 1
print(increment_v2(2))


def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(2, increment)
print(result)

high_ord_func_v2 = lambda x, func: x + func(x)
result_v2 = high_ord_func(2, increment_v2)
print(result_v2)