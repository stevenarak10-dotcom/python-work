age = 20
has_ticket = True
print(age >= 18 and has_ticket)  # true
print(age < 18 or has_ticket)  # true
print(age >= 18 and not has_ticket)  # false
print(not (age < 18 or has_ticket))  # false
