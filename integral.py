from sympy import *


def ToClose(temp):
    """

    :param temp: sentence start with the character just after the beginning of {
    :return: {index: index of close '}', result: content inside the curly }
    """
    wait_list = 1
    result = ''
    for i in range(len(temp)):
        if temp[i] == '{':
            wait_list += 1
        elif temp[i] == '}':
            wait_list -= 1
        if wait_list == 0:
            return {
                'index': i,
                'result': result
            }
        result += temp[i]
    return {
        'index': -1,
        'result': 'invalid Latex'
    }

def integral(eq):
    # \int_{a}^{b} (x ** 2 + (1/x))
    eq_end = len(eq) - 1 - eq[::-1].find(')')
    var = eq[eq_end + 3:]
    if var == 'lambda':
        var = 'lamda'
    var = symbols(var)
    if eq[5] != '_':  # 不定积分
        equation = eq[5:eq_end+1]
        equation = simplify(equation.replace('lambda', 'lamda'))
        return str(latex(integrate(equation, var)) + '+C')
    else:  # 定积分
        direct = ToClose(eq[7:])
        b = direct['result']  # 上限
        b_end = direct['index']
        direct = ToClose(eq[5 + b_end+5:])
        a = direct['result']  # 下限
        equation = eq[4 + b_end + 5 + direct['index'] + 3:eq_end]
        equation = simplify(equation.replace('lambda', 'lamda'))
        return str(latex(integrate(equation, (var, a, b))))


if __name__ == '__main__': #'\int (x^2 + \frac{1}{x})dx'
    # eqs = "$$\\int (x^2 + \\frac{1}{x})dx$$"
    print(integral('*\\int_{5}^{1}(x**2+((1)/(x)))*dx'))
    
    #['\int(x**2+(1/x))dx', '\int_{b}^{a} (x ** 2 + (1/x))dx', "\int (1/(2*y + cos(y)))dy", "\int (1/(6*x**2))dx", "\int (3*x**2+4*x-5)dx", "\int ((x+1)*e**(2*x))dx"]