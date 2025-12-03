import random

livres = [
    {"titre": "1984", "auteur": "Orwell", "annee": 1949, "tags": {"politique", "dystopie"}},
    {"titre": "Dune", "auteur": "Herbert", "annee": 1965, "tags": {"science-fiction"}},
    {"titre": "Le Petit Prince", "auteur": "Saint-Exupéry", "annee": 1943, "tags": {"enfant", "philosophie",}},
]

# 1. Afficher tous les titres
for livre in livres:
    print(livre["titre"])

print("------------------")

# 2. Ajouter un nouveau livre
livres.append({
    "titre": "Fondation",
    "auteur": "Asimov",
    "annee": 1951,
    "tags": {"science-fiction"}
})

# 3. Livres avant 1950
# anciens = [l for l in livres if l["annee"] < 1950]
a = []
for L in livres :
    if L["annee"]< 1950:
        a.append(L)
print("Livres avant 1950 :", a)

print("------------------")

# 4. Tous les tags uniques
tags = set()
for livre in livres:
    tags |= livre["tags"] 
print("Tags uniques :", tags)

print("------------------")

# 5. Livre aléatoire
aleatoire = random.choice(livres)
print(f"Vous devriez lire : {aleatoire['titre']} ({aleatoire['auteur']})")

print("------------------")

# 6. Trier par année
trie = sorted(livres, key=lambda x: x["annee"])
print("Trié par année :", trie)

print("------------------")

# 7. Transformer en liste de tuples
archives = [(l["titre"], l["auteur"], l["annee"]) for l in livres]
print("Structure tuples :", archives)


archives=[]
for l in livres:
    archives.append((l["titre"], l["auteur"], l["annee"]))

