import sqlite3
conn = sqlite3.connect("contact.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contact (
    contact_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
)
''')
conn.commit()
def add():
    a = input("Enter your id: ")
    b = input("Enter your name: ")
    c = input("Enter your phone: ")
    d = input("Enter your email: ")
    cursor.execute("INSERT INTO contact(contact_id,name, phone, email) VALUES (?, ?, ?,?)",(a,b,c,d))
    conn.commit()
    print("Your contact has been added")
def view():
    print("Displaying the records:")
    cursor.execute("SELECT * FROM contact")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def update():
    a = input("Enter the id you want to update: ")
    b = input("Enter the new name: ")
    c = input("Enter the new phone: ")
    d = input("Enter the new email: ")
    cursor.execute("UPDATE contact SET contact_id = ? name = ? phone = ? email = ?)",(a,b,c,d))
    conn.commit()
    print("Your contact has been updated")
def remove():
    a = input("Enter the id you want to remove: ")
    cursor.execute("DELETE FROM contact WHERE contact_id = ?",(a,))
    conn.commit()
    print("Your contact has been removed")
conn.commit()
while True:
    choice=int(input("=== Contact Management ===\n\t 1.Add contact\n\t 2.View contact\n\t 3.Delete contact\n\t 4.Update contact\n\t 5.Exit\n\t"))
    if choice == 5:
        print("Exiting")
        break
    elif choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        remove()
    elif choice == 4:
        update()
    else:
        print("Enter a valid option")
conn.close()