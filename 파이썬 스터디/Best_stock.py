import numpy as np
def best_stock(a):
    # your code here
    names=[]
    numbers=[]
    for x,y in a.items():
        names.append(x)
        numbers.append(y)
    index=np.argmax(numbers)
    return names[index]

if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")
