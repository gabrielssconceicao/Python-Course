def generator(n=0, maximum=10):
    while True:
        yield n
        n+=1
        if n > maximum:
            return
        
gen = generator(5,20)
for n in gen:
    print(n)