PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    template_file = open("Input/Letters/starting_letter.txt", "r")
    original_contents = template_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = original_contents.replace(PLACEHOLDER, stripped_name)
        new_file_path = f"Output/letter_for_{stripped_name}.txt"
        with open (new_file_path, "w") as file:
            file.write(new_letter)
