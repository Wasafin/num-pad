from tkinter import *

# create window
window = Tk()
window.title('Number Pad')
window.geometry('250x300')

# create the number grid
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

# configure rows and colums to resize window
for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    # create and place labels in the grid
    for i in range(4):
        for j in range(3):
            frame = Frame(master=window, relief=RAISED, borderwidth=1, bg='#d0efff')
            frame.grid(row=i, column=j, sticky="nsew")

            label = Button(master=frame, text=nums[i][j], bg='#d0efff', font=('Arial', 18))
            label.pack(expand=True, fill='both', padx=2, pady=2)
            
window.mainloop()