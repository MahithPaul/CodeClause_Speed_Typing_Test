#Required Libraries
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.title('CodeClause | Golden Project - Speed Typing')
root.geometry('850x500')
root.config(background="#090f19")
my_password = chr(randint(33, 126))



def click():

    #------------------------Creating Class For Finding Speed Typing-------------------------------

    class tester:
        def __init__(self, paragraph):
            self.correctWords = []
            self.typedWords = []
            self.incorrectWords = {}
            self.totalWords = []
            self.input = None
            self.paragraph = paragraph
            self.accuracy = 0
            self.time = 0
            self.wordPermin = 0
            self.run()


        #----------------Functions that run operations-------------------

        def clock(self):
            while len(self.typedWords) == 0:
                self.time += 1
                time.sleep(1)

        def run(self):
            threading.Thread(target=self.clock).start()
            threading.Thread(target=self.testSpeed).start()

        def testSpeed(self):
            print('\n\n'+self.paragraph+'\n\n')
            self.input = str(my_entry.get())
            self.totalWords = self.paragraph.split(' ')
            self.typedWords = self.input.split(' ')

            try:
                for i in range(len(self.typedWords)):
                    if (self.typedWords[i] == self.totalWords[i]):
                        self.correctWords.append(self.typedWords[i])
                    else:
                        self.incorrectWords.update({self.totalWords[i]: self.typedWords[i]})

            except Exception as e:
                print(e)

            self.accuracy = len(self.correctWords)/len(self.typedWords) * 100
            self.wordPerMin = len(self.typedWords) / (self.time/60)

            #--------Display in screen as output----------------

            my_accuracy.config(text="Accuracy: "+str(self.accuracy))
            my_words.config(text="Word Per Minute : "+str(self.wordPerMin))
            my_incorrect.config(text="Incorrect Words "+str(self.incorrectWords))


    Mytester = tester("I'm not a great programmer; I'm just a good programmer with great habits")

#----------------Text to type in Entry----------------------------
my_title = Label(root,text="Typing Speed Test",bg="#090f19", fg="#F9D949" ,font=("Helvetica",26,"bold"))
my_title.place(x=270,y=15)
my_word = Label(root,text="I'm not a great programmer; I'm just a good programmer",bg="#090f19", fg="#fff" ,font=("Helvetica",22,"bold"))
my_word.place(x=20,y=70)

my_word1 = Label(root,text="with great habits",bg="#090f19", fg="#fff" ,font=("Helvetica",22,"bold"))
my_word1.place(x=20,y=120)


my_label = LabelFrame(root, text="Type Here",bg="#2D2727", fg="#fff", font=("Helvetica", 18, "bold"))
my_label.place(x=20,y=180)

#---------------Entry Box for text input----------------

my_entry = Entry(my_label, font=("Helvetica", 24),width=30)
my_entry.pack(pady=20, padx=20)


#------------------Result Labels--------------------

my_accuracy = Label(root,bg="#090f19", fg="#fff", font=("Helvetica", 20) )
my_accuracy.place(x=70,y=320)

my_words = Label(root, bg="#090f19", fg="#fff", font=("Helvetica", 20) )
my_words.place(x=70,y=360)

my_incorrect = Label(root, bg="#090f19", fg="#fff", font=("Helvetica", 20) )
my_incorrect.place(x=70,y=400)

#-------------------Generate Button-------------------------

my_btn = Button(root, command=click, text="Generate",bg="#002B5B", fg="#fff" ,font=("Helvetica", 20))
my_btn.place(x=650,y=200)

root.mainloop()
