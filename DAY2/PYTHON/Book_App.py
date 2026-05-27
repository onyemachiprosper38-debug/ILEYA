import random

books = [
    "The Hobbit",
    "Harry Potter",
    "Atomic Habits",
    "Rich Dad Poor Dad"
]


def get_suggestion():

    answer = "yes"

    while answer == "yes":

       
        random_book = random.choice(books)

        
        random_page = random.randint(1, 100)

      
        print("\nSuggested Book:", random_book)
        print("Start from page:", random_page)

       
        answer = input("\nDo you want another suggestion? yes/no: ")

    print("Suggestion stopped.")



def add_book():

    new_book = input("Enter new book name: ")

    
    books.append(new_book)

    print("Book added successfully.")



def remove_book():

    remove_name = input("Enter book name to remove: ")

    
    books.remove(remove_name)

    print("Book removed successfully.")



def update_book():

    
    for i in range(len(books)):
        print(i, books[i])

    
    index = int(input("Enter index number to update: "))

    
    new_book = input("Enter new book name: ")

    
    books.pop(index)

   
    books.insert(index, new_book)

    print("Book updated successfully.")



def show_books():

    print("\nAll Books:")

    for book in books:
        print(book)



while True:

    print("\n===== BOOK SUGGESTION SYSTEM =====")
    print("1. Get Suggestion")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Update Book")
    print("5. Show All Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        get_suggestion()

    elif choice == "2":
        add_book()

    elif choice == "3":
        remove_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        show_books()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice")
