
def main(name):

    with open("Disque/Cartes.txt","r") as file:
        lines = file.readlines()
    
    numbers = [line[len(name):] for line in lines if line.startswith(name) ] 

    return numbers

if (__name__=="__main__"):
    main()

