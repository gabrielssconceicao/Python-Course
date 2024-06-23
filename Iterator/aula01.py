
iterable = ["I", "have", "__iter__"]
iterator = iter(iterable)  # has __iter__  and  __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator = iter(iterable)
for i in iterator:
    print(i)