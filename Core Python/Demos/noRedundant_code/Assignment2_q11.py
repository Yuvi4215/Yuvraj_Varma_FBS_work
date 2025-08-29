### Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# Take The amount values from user
amount=int(input('Enter the amount value :: '))

notes=[500,200,100,50,20,10]
count=[0,0,0,0,0,0]
index=0

while amount>9:
    count[index]=amount//notes[index]
    amount=amount%notes[index]
    index+=1
    
print(f"""note count
       {notes[0]} :: {count[0]}
       {notes[1]} :: {count[1]}  
       {notes[2]} :: {count[2]} 
       {notes[3]} :: {count[3]} 
       {notes[4]} :: {count[4]} 
       coins :: {amount}""")