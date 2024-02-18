class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def list_books(self):
        print("*** List of Books ***")
        self.file.seek(0) 
        books = self.file.readlines()
        for i, line in enumerate(books, 1):
            book_info = line.strip().split(",")
            book_title = book_info[0]
            book_author = book_info[1]
            print(f"{i}- {book_title} by {book_author}")

    def add_book(self):
        book_title = input("Enter the title of the book: ").strip().lower() 
        book_author = input("Enter the author of the book: ")

        #Sorun: kullanıcı yanlışlıkla tarihe 198e yazabilir
        #yayınlandığı tarih ve sayfa sayısında harf olamayacak
        while True:
            release_year = input("Enter the release year of the book (must be a number): ")
            if release_year.isdigit():
                release_year = int(release_year)
                break
            else:
                print("Invalid input. Please enter a valid number for the release year.")
        
        while True:
            num_pages = input("Enter the number of pages of the book (must be a number): ")    
            if num_pages.isdigit():
                num_pages = int(num_pages)
                break
            else:
                print("Invalid input. Please enter a valid number for the number of pages.")

        #Sorun: kullanıcı yanlışlıkla fazladan boşluk bırakabilir ("Harry  Potter" veya " Harry Potter "gibi) ve aynı kitabı tekrar ekleyebilir
        #kitabın yanlarında ve eğer iki kelimeliyse (Harry Potter) gibi ortasında boşluk kalmasın diye eklendi 
        self.file.seek(0)
        for line in self.file:
            existing_book_title = line.strip().split(",")[0].strip().lower()  
            if existing_book_title.replace(" ", "") == book_title.replace(" ", ""):
                print(f"The book '{book_title}' already exists in the library.")
                return

        # Eğer kitap kütüphanede yoksa kütüphaneye ekler ve sadece adını ve yazarını gösterir
        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"{book_title} by {book_author} has been added to the library.")

    def remove_book(self):
        removed_book_title = input("Enter the title of the book to remove: ")
        lines = []
        removed = False

        # Dosyadaki tüm satırları okur ve bunları bir listede saklar
        self.file.seek(0)  
        for line in self.file:
            lines.append(line.strip())

        # list'ten bütün kitapları siler
        for i, line in enumerate(lines):
            book_info = line.split(",")
            if book_info[0].strip().lower().replace(" ", "") == removed_book_title.strip().lower().replace(" ", ""):
                del lines[i]
                removed = True
                break

        if removed == True:
            # çıkarılan kitap harici diğer kitapları dosyaya yazdırır
            with open("books.txt", "w") as file:
                for line in lines:
                    file.write(line + "\n")
            
            print(f"{removed_book_title} has been removed from the library.")
        else:
            print(f"{removed_book_title} was not found in the library.")

    def count_books(self): #kullanıcı kaç tane kitap olduğunu bilemk ister diye eklendi 500 kitap varsa teker teker saymasın
        self.file.seek(0) 
        num_books = sum(1 for line in self.file)
        print(f"There are {num_books} books in the library.")

lib = Library()
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Count Books")
    print("q) Quit")
    choice = input("Enter your choice (1/2/3/4/q): ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.count_books()
    elif choice.lower() == "q":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please choose again.")
