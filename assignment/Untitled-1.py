def evalPolynomial(x):
    return str(3*(int(x)**5) + 2*(int(x)**4) - (int(x)**3) + 7*int(x) - 6)
#main
value = str(input('Enter a value for x: '))
re_turn = evalPolynomial(value)
print("Polynomial for ="+ value + ': ' + re_turn)