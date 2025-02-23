from colorama import Fore
import contextlib

rows = 0
size = 0
end_message = f'1. Choose a new pattern\n2. Exit'
zero_message = 'Please, enter a number different from zero!'
# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
while True:
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = abs(int(input("Enter the number of rows: ")))

        if rows == 0:
            print(zero_message)
            rows = abs(int(input("Enter the number of rows: ")))

    elif choice in [2, 5, 8]:  # Patterns that need size
        size = abs(int(input("Enter the size of the square/rectangle: ")))

        if size == 0:
            print(zero_message)
            size = abs(int(input("Enter the size of the square/rectangle: ")))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        # TODO: Loop through rows and print increasing stars
        while True:
            color = int(input('Choose one of the following colors:\n1. Red\n2. Green\n3. Magenta'
                              '\nEnter the number corresponding to your choice: '))
            if color == 1:
                print()
                save_file = int(input('Would you like to save the pattern as a text file?\n1. Yes\n2. No'
                                      '\nEnter the number corresponding to your choice: '))
                if save_file == 1:
                    with open('Red Triangle 1.txt', 'w') as f:
                        for i in range(rows + 1):
                            triangle_line = '*' * i
                            print(Fore.RED + triangle_line)
                            f.write(triangle_line + '\n')
                    print(Fore.RESET)

                elif save_file == 2:
                    for i in range(rows + 1):
                        print(Fore.RED + f"{'*' * i}")
                    print(Fore.RESET)
                break
            elif color == 2:
                print()
                save_file = int(input('Would you like to save the pattern as a text file?\n1. Yes\n2. No'
                                      '\nEnter the number corresponding to your choice: '))
                if save_file == 1:
                    with open('Green Triangle 1.txt', 'w') as f:
                        for i in range(rows + 1):
                            triangle_line = '*' * i
                            print(Fore.GREEN + triangle_line)
                            f.write(triangle_line + '\n')
                    print(Fore.RESET)
                elif save_file == 2:
                    for i in range(rows + 1):
                        print(Fore.GREEN + f"{'*' * i}")
                    print(Fore.RESET)
                break
            elif color == 3:
                print()
                save_file = int(input('Would you like to save the pattern as a text file?\n1. Yes\n2. No'
                                      '\nEnter the number corresponding to your choice: '))
                if save_file == 1:
                    with open('Magenta Triangle 1.txt', 'w') as f:
                        for i in range(rows + 1):
                            triangle_line = '*' * i
                            print(Fore.MAGENTA + triangle_line)
                            f.write(triangle_line + '\n')
                    print(Fore.RESET)
                elif save_file == 2:
                    for i in range(rows + 1):
                        print(Fore.MAGENTA + f"{'*' * i}")
                    print(Fore.RESET)
                break
            else:
                print('Invalid choice! Please, choose again!')
                # color = int(input('1. Red\n2. Green\n3. Magenta\nEnter the number corresponding to your choice: '))
                continue

    elif choice == 2:  # Square with Hollow Center
        # TODO: Create a square with a hollow center

        print('*' * size)
        for i in range(1, size - 1):
            print(f"*{' ' * (size - 2)}*")
        print('*' * size)

    elif choice == 3:  # Diamond
        # TODO: Create a diamond shape using loops

        if rows % 2 != 0: # Pattern for odd numbers.
            for i in range(rows + 1):
                if i % 2 == 0:
                    continue
                print(f'{' ' * ((rows - i) // 2)}{'*' * i}')

            for k in range(rows - 1, 0, -1):
                if k % 2 == 0:
                    continue
                print(f'{' ' * ((rows - k) // 2)}{'*' * k}')

        elif rows % 2 == 0: # Pattern for even numbers
            for i in range(1, rows):
                if i % 2 == 0:
                    continue
                print(f'{' ' * ((rows - i) // 2)}{(i + 1) * '*'}')

            for k in range(rows, 0, -1):
                if k % 2 == 0:
                    continue
                print(f'{' ' * ((rows - k) // 2)}{(k + 1) * '*'}')

    elif choice == 4:  # Left-angled Triangle
        # TODO: Print decreasing stars for each row

        for i in range(rows, 0, -1):
            print(f'{'*' * i}')


    elif choice == 5:  # Hollow Square
        # TODO: Similar to choice 2 but ensure perfect square logic

        for i in range(1, size + 1):
            if i == 1 or i == size:
                print("*" * size)
            else:
                print("*" + " " * (size - 2), end="")
                print("*")

    elif choice == 6:  # Pyramid
        # TODO: Center-align stars to form a pyramid

        for i in range(rows + 1):
            if i % 2 == 0:
                continue
            print(f'{' ' * ((rows - i) // 2)}{'*' * i}')

    elif choice == 7:  # Reverse Pyramid
        # TODO: Create an upside-down pyramid

        for i in range(rows, 0, -1):
            if i % 2 == 0:
                continue
            print(f'{' ' * ((rows - i) // 2)}{'*' * i}')

    elif choice == 8:  # Rectangle with Hollow Center
        # TODO: Handle separate width and height inputs for rectangle

        width = abs(int(input("Enter the width of the rectangle: ")))
        height = abs(int(input("Enter the height of the rectangle: ")))

        for i in range(height):
            if i == 0:
                print('*' * width)
            elif i == (height - 1):
                print('*' * width)
            else:
                print(f'*{' ' * (width - 2)}*')

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Optional - Allow the user to restart or exit
    print()
    print(end_message)

    end_choice = int(input("Enter the number corresponding to your choice: "))

    if end_choice == 1:
        continue

    if end_choice == 2:
        print('Goodbye!')
        break
    else:
        print("❌ Invalid choice! Please restart the program.")
        break

