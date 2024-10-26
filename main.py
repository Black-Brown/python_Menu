def menu():
    print("=== MENU PRINCIPAL ===")
    print("1.")
    choice = input("Elige una opción (1-4): ")
    return choice

def main():
    while True:
        choice = menu()
        

if __name__ == "__main__":
    main()
