from scipy.optimize import linprog

c = [2, -1]
A = [[1, 3], [-1, 2], [1, -2], [2, 3]]
b = [6, 6, 1, 16]
x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

print('Оптимальное значение функции:', res.fun)
print('Оптимальные значения переменных x1 и x2:', res.x)
