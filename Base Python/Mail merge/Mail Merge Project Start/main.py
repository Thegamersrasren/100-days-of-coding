

PLACEHOLDER = "[name]"

with open(r"C:\Users\garen\Documents\Project Work\Mail merge\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    names_list = names.readlines()

with open(r"C:\Users\garen\Documents\Project Work\Mail merge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter:
    letter_content = letter.read()
    
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        
        with open(fr"C:\Users\garen\Documents\Project Work\Mail merge\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as output_letter:
            output_letter.write(new_letter)
