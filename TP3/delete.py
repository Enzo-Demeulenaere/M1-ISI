
def main(name):

    with open("Disque/Cartes.txt","r") as file:
        lines = file.readlines()
    
    newLines = [line for line in lines if not line.startswith(name) ] 

    with open("Disque/Cartes.txt","w") as file:
        file.write(newLines)

if (__name__=="__main__"):
    main()

