try:
    n=int(input())
    b=int(input())
    a=input()
    c=n+b
    l=a+b
    n.append(3)
except ValueError:
    raise ValueError("Value Error Occured")
except TypeError:
    raise TypeError("Type Error Occured")
except AttributeError:
    raise AttributeError("Attribute Error Occured")