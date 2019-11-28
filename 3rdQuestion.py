try:
    n=int(input())

except ValueError:
    raise ValueError("Value Error Occured")
except EOFError:
    raise EOFError("End of the file Error")
except KeyboardInterrupt:
    raise KeyboardInterrupt("Keyboard Interupt Occured")