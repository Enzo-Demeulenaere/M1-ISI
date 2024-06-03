# Rendu "Les droits d’accès dans les systèmes UNIX"

## Binome

- Nom, Prénom, email: Demeulenaere Enzo enzo.demeulenaere.etu@univ-lille.fr

- Nom, Prénom, email: ___

## Question 1

Le processus peut en effet écrire car même si toto n'a pas les droits d'écriture, il appartient au groupe ubuntu qui lui a les droits d'écriture

## Question 2

Le caractère x appliqué à un repertoire nous permets d'acceder à l'ensemble de ses sous-repertoires

L'utilisateur toto est privé d'éxecution sur mydir car son groupe n'a plus la permission d'executer ce repertoire

L'on voit maintenant qu'il y a un fichier data.txt dans mydir mais nous ne connaissons rien des droits sur ce fichier, cela s'explique par le fait que toto a les droits de lecture sur mydir 

## Question 3

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    char* filename = argv[1];
    FILE* file = fopen(filename,"r");
    printf("EUID : %d \n", geteuid());
    printf("EGID : %d \n", getegid());
    printf("RUID : %d \n", getuid());
    printf("RGID : %d \n", getgid());
    if (file == NULL){
        perror("Error opening file");
        return EXIT_FAILURE;
    }
    char ligne[100];
    while(fscanf(file, "%99[^\n]\n",ligne) == 1){
        printf("%s\n",ligne);
    }
    fclose(file);
    return 0;
}
```

Depuis toto, le programme n'arrive pas à ouvrir le fichier mydir/data.txt mais tous les ID ont pour valeur 1001.

Avec le flag set-user-id activé, toto arrive à ouvrir le fichier et la valeur du EUID est desormais de 1000, les autres valeurs sont toujours 1001.

## Question 4

```py
import os

def main: 

    print("EUID :";os.geteuid())
    print("EGID :",os.getegid())

if __name__ == "__main__":
    main()
```

Les EUID et EGID ont tous deux un id valant 1001 depuis toto

Un utilisateur pourrait changer un de ses attributs en executant un programme qui a des accès dépassant ceux de l'utilisateur.

## Question 5

D'après le manuel, la commande chfn permets de changer les informations d'un utilisateur.

la commande ls -al /usr/bin/chfn nous affiche les permissions suivantes : "-rwsr-xr-x" 
Cela signifie que l'utilisateur a les droits de lecture et écriture lors de l'execution, il obtient les droits du proprietaire, sinon le groupe ainsi que le reste des utilisateurs ont pour permissions de lire et d'executer le fichier

Après avoir utilisé la commande chfn depuis l'utilisateur toto, nous pouvons remarquer les changement appliqués lors de la lecture de etc/passwd

## Question 6

Je n'ai pas la réponse exacte à cette question mais je suppose que les mots de passe des utilisateurs sont hachés et stockés dans un fichier ou des fichiers accessibles uniquement à l'utilisateur root pour réduire au maximum les accès aux mots de passe, et ainsi augmenter la sécurité

## Question 7

Pour la question 7, j'ai commencé à creer la structure sans avoir pu verifier les permissions à travers des scripts bash

## Question 8

Le programme et les scripts dans le repertoire *question8*.

## Question 9

Le programme et les scripts dans le repertoire *question9*.

## Question 10

Les programmes *groupe_server* et *groupe_client* dans le repertoire
*question10* ainsi que les tests. 








