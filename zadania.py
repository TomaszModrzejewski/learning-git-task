john = "John"
michael = "Michael"
terry = "Terry"
eric = "Eric"
graham = "Graham"

name = [john, michael, terry, eric, graham]
count = [1200, 1300, 1400, 1500, 1600]
dictionary = dict(zip(name, count))
for name, count in dictionary.items():
    print(name, count)
print()

numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
primes = []


def prime(n):
    prime = int(n**0.5) + 1
    if n == 1: return False

    for i in range(2, prime):
        if n % i == 0:
            return False
    return True


for element in numbers: 
    if prime(element):
        primes.append(element)
print(primes)       
print()

days = ['Mon', 'Wed', 'Fri', 'Sat']
print(days)
days.insert(1, 'Tue')
days.insert(3, 'Thu')
days.insert(6, "Sun")
print(days)
print()

tea = [("włącz czajnik"), 
       ("znajdź opakowanie herbaty"),
       ("zalej herbatę"),
       ("nalej wody do czajnika"),
       ("wyjmij kubek"),     
       ("włóż herbatę do kubka")]
tea.sort()
tea.insert(0, "znajdź opakowanie herbaty")
tea.pop(6)
print(tea)
