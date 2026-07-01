# Cas particulier : (r=n+1)

Dans ce programme, on fixe :

```python
n = 5
r = n + 1
```

Donc ici :

```python
r = 6
```

Le programme vérifie si une permutation de taille (n) évite une sous-suite croissante de longueur (r).

Or, une permutation de taille (5) ne peut pas contenir une sous-suite croissante de longueur (6).
Donc la condition d’évitement est automatiquement vérifiée.

Ainsi, le programme filtre seulement les permutations qui :

* commencent par (1) ;
* ont des têtes de runs croissantes ;
* ont des pieds de runs décroissants.

---

## Test en ligne

Pour tester le programme :

1. Ouvrir le site :

```text
https://www.online-python.com/
```

2. Effacer le code déjà présent.

3. Copier-coller le programme Python.

4. Cliquer sur **Run**.

---

## Modifier la valeur de (n)

Dans le programme, on peut modifier :

```python
n = 5
r = n + 1
```

Par exemple, si on prend :

```python
n = 7
r = n + 1
```

alors :

```python
r = 8
```

Le programme cherchera à éviter une sous-suite croissante de longueur (8), ce qui est impossible dans une permutation de taille (7).
La condition d’évitement reste donc toujours vraie.

---

## Interprétation mathématique

Pour une permutation de taille (n), il est impossible d’avoir une sous-suite de longueur (n+1).

Donc :

[
\operatorname{Av}(12\cdots(n+1)) = S_n.
]

Cela signifie que toutes les permutations de taille (n) évitent automatiquement le motif croissant (12\cdots(n+1)).

Le programme étudie donc uniquement les contraintes sur les runs.
