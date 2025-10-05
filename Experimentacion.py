import time
import random
import matplotlib.pyplot as plt

def contar_subarreglos_topdown(n, p, q):
    # Precalcular posiciones (0-based)
    pos_p = [0] * (n + 2)
    pos_q = [0] * (n + 2)
    
    for i in range(n):
        pos_p[p[i]] = i
        pos_q[q[i]] = i
    
    pos_p[n + 1] = n
    pos_q[n + 1] = n

    # Memoización
    memo_ell = {}
    memo_r = {}
    memo_dp = {}
    
    def ell(x):
        if x == 0: return 0
        if x in memo_ell: return memo_ell[x]
        result = min(ell(x - 1), pos_p[x], pos_q[x]) if x > 1 else min(pos_p[1], pos_q[1])
        memo_ell[x] = result
        return result
    
    def r(x):
        if x == 0: return n - 1
        if x in memo_r: return memo_r[x]
        result = max(r(x - 1), pos_p[x], pos_q[x]) if x > 1 else max(pos_p[1], pos_q[1])
        memo_r[x] = result
        return result
    
    def DP(x):
        if x > n + 1: return 0
        if x in memo_dp: return memo_dp[x]
        
        if x == 1:
            l1, r1 = ell(1), r(1)
            result = (l1 * (l1 + 1)) // 2 + ((n - r1 - 1) * (n - r1)) // 2
            if r1 > l1 + 1:
                result += ((r1 - l1 - 1) * (r1 - l1)) // 2
        else:
            l_prev, r_prev = ell(x - 1), r(x - 1)
            
            if l_prev > r_prev:
                result = 0
            else:
                result = 0
                if x <= n:
                    if pos_p[x] > r_prev and pos_q[x] > r_prev:
                        result += (l_prev + 1) * (min(pos_p[x], pos_q[x]) - r_prev)
                    if pos_p[x] < l_prev and pos_q[x] < l_prev:
                        result += (l_prev - max(pos_p[x], pos_q[x])) * (n - r_prev)
                    if (pos_p[x] < l_prev and pos_q[x] > r_prev) or (pos_q[x] < l_prev and pos_p[x] > r_prev):
                        left_part = l_prev - min(pos_p[x], pos_q[x])
                        right_part = max(pos_p[x], pos_q[x]) - r_prev
                        result += left_part * right_part
                else:
                    result = (l_prev + 1) * (n - r_prev)
        
        memo_dp[x] = result
        return result
    
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
        print(f"Caso {i}: resultado={resultado}, esperado={caso['esperado']}, {'CORRECTO' if resultado == caso['esperado'] else 'INCORRECTO'}")

# =====================
# Experimento de tiempos
# =====================
def experimento_tiempos():
    tamaños = [100, 500, 1000, 2000, 5000, 10000]
    tiempos = []

    for n in tamaños:
        p = list(range(1, n+1))
        q = p.copy()
        random.shuffle(p)
        random.shuffle(q)
        
        start = time.time()
        contar_subarreglos_topdown(n, p, q)
        end = time.time()
        
        tiempos.append(end - start)

    # Graficar
    plt.plot(tamaños, tiempos, marker='o')
    plt.xlabel("Tamaño de la permutación n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución del algoritmo Top-Down vs tamaño n")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    pruebas_finales()
    experimento_tiempos()