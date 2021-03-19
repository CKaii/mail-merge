with open('./Input/Letters/starting_letter.txt') as letter, open('./Input/Names/invited_names.txt') as guest_names:
    contents = letter.read()
    for name in guest_names:
        # removes the new line from each name
        revised_name = name.strip('\n')

        # replaces [name] with each invited individuals name
        contents_name = contents.replace('[name]', revised_name)

        # creates a new letter with each individuals name
        new_letter = open(f'./Output/ReadyToSend/letter_for_{revised_name}.txt', 'w')

        # updates new letter with starting letter template and updated name
        update_letter = new_letter.write(contents_name)