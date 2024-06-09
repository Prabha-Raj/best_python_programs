def compose2(f, g):
    return lambda x:f(g(x))
def d(x):
    return x*2
def e(x):
    return x+1
a=compose2(d,e) # FunctionC = compose(FunctionB,FunctionA)
print(a(5)) 