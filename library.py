books = {
    1: "Reply 1998",
    2: "Teach You Lesson", 
    3: "Harry Potter",
    4: "Atomic Habits",
    5: "Wings of Fire"
}

search_id = int(input("Enter Book ID: "))
print(books.get(search_id, "Book ID not found"))