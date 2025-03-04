first_name = "Jasmine"
surname = "Davis"

full_name = first_name + " " + surname

# print(full_name)

greeting = "Hello"

# print((greeting + " ") * 3)

company = "CodeBytes"

# print(company[0])
# print(company[4])
# print(company[-1])

# print(company[0:4])
# print(company[4:])
# print(company[:4])

uppercase_name = full_name.upper()
lowercase_name = full_name.lower()

# print(uppercase_name)
# print(lowercase_name)

message = " Let's  learn Python! "
clean_message = message.strip()

# print(message)
# print(clean_message)

new_message = clean_message.replace("Python", "JavaScript")

# print(new_message)

find_word = clean_message.find("Python")
# find_word = clean_message.find("HTML")

# print(find_word)

bulletin = "Python! Python! Python!"
count_bulletin = bulletin.count("Python")

# print(count_bulletin)

welcome_message = f"Hi {first_name}, welcome to {company}."

# print(welcome_message)

# common_error = 'I don't know why this has caused an error.'
# common_error = "I don't know why this has caused an error."
common_error = 'I don\'t know why this has caused an error.'

# print(common_error)
