def test():
    print("One")
    yield 10

    print("Two")
    yield 20

    print("Three")
    yield 30
    x = test()
    #Abhi kuch bhi print nahi hoga.
    print(next(x))#phle next() ...... one 10
    print(next(x))
    print(next(x))
    print(next(x))#stopIteation

####################################
def count():
    yield 1
    yield 2
    yield 3

for i in count():
    print(i)

    #######################3

#| `return`                           | `yield`                   |
#| ---------------------------------- | ------------------------- |
#| Function khatam                    | Function pause            |
#| Ek hi value (ya tuple/list) return | Ek-ek value generate      |
#| Dobara shuru se call karna padega  | Wahi se continue hota hai |
#| Generator nahi banta               | Generator ban jata hai    |
#Generator ko ek baar consume kar diya, to uski values dobara nahi milti. AGR FR SE CHAIYE TO G=TEXT()
