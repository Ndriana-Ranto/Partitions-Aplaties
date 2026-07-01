## Description

Ce programme Python génère des permutations de taille (n) satisfaisant des conditions liées aux runs croissants.

Pour deux entiers (n) et (r), le programme cherche toutes les permutations commençant par (1) telles que :

1. la permutation possède une sous-suite croissante de longueur (r) contenant (1) ;
2. elle ne possède aucune sous-suite croissante de longueur strictement supérieure à (r) contenant (1) ;
3. les têtes des runs sont croissantes ;
4. les pieds des runs sont décroissants.

Ainsi, le paramètre (r) représente la longueur maximale exacte d’une sous-suite croissante contenant (1).

## Paramètres

Dans le programme, on peut modifier :

```python
n = 7
r = 5
```

Ici :

* (n = 7) signifie que l’on travaille avec les permutations de ({1,2,3,4,5,6,7}) ;
* (r = 5) signifie que la plus longue sous-suite croissante contenant (1) doit être de longueur exactement (5).

## Définition d’un run

Un run est un bloc maximal de termes consécutifs strictement croissants.

Par exemple :

```text
(1, 3, 5, 2, 4)
```

se décompose en :

```text
[1, 3, 5] [2, 4]
```

Cette permutation possède donc 2 runs.

## Sortie du programme

Le programme affiche les permutations valides, leur décomposition en runs, puis les classe selon le nombre de runs.

À la fin, il affiche le total général des permutations obtenues.
