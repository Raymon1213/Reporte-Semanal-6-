import time
import random
import matplotlib.pyplot as plt
import numpy as np

def contar_subarreglos_topdown(n, p, q):
    pos_p = [0] * (n + 2)  # +2 para incluir n+1
    pos_q = [0] * (n + 2)
    for i in range(n):
        pos_p[p[i]] = i
        pos_q[q[i]] = i
    pos_p[n + 1] = n
    pos_q[n + 1] = n

    memoL, memoR, memoDP = {}, {}, {}

    def L(x):
        if x == 0: return 0
        if x in memoL: return memoL[x]
        if x == 1: res = min(pos_p[1], pos_q[1])
        else: res = min(L(x-1), pos_p[x], pos_q[x])
        memoL[x] = res
        return res

    def R(x):
        if x == 0: return n - 1
        if x in memoR: return memoR[x]
        if x == 1: res = max(pos_p[1], pos_q[1])
        else: res = max(R(x-1), pos_p[x], pos_q[x])
        memoR[x] = res
        return res

    def A(x):
        l, r = L(x), R(x)
        if l > r: return 0
        return (l + 1) * (n - r)

    def DP(x):
        if x in memoDP: return memoDP[x]
        if x == 1:
            l1, r1 = min(pos_p[1], pos_q[1]), max(pos_p[1], pos_q[1])
            left_count = l1 * (l1 + 1) // 2
            right_count = (n - r1 - 1) * (n - r1) // 2
            mid_count = (r1 - l1 - 1) * (r1 - l1) // 2 if r1 > l1 + 1 else 0
            res = left_count + right_count + mid_count
        else:
            l_prev, r_prev = L(x-1), R(x-1)
            if l_prev > r_prev:
                res = 0
            else:
                res = 0
                if x <= n:
                    if pos_p[x] > r_prev and pos_q[x] > r_prev:
                        res += (l_prev + 1) * (min(pos_p[x], pos_q[x]) - r_prev)
                    if pos_p[x] < l_prev and pos_q[x] < l_prev:
                        res += (l_prev - max(pos_p[x], pos_q[x])) * (n - r_prev)
                    if (pos_p[x] < l_prev and pos_q[x] > r_prev) or (pos_q[x] < l_prev and pos_p[x] > r_prev):
                        left_part = l_prev - min(pos_p[x], pos_q[x])
                        right_part = max(pos_p[x], pos_q[x]) - r_prev
                        res += left_part * right_part
                else:
                    res = A(n)
        memoDP[x] = res
        return res

    total = 0
    for x in range(1, n + 2):
        total += DP(x)
    return total


# =====================
# Pruebas de ejemplos
# =====================
def pruebas_finales():
    casos = [
        {"n": 3, "p": [2, 3, 1], "q": [3, 1, 2], "esperado": 2},
        {"n": 4, "p": [1, 2, 3, 4], "q": [1, 3, 2, 4], "esperado": 9},
        {"n": 7, "p": [7, 3, 6, 2, 1, 5, 4], "q": [6, 7, 2, 5, 3, 1, 4], "esperado": 16},
    ]
    print("=== PRUEBAS DE EJEMPLOS ===")
    for i, caso in enumerate(casos, 1):
        resultado = contar_subarreglos_topdown(caso["n"], caso["p"], caso["q"])
        print(f"Caso {i}: resultado={resultado}, esperado={caso['esperado']}, "
              f"{'CORRECTO' if resultado == caso['esperado'] else 'INCORRECTO'}")


# =====================
# Experimento de tiempos con semilla fija
# =====================
def experimento_tiempos():
    random.seed(42)  # Semilla fija para reproducibilidad
    tamaños = [100, 500, 1000, 2000, 5000]
    tiempos = []

    for n in tamaños:
        p = list(range(1, n+1))
        q = list(range(1, n+1))
        random.shuffle(p)
        random.shuffle(q)
        start = time.time()
        contar_subarreglos_topdown(n, p, q)
        end = time.time()
        tiempos.append(end - start)
        print(f"n={n}, tiempo={end-start:.6f}s")

    # Comparación con f(x) = α * n (ajuste lineal teórico O(n))
    tiempos_normalizados = [t / n for t, n in zip(tiempos, tamaños)]
    cte = np.mean(tiempos_normalizados)

    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos, 'o-', label="Tiempo experimental (s)")
    plt.plot(tamaños, [cte * n for n in tamaños], 'r--', label=f"Referencia O(n), α={cte:.2e}")
    plt.xlabel("Tamaño de la entrada n (longitud de la permutación)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución del algoritmo Top-Down vs tamaño n")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    pruebas_finales()
    print("\n=== EXPERIMENTO DE TIEMPOS ===")
    experimento_tiempos()
