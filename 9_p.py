#HANGMAN GAME
import random

word=("apple","banana","orange","pineapple","coconut","truck", 'feeling','time','love')

hangman_art={0:("    ",
                "    ",
                "    "),
            1: ("  o  ",
                "    ",
                "    "),
            2: ("  o  ",
                "  |  ",
                "    "),
            3: ("  o  ",
                " /|  ",
                "    "),
            4: ("  o  ",
                " /|\\ ",
                "    "),
            5: ("  o  ",
                " /|\\ ",
                " /    "),
            6: ("  o  ",
                " /|\\ ",
                " /'\\ ")
    
} 
def display_man(wrong_guesses):
    print("=====================================")
    for line in hangman_art[wrong_guesses]:
        print (line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def display_hint(hint)  :
    print(" ".join(hint))
    
def display_answer(answer) :
    print(" ".join(answer))
def main() :
    answer = random.choice(word)
    hint = ['_']*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True
    
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
            
        guess=input("enter a letter:").lower()
        
        if len(guess)!=1:
            print ("INVALID ANSWER \n please enter a single letter")
        #elif guess != guess.isalpha():
            print ("INVALID ANSWER\n please enter a letter")    
            
            
            
            continue
        
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                
        else:
            wrong_guesses+=1    
        
        
        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("<<<<<<<<<<<<you win>>>>>>>>>>>")
            is_running=False
        elif wrong_guesses >=len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("<<<<<<<<<<you lose>>>>>>>") 
            is_running=False

if __name__=="__main__":
    main()
    
