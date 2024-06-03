import subprocess
import base64

def main():

    pswd1 = input("Password 1:")
    pswd2 = input("Password 2:")

    file1 = "Cle1/File.txt"
    file2 = "Cle2/File.txt"

    command1 = f'echo -n "{file1}" | openssl enc -aes-256-cbc -a -k {pswd2} -pbkdf2'
    command2 = f'echo -n "{file2}" | openssl enc -aes-256-cbc -a -k {pswd1} -pbkdf2'

    result1 = subprocess.check_output(command1, shell=True).decode('utf-8').strip()
    result2 = subprocess.check_output(command2, shell=True).decode('utf-8').strip()
    
    with open("Cle1/File.txt","w") as file:
        file.write(result1)
    with open("Cle2/File.txt","w") as file:
        file.write(result2)

    result1_128 = base64.b64encode(result1.encode()).decode('utf-8')[:16]
    result2_128 = base64.b64encode(result2.encode()).decode('utf-8')[:16]

    binary_result1 = ''.join(format(ord(char), '08b') for char in result1_128)
    binary_result2 = ''.join(format(ord(char), '08b') for char in result2_128)
    
    masterkey = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(binary_result1, binary_result2))

    fileName = "Disque/Cartes.txt"
    newFileName = "Disque/Cartes_Crypté.txt"
    command = f'openssl enc -aes-256-cbc -a -k {masterkey} -pbkdf2 -in "{fileName}" -out "{newFileName}"'
    subprocess.run(command, shell=True)

        
if (__name__=="__main__"):
    main()

