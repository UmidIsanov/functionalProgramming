from scipy.optimize import linprog

c = [-1, -2]
A = [[2, 3], [2, 1], [1, 0], [1, -1], [-2, -1]]
b = [6, 4, 1, -1, -1]
x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

print('Оптимальное значение функции:', -res.fun)
print('Оптимальные значения переменных x1 и x2:', res.x)
