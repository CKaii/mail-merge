with open('./Input/Letters/starting_letter.txt') as letter, open('./Input/Names/invited_names.txt') as guest_names:
    contents = letter.read()
    for name in guest_names:
        revised_name = name.strip('\n')
        contents_name = contents.replace('[name]', revised_name)
        # print(contents_name)
        new_letter = open(f'./Output/ReadyToSend/letter_for_{revised_name}.txt', 'w')
        update_letter = new_letter.write(contents_name)