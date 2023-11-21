import numpy
import numpy as np


def input_by_keyword_emc(n_):  # n_ - число переменных (иксов)
    return np.array(list(map(int, input().split()))).reshape(n_, n_ + 1)


def res_gauss_output_and_create_emc(v, n):
    a = np.array([[0.0] * n] * n)
    x_for_assembling_b = np.array([x for x in range(v, v + 3 * n, 3)]).reshape(n, 1)
    for i in range(n):
        a[i, i] = v
        for j in range(n):
            if i != j:
                a[i, j] = v * 0.01
        v += 3
    b = np.dot(a, x_for_assembling_b)
    matrix_emc = np.hstack([a, b])
    print(matrix_emc)
    numpy.set_printoptions(precision=3, floatmode='fixed')
    # n = len(matrix_emc)
    for j in range(n):
        matrix_emc[j, :] /= matrix_emc[j, j]
        for i in range(j + 1, n):
            matrix_emc[i, :] -= matrix_emc[j, :] * matrix_emc[i, j]
    print(matrix_emc)  # результат прямого хода
    x = np.array([0.0 for i in range(n)])
    x[n - 1] = np.array(matrix_emc[n - 1, n])  # x_n = b_n
    for i in range(n - 2, -1, -1):
        item = matrix_emc[i, n]
        for j in range(i + 1, n):
            item -= matrix_emc[i, j] * x[j]
        x[i] = item
    # x = np.append(x, [matrix_emc[n - 2, n] - matrix_emc[n - 2, n - 1] * x[0]])
    # x = np.append(x, matrix_emc[n - 3, n] - matrix_emc[n - 3, n - 2] * x[1])
    print(x)


def get_emc_for_run_through_method(v, n):
    a = np.array([[0.0] * n] * n)
    x_for_assembling_b = np.array([x for x in range(v, v + 3 * n, 3)]).reshape(n, 1)
    for i in range(n):
        a[i, i] = v
        for j in range(n):
            if abs(i - j) >= 2:
                a[i, j] = 0
            elif i != j:
                a[i, j] = v * 0.01
        v += 3
    b = np.dot(a, x_for_assembling_b)
    emc = np.hstack([a, b])
    return emc


def print_p_q_x(array):
    array_p_q_x = np.zeros((len(array) + 1, 3), dtype=np.float64)
    array_p_q_x[0][0] = 0  # P
    array_p_q_x[0][1] = 0  # Q
    # print(f"[1]a={array[1][0]} b={-1*array[1][1]} c={array[1][2]} d={array[1][-1]}")
    for i in range(1, len(array_p_q_x) - 1):
        array_p_q_x[i][0] = array[i - 1][i] / (
            -1 * array[i - 1][i - 1] - array[i - 1][i - 2] * array_p_q_x[i - 1][0]
        )
        # P(104-106): a_i=array[i][i - 1] , b_i=-1 * array[i][i] , c_i=array[i][i + 1] P_i-1=array_P_Q[i - 1][0] , Q_i=1=array_P_Q[i - 1][1]
        array_p_q_x[i][1] = (
            array[i - 1][i - 2] * array_p_q_x[i - 1][1] - array[i - 1][-1]
        ) / (-1 * array[i - 1][i - 1] - array[i - 1][i - 2] * array_p_q_x[i - 1][0])
        # Q(108-110)        # ОПТИМИЗИРОВАТЬ ОПЕРАЦИИ(104-110) (Т.К. B=-B ПЕРЕПИСАТЬ ЗНАКИ (МИНУСЫ))
    # array_p_q_x[len(array_p_q_x) - 1][1] = -array[len(array) - 1][-2]  # Q_n-1
    # print(f"[-1]a={array[-1][-3]} b={-1*array[-1][-2]} d={array[-1][-1]}")
    array_p_q_x[-1][1] = (array[-1][-3] * array_p_q_x[-2][1] - array[-1][-1]) / (
        -1 * array[-1][-2] - array[-1][-3] * array_p_q_x[-2][0]
    )  # Q_n-1
    array_p_q_x[-1][2] = array_p_q_x[-1][1]  # X_n
    for i in range(len(array_p_q_x) - 2, -1, -1):
        array_p_q_x[i][2] = (
            array_p_q_x[i + 1][0] * array_p_q_x[i + 1][2] + array_p_q_x[i + 1][1]
        )
        # for i in range (len(array_p_q_x))
    for i in range(len(array_p_q_x) - 1):
        print(round(array_p_q_x[i][2], 2), end=" ")


def output_res_run_through_method(ecm, n):
    p = np.empty(n + 1)
    q = np.empty(n + 1)
    p[1] = ecm[0, 1] / (-ecm[0, 0])  # p_2 = c_1 / b_1  в обозначениях лекций
    q[1] = -ecm[0, n] / (-ecm[0, 0])  # q_2 = - d_1 / b_1
    for i in range(1, n - 1):
        # p_(i+1) = c_i / (b_i - a_i * p_i) в обозначениях лекций
        # q_(i+1) = (a_i * q_i - d_i) / (b_i - a_i * p_i) в обозначениях лекций
        if i == n:
            p[i] = 0
        else:
            p[i] = ecm[i - 1, i] / (-ecm[i - 1, i - 1] - ecm[i - 1, i - 2] * p[i - 1])
        q[i] = (ecm[i - 1, i - 2] * q[i - 1] - ecm[i - 1, -1]) / (-ecm[i - 1, i - 1] - ecm[i - 1, i - 2] * p[i - 1])
    print(list(zip(p[1:], q[1:])), end=' ')
    print(ecm[n - 1, n - 1])  # q_(n+1) == b_n
    x = np.empty(n + 1)
    x[n] = ecm[n - 1, n - 1]  # x_n = q_(n+1)
    for i in range(n - 2, -1, -1):
        x[i] = p[i + 1] * x[i + 1] + q[i + 1]
    print(x[1:])


# res_gauss_output_and_create_emc(9, 1000)
n = 5
v = 9
print((get_emc_for_run_through_method(v, n)))
output_res_run_through_method((get_emc_for_run_through_method(v, n)), n)  # Это не работает!!!!
print_p_q_x(get_emc_for_run_through_method(v, n))  # Это работает верно!




# n = int(input("n = "))
# matrix_emc = input_by_keyword_EMC(n)
# Матрица расширенных коэффициэентов
# matrix_emc = np.array([[9,   0.09, 0.09,  0.09, 0.09, 86.94],
#                        [0.12, 12,   0.12, 0.12,  0.12, 151.56],
#                        [0.15, 0.15, 15,   0.15,  0.15, 234],
#                        [0.18, 0.18, 0.18, 18,    0.18, 334.26],
#                        [0.21, 0.21, 0.21, 0.21,  21,   452.34]])
