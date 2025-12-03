# ==============================================================
# EXERCICE 1 — Afficher les éléments d’une liste
# ==============================================================

nombres = [1, 2, 3, 4]

for n in nombres:
    print(n)

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 2 — Trouver le plus grand nombre
# ==============================================================

nums = [3, 7, 2, 9, 5]
max_value = nums[0]

for n in nums:
    if n > max_value:
        max_value = n

print("Le plus grand nombre est :", max_value)

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 3 — Compter les nombres pairs
# ==============================================================

l = [4, 1, 8, 3, 10]
count = 0

for x in l:
    if x % 2 == 0:
        count += 1

print("Nombre de nombres pairs :", count)

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 4 — Ajouter un élément à une liste
# ==============================================================

l = [10, 20, 30]
x = 50
l.append(x)

print("Liste après ajout :", l)

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 5 — Inverser une liste manuellement
# ==============================================================

l = [1, 2, 3, 4, 5]
inv = []

for i in range(len(l) - 1, -1, -1):
    inv.append(l[i])

print("Liste inversée :", inv)

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 6 — Fonction somme()
# ==============================================================

def somme(l):
    total = 0
    for x in l:
        total += x
    return total

print("Somme de [5, 5, 10] :", somme([5, 5, 10]))

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 7 — Fonction min_max()
# ==============================================================

def min_max(l):
    mini = l[0]
    maxi = l[0]

    for x in l:
        if x < mini:
            mini = x
        if x > maxi:
            maxi = x

    return mini, maxi

print("Min et Max de [8,2,6,1,10,3] :", min_max([8, 2, 6, 1, 10, 3]))

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 8 — Filtrer uniquement les nombres pairs
# ==============================================================

def filtrer_pairs(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)
    return result

print("Nombres pairs :", filtrer_pairs([1, 2, 3, 4, 5, 6]))

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 9 — Vérifier si une liste est triée
# ==============================================================

def est_triee(l):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            return False
    return True

print("Liste [1,2,3,4] triée ?", est_triee([1, 2, 3, 4]))
print("Liste [3,1,2] triée ?", est_triee([3, 1, 2]))

print("\n----------------------------\n")


# ==============================================================
# EXERCICE 10 — Fusionner deux listes (sans +)
# ==============================================================

def fusionner(l1, l2):
    result = []
    for x in l1:
        result.append(x)
    for x in l2:
        result.append(x)
    return result

print("Fusion :", fusionner([1, 2, 3], [4, 5, 6]))

print("\n----------------------------\n")
