import random

if __name__ == '__main__':
     print("Hello, Welcome to the Hangman Game.")
     file = open('words.txt','r')
     tempWords = file.read().splitlines()
     easyWords = []
     mediumWords = []
     hardWords = []
     lives = 6
     body = {6:'Left Arm',5:'Right Arm',4:'Left Leg',3:'Right Leg',2:'Torso',1:'Head'}
     diff = {"easy": easyWords, "medium": mediumWords, "hard": hardWords}
     for i in tempWords:
          if len(i) < 4:
             easyWords.append(i)
          elif len(i) >= 4 and len(i) < 7:
               mediumWords.append(i)
          else:
               hardWords.append(i)
     c = input("Choose Your Difficulty(Easy   Medium   Hard):").lower()
     word = random.choice(diff[c])
          