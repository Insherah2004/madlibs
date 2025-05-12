import tkinter as tk

def create_madlib():
    adjective1 = adj1_entry.get()
    place = place_entry.get()
    verb = verb_entry.get()
    adjective2 = adj2_entry.get()
    animal = animal_entry.get()
    past_verb = past_verb_entry.get()
    plural_noun = plural_noun_entry.get()
    adjective3 = adj3_entry.get()
    
    madlib = f"Yesterday me and my {adjective1} friend went to a {place} to {verb}.\
    We saw a {adjective2} {animal} that {past_verb} in front of us.\
    We laughed so hard that we dropped our {plural_noun}. It was the {adjective3} day ever."
    
    output_label.config(text=madlib)
    
# Creating the main window
root = tk.Tk()
root.title('MadLib Games')
root.geometry('700x700')
    
# Input labels and fields
tk.Label(root, text= 'Enter an adjective:').pack()
adj1_entry = tk.Entry(root, width = 40)
adj1_entry.pack()
    
tk.Label(root, text='Enter a place:').pack()
place_entry = tk.Entry(root, width = 40)
place_entry.pack()

tk.Label(root, text = 'Enter a verb:').pack()
verb_entry = tk.Entry(root, width = 40)
verb_entry.pack()
    
tk.Label(root, text = 'Enter another adjective:').pack()
adj2_entry = tk.Entry(root, width = 40)
adj2_entry.pack()
    
tk.Label(root, text = 'Enter a animal:').pack()
animal_entry = tk.Entry(root, width = 40)
animal_entry.pack()
    
tk.Label(root, text = 'Enter a past verb:').pack()
past_verb_entry = tk.Entry(root, width = 40)
past_verb_entry.pack()
    
tk.Label(root, text = 'Enter a plural Noun:').pack()
plural_noun_entry = tk.Entry(root, width = 40)
plural_noun_entry.pack()
    
tk.Label(root, text = 'Enter another adjective:').pack()
adj3_entry = tk.Entry(root, width = 40)
adj3_entry.pack()
    
# Submit Button
submit_button = tk.Button(root, text = 'GET YOUR MADLIB STORY!', command=create_madlib)
submit_button.pack(pady = 10)
    
output_label = tk.Label(root, text = '', wraplength=450, justify='left', font=('Arial', 14), padx = 10, pady = 10)
output_label.pack()
    
# Run the GUI loop
root.mainloop()
    