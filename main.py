def write_to_diary(entry):
  with open("diary.txt", "a") as file:
    file.write(entry + "\n")
  print("Entry added to the diary.")

def read_diary():
  try:
    with open("diary.txt", "r") as file:
      print("Your diary entries:")
      print("--------------------")
      print(file.read())
  except FileNotFoundError:
    print("Your diary is empty. 404 Error")

def main():
  print("Welcome to Your Own Diary!")
  print("---------------------------")
  while True:
    print("\nWhat would you like to do?")
    print("1. Write an entry")
    print("2. Read your diary")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
      entry = input("Enter your diary entry: ")
      write_to_diary(entry)
    elif choice == "2":
      read_diary()
    elif choice == "3":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()