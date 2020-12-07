import tkinter as tk
from random import randint

root = tk.Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")


def pick():
    entries = ['Sanbid Roy Chowdhury', 'The refuge Malik', 'Google India', 'DotDotCom', 'Jon Layman', 'Itz Omen',
               'Roberto Picco', 'Adigun olamide', 'Saurabh Parate', 'Exceptional Faruk', 'Avinash Upadhyaya',
               'Fabio F. de Aquino', 'Ganesh Hegde', 'Hardy Don', 'Trap Town NCS', 'NIRMAL SRINIVAS CHINTALA', 'Weston',
               'Gavin Hou', 'Bhanumathi A', 'Faoud Mohd ', 'rocket science', 'LucaVont', 'Kristian Simko', 'LunarAtom',
               'Code With Wasif', 'Shreyas shetty', 'Panagiotis V', 'Dan Esquibel', 'TechiesSpammer69', 'John Dripper',
               'Barbossa', 'Sahan Eakanayaka', 'Cassio Lacaz', 'Ranga bharath', 'Kisalay Suman', 'Le Dung', 'Mildo',
               'Ivan Yosifov', 'Shreyas shetty', 'pranav Bhatki', 'Atharv Nuthi', 'Tibas Tiba', 'Yash Thakkar', 'Dario',
               'deranged llama', 'Tom Blackwood', 'Christian Dimayacyac', 'Shaun A', 'Tchosk', 'Ahsan Arain',
               'GRANDHI NAGESHWARAO', 'Baby Daily Life', 'PERFECT IGBADUMHE', 'Amad Ahmed', 'benage andy',
               'Gerald Minoza', 'Samuel Hafer', 'Augusto Sousa', 'Andreas Mls', 'Somali flame', 'GPSSerbia',
               'Hima Subedi', 'Ignatus Nana Amoah', 'Videos Promoter', 'Nabil Fantes', 'collins anele', 'Utku Yucel',
               'Robert Coffie', 'M Dandan', 'Hudaibia Syed', 'abdurrahman zakariya', 'sabin katwal', 'Hardy Don',
               'v sr', '10 bitangaje', 'Jon Bascos', 'Gaming Hub', 'Ace Hardy', 'Arsh Bains', 'Hima Subedi',
               'Samuel Hafer', 'Fake Account', 'Spider', 'Callum Telford', 'Nikola Franicevic', 'David Blankinship',
               'Unison', 'ramona Saintandre', 'Mohan hari krishna']
    entries_set = set(entries)
    unique_entries = list(entries_set)

    # create list size variable
    our_number = len(unique_entries) - 1
    # create a random number between 0 and len(unique_entries)
    rando = randint(0, our_number)

    winnerLabel = tk.Label(root, text=unique_entries[rando], font=("Helvetica", 24))
    winnerLabel.pack(pady=50)


topLabel = tk.Label(root, text="Win-O-Rama!", font=("Helvetica", 24))
topLabel.pack(pady=20)

winButton = tk.Button(root, text="Pick OUR WINNER", font=("Helvetica", 24), command=pick)
winButton.pack(pady=20)

root.mainloop()