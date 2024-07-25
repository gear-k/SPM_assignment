# print("".join(header))
# for i in range(size):
#     print(separator)
#     row = [f"{i+1:2}  "]
#     for j in range(temp):
#         cell = self.cells[i][j+self.start]
#         if cell.isdigit():
#             color = Fore.BLUE  # Blue for digits
#         elif cell.isalpha():
#             color = Fore.GREEN  # Green for letters
#         else:
#             color = Style.RESET_ALL
#         row.append(f"| {color}{cell}{Style.RESET_ALL} ")
#     row.append("|")
#     print("".join(row))
# print(separator)

# from colorama import Fore, Style, init
# init()
# print(Fore.RED + "This text is red!" + Style.RESET_ALL)
# print("hi")
# print(Fore.GREEN + "This text is green!")
# print(Fore.BLUE + "This text is blue!")
# print(Style.BRIGHT + "This text is bright!")
# print(Style.DIM + "This text is dim!")
# print(Style.RESET_ALL)

# color = Fore.GREEN
# cell = "rcsdvcdsv"
# print(f"{color}{cell}{Style.RESET_ALL}")

# position = input("Enter the position to place the building (e.g., A1): ").strip().lower()
# position = position.replace(" ", "")
# print(position, 1)

# row = ord(position[0].upper()) - ord('A')
# col = int(position[1:]) - 1

# print(row, col)

filename = 'cancel'

if filename == 'cancel' or filename == 'hi':
    print("'hi'")