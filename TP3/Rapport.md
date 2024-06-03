# Rapport TP Cryptographie

## Question 1

Une solution proposée serait de faire en sorte que le mot de passe d'un des responsables permette de décrypter un fichier sur la clé usb de l'autre responsable, les 2 fichiers décryptés permettant l'accès au service.
Ainsi, un responsable a bien besoin de ses 2 facteurs ainsi que des facteurs de l'autre responsable

## Question 2

1.
i   Mise en Service (decrypt.py)
ii  Ajouter une paire (add.py)
iii Supprimer une paire (delete.py)
iv  Chercher les n° de cartes associés à un nom (search.py)
v   Initialiser les 2 clefs usb et le disk (setup.py)

## Question 3 

Une nouvelle solution où chaque responsable a un représentant serait donc d'avoir 2 nouvelles clés et 2 mots de passe, ainsi il faudrait également dans chaque clé une second fichier qui correspond à une donnée ne pouvant être décryptée que par le mot de passe du représentant du responsable de l'autre partie, l'algorithme de décryptage essaierait donc de former la master key avec les différentes combinaisons de mots de passe.

Supposons Alice et Bob les 2 responsables, et leurs représentant respectifs Charlie et Daniel. 
L'algorithme tentera donc de former la masterkey formée avec les informations d'Alice et Bob, si celle-ci échoue, il va tenter la combinaison d'Alice et Daniel, puis Charlie et Bob, et enfin Charlie et Daniel. Cette solution nous permets donc d'avoir 4 masterkey différentes et par consequent d'identifier correctement quel couple de responsable ou représentant essaie d'acceder au service
