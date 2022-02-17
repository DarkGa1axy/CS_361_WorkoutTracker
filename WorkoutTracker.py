import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


from tkinter import ttk
from tkinter.messagebox import askyesno

current_page = 1
started_workout = 0
home_page = 1
workouts = ["Push Workout: 11:00am", "Yoga Session: 6:00pm"]
completed_workouts = ["Pull Workout: 6:00am"]

class App(tk.Tk):
 

    def __init__(self):
     
        
        super().__init__()

        self.title('Workout Tracker')
        self.geometry('700x500')
        self.resizable(True, True)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.button1 = ttk.Button(self, text='Home')
        self.button1['command'] = self.home
        self.button1.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

        self.button2 = ttk.Button(self, text='New Workout')
        self.button2['command'] = self.create_workout
        self.button2.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.button3 = ttk.Button(self, text='Completed Workouts')
        self.button3['command'] = self.completed_workouts
        self.button3.grid(column=2, row=2, sticky=tk.EW, padx=5, pady=5)
        
        self.button1.config(state="disabled")
        self.home()



    def completed_workouts(self):
        self.button3.config(state="disabled")
        self.button2.config(state="enabled")
        self.button1.config(state="enabled")
        global started_workout
        global current_page
        global workouts
        global completed_workouts

        def create_completed_workouts():
            self.pb = ttk.Progressbar(
                self,
                orient='horizontal',
                mode='determinate',
                length=200,
                
            )
            self.pb.grid(column=0, row=0, padx=10, pady=10)
            self.pb['value']= len(completed_workouts) / (len(workouts) + len(completed_workouts)) *100
            
            self.framepb = ttk.Frame(self)
            self.framepb.columnconfigure(0, weight=3)
            self.framepb.columnconfigure(1, weight=1)
            self.framepb.grid(column=1, row=0, padx=10, pady=10)
            
          

            ttk.Label(self.framepb, text='Workouts Today').grid(column=1, row=0, padx=10, pady=10)

            for x in range(len(completed_workouts)):
                ttk.Label(self.framepb, text=completed_workouts[x]).grid(column=1, row=x+1, padx=10, pady=10)
                
        
            
            

        if started_workout == 1:
                self.notebook.destroy()
                started_workout = 0

        if (current_page == 1):
           
            self.frame.destroy()
            create_completed_workouts()
            current_page = 3
            
        elif (current_page == 2): 
            
            self.listbox.destroy()
            create_completed_workouts()
            current_page = 3
          
        else:
            create_completed_workouts()
            current_page = 3

    def create_workout(self):
        self.button2.config(state="disabled")
        self.button3.config(state="enabled")
        self.button1.config(state="enabled")
        global started_workout
        global current_page
        global workouts
        langs = ('Push Workout', 'Pull Workout', 'Leg Workout', 'Running workout', 'Yoga Session', 'Custom Workout')
        
        

        def items_selected(event):
            selected_indices = self.listbox.curselection()

            def add_workout ():
                workouts.append(specific_workout + ": " + self.userinput.get())
                self.frameadd.destroy() 
                self.home()


            specific_workout = langs[selected_indices[0]]

            self.userinput = tk.StringVar()

            self.frameadd = ttk.Frame(self)
            self.frameadd.columnconfigure(0, weight=3)
            self.frameadd.columnconfigure(1, weight=1)
            self.frameadd.grid(column=2, row=0, padx=10, pady=10)
            
            ttk.Entry(self.frameadd, textvariable=self.userinput, width = 20).grid(column=0,row=0, padx = 10, pady = 10)

            ttk.Button(self.frameadd, text="Create Workout", command=add_workout).grid(column=0,row=1, padx = 10, pady = 10)


    
        def create_listbox():
            self.langs_var = tk.StringVar(value=langs)
            self.listbox = tk.Listbox(
                self,
                listvariable=self.langs_var,
                height=10,
                selectmode='extended')
            self.listbox.grid(column=1,row=0, padx = 10, pady = 10)
            self.listbox.bind('<<ListboxSelect>>', items_selected)

        if started_workout == 1:
                self.notebook.destroy()
                started_workout = 0
    
        if current_page == 1:
            
            self.frame.destroy()
            create_listbox()
            current_page = 2
          
        elif current_page == 3:
            
            self.framepb.destroy()
            self.pb.destroy()
            create_listbox()
            current_page = 2
         
        else:
        
            create_listbox()
            current_page = 2 

    def home(self):
        self.button3.config(state="enabled")
        self.button2.config(state="enabled")
        self.button1.config(state="disabled")
        global started_workout
        global current_page
        global workouts

        def delete_workout(workout_name):
            answer = askyesno(title='confirmation',
                    message='Are you sure you want to delete this workout?')
            if answer:
                workouts.remove(workout_name)
                self.frame.destroy()
                create_frame(len(workouts))

        def start_workout():
            global started_workout
            self.frame.destroy()
            self.notebook = ttk.Notebook(self)
            self.notebook.grid(column=1, row=0)

            self.frame1 = ttk.Frame(self.notebook, width=400, height=280)
            self.frame2 = ttk.Frame(self.notebook, width=400, height=280)
            self.frame3 = ttk.Frame(self.notebook, width=400, height=280)

            self.frame1.pack(fill='both', expand=True)
            self.frame2.pack(fill='both', expand=True)
            self.frame3.pack(fill='both', expand=True)

            self.notebook.add(self.frame1, text='First Exersize')
            self.notebook.add(self.frame2, text='Second Exersize')
            self.notebook.add(self.frame3, text='Third Exersize')

            self.text = tk.Label(self.frame1, text='3x8 dumbell press')
            self.text.pack(fill='both', expand=True)

            self.text = tk.Label(self.frame2, text='5x8 dumbell flys')
            self.text.pack(fill='both', expand=True)

            self.text = tk.Label(self.frame3, text='4x4 bench press at 80% of max weight')
            self.text.pack(fill='both', expand=True)
            

            started_workout = 1

        def complete_workout(workout):
            global completed_workouts
            completed_workouts.append(workout)
            workouts.remove(workout)
            self.frame.destroy()
            create_frame(len(workouts))
            

        def create_frame(num_workouts):
            self.frame = ttk.Frame(self)
            self.frame.columnconfigure(0, weight=3)
            self.frame.columnconfigure(1, weight=1)
            self.frame.grid(column=1, row=0, padx=10, pady=10)

            ttk.Label(self.frame, text='Workouts Today').grid(column=0, row=0, sticky=tk.W)

            for x in range(num_workouts): 
                ttk.Checkbutton(self.frame, text=workouts[x],command=lambda: complete_workout(workouts[x])).grid(column=0, row=x+1, sticky=tk.W)
                ttk.Button(self.frame, text='Start Workout',command=start_workout).grid(column=1, row=x+1, sticky=tk.W)
                ttk.Button(self.frame, text='Delete',command=lambda: delete_workout(workouts[x])).grid(column=2, row=x+1, sticky=tk.W)
        
        global home_page
        if home_page ==1:
            try: 
                self.notebook.destroy()
                home_page=0
            except:
                home_page=0

        if started_workout == 1:
            self.notebook.destroy()
            started_workout = 0

        if current_page == 2:
            self.listbox.destroy()
            create_frame(len(workouts))
            current_page = 1
           
        elif current_page == 3:
            self.framepb.destroy()
            self.pb.destroy()
            create_frame(len(workouts))
            current_page = 1

        else: 
            create_frame(len(workouts))
            current_page = 1

     

if __name__ == "__main__":
    
    app = App()
    app.mainloop()