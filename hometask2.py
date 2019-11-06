# 1
philosophy = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. " \
            "Complex is better than complicated. Flat is better than nested. Sparse is better than dense.Readability counts."
print("Count of word 'better' - ", philosophy.count('better'))
print("Count of word 'never' - ", philosophy.count('never'))
print("Count of word 'is' - ", philosophy.count('is'))
print(philosophy.upper())
print(philosophy.replace('i', '&'))
# 2
n = str(4832)
product = int(n[0])*int(n[1])*int(n[2])*int(n[3])
print("Product of multiplication is ", product)
print("Reverse writing of number is ", int(n[::-1]))
print("Sorted number is ", int(''.join(sorted(n))))
# 3
a = 5
b = 3
a = a + b
b = a - b
a = a - b
print("a = ",a)
print("b = ",b)
