from scipy.optimize import linprog

c = [-0.5, -1]
A = [[2, 1], [3, -2], [-1, 2], [-2, -3]]
b = [9, 12, 8, -6]
x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')


print('Оптимальное значение функции:', -res.fun)
print('Оптимальные значения переменных x1 и x2:', res.x)
