import os

def main: 

    print("EUID :";os.geteuid())
    print("EGID :",os.getegid())

if __name__ == "__main__":
    main()