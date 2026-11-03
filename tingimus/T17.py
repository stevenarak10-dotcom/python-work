
correct_username = "student"
correct_password = "python"

username = input("Kasutajanimi: ")
password = input("Parool: ")

if username == correct_username and password == correct_password:
    print("Ligipääs lubatud.")
else:
    print("Ligipääs keelatud.")
