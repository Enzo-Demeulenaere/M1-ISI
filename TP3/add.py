
def main(name,number):

    with open("Disque/Cartes.txt","a") as file:
        file.write(name,str(number))

if (__name__=="__main__"):
    main()

