import time
from CalculateDiagonalElementInArray import random_matrix_and_calculate_diagonal
from LongestString import longest_string
from MatchingElementInArray import matching_elements_in_array
from ReverseString import reverse_string

def menu():
    while True:
        print("\nPilih fungsi yang ingin dijalankan:")
        print("1. Hitung pengurangan diagonal matriks")
        print("2. Temukan kata terpanjang")
        print("3. Hitung jumlah elemen yang cocok dalam dua array")
        print("4. Membalikan string")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1-5): ")
        print("\n")
        if choice == '1':
            random_matrix_and_calculate_diagonal()
        elif choice == '2':
            longest_string()
        elif choice == '3':
            matching_elements_in_array()
        elif choice == '4':
            reverse_string()
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print("\n"+"----------------------------------------------------")  # Print a line for spacing
        time.sleep(1)  # Delay for 2 seconds

# Run the menu
if __name__ == "__main__":
    menu()
