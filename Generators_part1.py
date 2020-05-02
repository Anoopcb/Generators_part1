## Generators

##generators are iterators

# Iterator, Iterable

l = [1, 2, 3] #iterable
for i in l:
    print(i)
## i = iter(l)
## print(next(i))## this how for loop works, first iterable will be changed in iter
## next function can't be called on iterable

print(list(map(lambda a : a**2, l)))## this is iterator

for num in map(lambda a: a**2, l):
    print(num)

## creating a generator

# generator function
# generator comprehension

def nums(a):
    for i in range(1, a+1):
        yield (i)## THIS IS REALLY IMPORTANT WORD

for number in nums(10):
    print(number)




def even_generator(n):
    for num in range(1, n+1):
        if num%2==0:
            yield(num)
even_nums = even_generator(20)

for num in even_nums:
    print(num)

square = [i**2 for i in range(1, 11)]
print(square)



square = (i**2 for i in range(1, 11))
print(square)


#l = [i**2 for in range(10000000)] this is list comprehension and it will take lots of memory

#g = (i**2 for in range(10000000))- this is generators, it will not take that much of memory






