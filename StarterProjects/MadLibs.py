def get_input(word_type: str):
    user_input: str = input(f'Please enter a {word_type}: ')
    return user_input


noun1 = get_input('noun')
verb1 = get_input('verb')
adjective = get_input('adjective')
noun2 = get_input('noun')
verb2 = get_input('verb')

story = f'''
Once upon a time, there was a {noun1} who used to {verb1}.

One day, {noun1} found an {adjective} {noun2} and decided to {verb2} it.

'''
print(story)