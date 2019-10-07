import random
import sys
import time
from operator import itemgetter


def pob_ini(n, p):
    return [indv_fitness(n) for _ in range(p)]


def indv_fitness(n):
    individuo = list(range(n))
    random.shuffle(individuo)
    return [fitness(individuo), individuo]


def fitness(individuo):
    n = len(individuo)
    fitness = n * (n - 1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if (i - individuo[i] == j - individuo[j]) or (i + individuo[i] == j + individuo[j]):
                    fitness -= 1
    return fitness


def prob_fitness(poblacion):
    fitness = [individuo[0] for individuo in poblacion]
    total_fit = sum(fitness)
    relativo = [fit / total_fit for fit in fitness]
    return [sum(relativo[:i + 1]) for i in range(len(relativo))]


def ruleta_select(poblacion, probabilidades):
    seleccion = []
    for _ in range(2):
        r = random.random()
        for (idx, individuo) in enumerate(poblacion):
            if r <= probabilidades[idx]:
                seleccion.append(individuo)
                break
    return seleccion


def cruza(individuo1, individuo2, c, m):

    a, b = individuo1[1], individuo2[1]
    if random.random() < c:
        n = len(a)
        x = random.randrange(1, n)
        a, b = a[:x] + b[x:], b[:x] + a[x:]
        a, b = indv_optimo(a), indv_optimo(b)
        a, b = mutar_indv(a, m), mutar_indv(b, m)
        return [[fitness(a), a], [fitness(b), b]]
    else:
        return [indv_fitness(len(a)), indv_fitness(len(a))]


def indv_optimo(individuo):
    n = len(individuo)
    corrector = [0] * n
    for i in range(n):
        corrector[individuo[i]] += 1

    for i in range(n):
        if corrector[i] == 2:
            for j in range(n):
                if corrector[j] == 0:
                    for k in range(n):
                        if individuo[k] == i:
                            individuo[k] = j
                            corrector[j] += 1
                            corrector[i] -= 1
                            break
                    break
    return individuo


def mutar_indv(individuo, m):
    if random.random() < m:
        n = len(individuo)
        x = random.choices(range(n), k=2)
        individuo[x[0]], individuo[x[1]] = individuo[x[1]], individuo[x[0]]
    return individuo


def new_pob(poblacion, i, p, it):

    for i in range(it):
        print("> iteracion: %d" % i)
        n = len(poblacion[0][1])
        mejor_fitness = n * (n - 1)
        probabilidades = prob_fitness(poblacion)
        for _ in range(int(len(poblacion) / 2)):
            padres = ruleta_select(poblacion, probabilidades)
            hijos = cruza(padres[0], padres[1], c, m)
            poblacion.append(hijos[0])
            poblacion.append(hijos[1])
        poblacion = sorted(poblacion, key=itemgetter(0), reverse=True)
        poblacion = poblacion[:p]
        for individuo in poblacion:
            if individuo[0] == mejor_fitness:
                print("\n> Se, ha encontrado una solucion en: ")
                print(individuo[0], "\t", individuo[1])
                return poblacion
    return poblacion


# tablero
n = int(sys.argv[1])
# individuos
p = int(sys.argv[2])
# iteraciones
it = int(sys.argv[3])
 # Probabilidad de cruza
c = float(sys.argv[4])
# Probabilidad de muta
m = float(sys.argv[5])
if len(sys.argv) == 7:
    r = sys.argv[6]
     # Semilla
    random.seed(r)
else:
    r = "-"


print("\n> Problema N-reinas", "n: %d" % n, "p: %d" % p, "it: %d" % it, "c: %.2f" %
      c, "m: %.2f" % m, "f: %d" % (n * (n - 1)), "r: %s" % r, "\n> Poblacion Inicial", sep="\n")
poblacion = pob_ini(n, p)
sorted(poblacion, key=itemgetter(0), reverse=True)
for individuo in poblacion:
    print(individuo[0], individuo[1], sep="\t")
print()


start_time = time.time()
poblacion_final = new_pob(poblacion, 0, p, it)
print("\n> Tiempo de Ejecucion: %f segundos" % (time.time() - start_time))


print("\n> Poblacion Final")
sorted(poblacion_final, key=itemgetter(0), reverse=True)
for individuo in poblacion_final:
    print(individuo[0], individuo[1], sep="\t")
