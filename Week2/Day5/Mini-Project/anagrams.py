from anagram_checker import  AnagramChecker

def main():
        sowpods_checker = AnagramChecker('/sowpods.txt')
        user_word = ''
        while user_word.lower() != 'x':
            user_input = input('Please enter your word to check or "x" to exit: ')
            user_word = user_input.lower()
            
            if user_input=='x':
                pass
            elif user_input.isalpha():
                sowpods_checker.get_anagrams(user_word)
            else:
                print('Sorry, invalid input.')

        print('Goodbye!')
    

 
main()











