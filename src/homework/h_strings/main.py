import strings

def menu():
    print("""
1. Hamming Distance
2. DNA Complement
3. Exit
          """)
    
def run_menu():
    menu()
    option = int(input("Select a menu option: "))
    handle_menu(option)

def handle_menu(option):
    while True:
        if option == 1:
            print("The valid DNA characters are A, C, G, T.")
            str1 = input("Enter a string of DNA: ")
            str2 = input("Enter a second, different string of DNA: ")
            print(f"The Hamming distance is {strings.get_hamming_distance(str1.upper(), str2.upper())}.")
            
        elif option == 2:
            print("The valid DNA characters are A, C, G, T.")
            dna = input("Enter a string of DNA: ")
            print(f"The DNA complement is {strings.get_dna_complement(dna.upper())}.")
            
        elif option == 3:
            print("You have chosen to exit.")
            exit()
        else:
            print("Invalid choice.")
            
        run_menu()

run_menu()
