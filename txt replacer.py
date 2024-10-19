import nltk
import os
from dotenv import load_dotenv, dotenv_values

# Specify the local NLTK data directory
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
nltk.data.path.append(nltk_data_dir)
def replace_verbs(text, replacement_word):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Tag the parts of speech
    pos_tags = nltk.pos_tag(words)
    
    # Replace verbs with the replacement word
    replaced_text = ' '.join([replacement_word if tag.startswith('VB') else word for word, tag in pos_tags])
    
    return replaced_text
# start menu
def starting_menu():
    print('start')
    print('exit')
    choice=str(input()).lower()
    return choice


result=starting_menu()
if result == 'start':
    while True:
        print('to exit type exit')
        print('please enter the word that replaces verbs:\n')
        replacement = str(input())
        print('please enter the text to replace:\n')
        result= str(input())

        if result == 'exit':
            starting_menu()
            break
        
        
        output_text = replace_verbs(result, replacement)

        print(output_text)



elif result =='exit':
    exit()
else:
    print('please enter a valid resopnse')
    starting_menu()
