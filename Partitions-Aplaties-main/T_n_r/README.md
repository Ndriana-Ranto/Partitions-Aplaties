# Triangular Flattened Partitions – Python Generator

## Description

Ce programme Python permet de générer des permutations satisfaisant simultanément plusieurs contraintes combinatoires liées aux **Triangular Flattened Partitions**.

Pour une valeur donnée de :

* **n** : taille de la permutation ;
* **r** : longueur du motif croissant interdit (12\cdots r),

le programme énumère toutes les permutations commençant par **1** qui vérifient les conditions suivantes :

1. **Évitement du motif croissant** (12\cdots r) (aucune sous-suite croissante de longueur (r)).
2. Les **têtes des runs** sont strictement croissantes.
3. Les **pieds des runs** sont strictement décroissants.

Les résultats sont ensuite classés selon leur **nombre de runs**, puis le programme affiche le nombre total de permutations obtenues.



# Modifier les paramètres

À la fin du programme, dans le bloc principal, on trouve :

```python
if __name__ == "__main__":
    n = 5
    r = 4
```

Il suffit de modifier ces deux valeurs.

Par exemple :

```python
n = 7
r = 5
```

Le programme générera alors toutes les permutations de taille **7** évitant le motif **12345**, satisfaisant également les deux contraintes sur les runs.

---

# Signification des paramètres

* **n** : taille de la permutation.

Exemple :

```
n = 5
```

Le programme travaille sur les permutations de

```
(1,2,3,4,5)
```

---

* **r** : longueur du motif croissant interdit.

Par exemple

```
r = 4
```

signifie que toute permutation contenant une sous-suite croissante de longueur **4** est rejetée.

---

# Exemple de sortie

Pour

```python
n = 5
r = 4
```

on obtient :

```
🔹 Permutations avec 2 run(s) (sous-total : 2)
(1, 3, 5, 2, 4)
(1, 4, 5, 2, 3)

🔹 Permutations avec 3 run(s) (sous-total : 1)
(1, 5, 2, 4, 3)

✅ Total général : 3
```

Chaque ligne indique :

* la permutation obtenue ;
* sa décomposition en runs ;
* le groupe auquel elle appartient selon son nombre de runs.

---

# Définition d'un run

Un **run** est un bloc maximal de termes consécutifs strictement croissants.

Exemple :

```
(1, 3, 5, 2, 4)
```

se décompose en

```
[1,3,5] [2,4]
```

Il possède donc **2 runs**.

---

# Conditions imposées

Une permutation est conservée uniquement si elle satisfait simultanément :

* elle commence par **1** ;
* elle évite le motif croissant (12\cdots r) ;
* les têtes des runs sont croissantes ;
* les pieds des runs sont décroissants.

---

# Applications

Ce programme sert principalement à la recherche en combinatoire énumérative, notamment dans l'étude des **Triangular Flattened Partitions**, des permutations à motifs interdits et de l'énumération des familles (T_{n,r}).

Il permet de produire rapidement des exemples, de vérifier des conjectures et de calculer expérimentalement les cardinalités pour différentes valeurs de (n) et (r).
