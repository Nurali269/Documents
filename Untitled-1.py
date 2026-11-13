#задача 1
def high_and_low(numbers):
    nums = [int(x)for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"

print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5"))
print(high_and_low("1 9 3 4 -5"))

print()

#задача 2
def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *=int(digit)
        n = product
        count += 1
    return count
print(persistence(39))

print()
#задача 3/get the midle character
def get_middle(s):
    length = len(s)
    if length == 0:
        return ""
    
    mid = length // 2
    if length % 2 == 0:
        return s[mid - 1 : mid + 1]
    else:
        return s[mid]
print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))

print()

#задача 4/unique_in_order
def unique_in_order(sequence):
    result = []
    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)
    return result
print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order("ABBCcAD"))
print(unique_in_order([1,2,2,3,3]))

print()

#задача 5
def divisors(integer):
    result = [i for i in range(2, integer) if integer % i == 0]
    
    if not result:
        return f"{integer} is prime"
    
    return result
print(divisors(12))
print(divisors(13))
print(divisors(15))

print()

#задача 6
import string

def is_pangram(st):
    st = st.lower()
    return all(letter in st for letter in string.ascii_lowercase)
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello, world!"))
print(is_pangram("Pack my box with five dozen liquor jugs."))

print()

