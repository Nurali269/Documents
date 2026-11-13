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

#задача 7
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
print(validate_pin("1234"))
print(validate_pin("123456"))
print(validate_pin("12345"))
print(validate_pin("1234a"))
print(validate_pin("1234567"))

print()
#задача 8
def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]
print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))

print()
#задача 9
def sort_by_length(arr):
    return sorted(arr, key=len)
print(sort_by_length(["Telescope", "Glasses", "Eye", "Opitcs", "I"]))

print()

#задача 10
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
print(solution(10))
print(solution(20))
print(solution(30))

print()

#задача 11
def reverse_words(text):
    return " ".join(word[::-1] for word in text.split (" "))
print(reverse_words("Hello World"))
print(reverse_words("Python is fun"))

print()

#задача 12
def count_bits(n):
    return bin(n).count("1")
print(count_bits(5))
print(count_bits(10))
print(count_bits(15))

print()

#задача 13
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())
print(to_jaden_case("hello world"))
print(to_jaden_case("KKC collage is very good"))

print()

#задача 14
def comp(array1, array2):
    return array1 is not None and array2 is not None and sorted([x**2 for x in array1]) == sorted(array2)
print(comp([1, 2, 3], [1, 4, 9]))
print(comp([1, 2, 3], [1, 4, 8]))
print(comp([1, 2, 3], [1, 4, 9, 16]))

print()

#задача 15
def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, 1)]
print(number(["Hello", "World", "Python"]))
print(number(["This", "is", "a", "test"]))

print()

#задача 16
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']))

print()

#задача 17
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
print(number([(10, 0), (3, 5), (5, 8)]))
print(number([(3, 0), (9, 1), (4, 10), (12, 2), (6, 1), (7, 10)]))  

print()

#задача 18
def high(x):
    return max(x.split(), key=lambda w: sum(ord(c) - 96 for c in w))
print(high("man i need a taxi up to ubud"))
print(high("what time are we climbing up the volcano"))
print(high("take me to semynak"))

print()

#задача 19
def find_uniq(arr):
    return next(x for x in set(arr) if arr.count(x) == 1)
print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 3, 3, 3, 3, 4]))

print()

#задача 20
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
print(is_anagram("listen", "silent"))
print(is_anagram("triangle", "integral"))
print(is_anagram("hello", "world")) 

print()

#задача 21
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])
print(gimme([2, 3, 1]))
print(gimme([5, 10, 14]))

print()

#задача 22
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
print(xo("xo"))
print(xo("xxoo"))
print(xo("Hello, my name is Alex"))

print()

#задача 24
def dont_give_me_five(start,end):
    return sum('5' not in str(i) for i in range(start, end + 1))
print(dont_give_me_five(1, 9))
print(dont_give_me_five(4, 17))

print()

#задача 25
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
print(max_multiple(3, 10))
print(max_multiple(7, 20))

print()

#задача 26
def square_digits(num):
    return int(''.join(str(int(c)**2) for c in str(num)))  
print(square_digits(9119))
print(square_digits(1234))

print()

#задача 27
def printer_error(s):
    return f"{sum(c > 'm' for c in s)}/{len(s)}"
print(printer_error("aaabbbbhaijjjm"))
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))

print()

#задача 28
import heapq

def queue_time(customers, n):
    t = [0] * n
    for c in customers:
        heapq.heappushpop(t, t[0] + c)
    return max(t, default=0)
print(queue_time([5, 3, 4], 1))
print(queue_time([10, 2, 3, 3], 2))
print(queue_time([2, 3, 10], 2))

print()

#задача 29
def in_array(array1, array2):
    return sorted(set(a for a in array1 if any(a in b for b in array2)))
print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))

print()

#задача 30
def stray(arr):
    return min(set(arr), key=arr.count)
print(stray([1, 1, 2]))
print(stray([17, 17, 3, 17, 17, 17, 17]))

print()

#задача 31
def capitalize(s):
    return ["".join(c.upper() if i % 2 == e else c for i, c in enumerate(s)) for e in (0, 1)]
print(capitalize("abcdef"))
print(capitalize("Hello World"))

print()
