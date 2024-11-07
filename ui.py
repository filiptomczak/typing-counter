from tkinter import *


class UserInterface():
    
    def __init__(self,root, wm, user, timer, calc):
        self.root = root
        self.root.title('typing test')
        self.root.config(padx=20,pady=20,bg='#efefef')
        self.labels=[]
        self.wm = wm

        self.user_entry = Entry(self.root)
        self.user=user
        self.user.set_entry(self.user_entry)
        self.user_entry.grid(column = 0, row=1, columnspan=5)
        self.user_entry.bind('<space>', lambda event: self.check_word(event) )

        self.create_labels(self.wm.words)

        self.timer = timer
        self.calc = calc
        self.counter_label = Label(self.root)
        self.counter_label.grid(column = 0, row=0, columnspan=5)

    def create_labels(self, words):
        row=2
        col=0        
        for word in self.wm.words:
            label = Label(self.root, text = word)
            label.config(padx=5,pady=2)
            label.grid(column=col,row=row)
            self.labels.append(label)
            col+=1
            if col != 0 and col%5 == 0:
                col=0
                row+=1
        self.highlight_label(self.wm.curr)

    def delete_labels(self):
        for l in self.labels:
            l.destroy()
        self.labels=[]
       
    def highlight_label(self, curr):
        if curr >= len(self.labels):
            self.delete_labels()
            self.wm.reset_values()
            self.create_labels(self.wm.words)
        else:
            self.labels[curr].config(foreground="green")
    
    def check_word(self, event):
        if(self.user.get_text()==self.wm.get_curr_word()):
            self.wm.curr+=1
            self.highlight_label(self.wm.curr)
            delta = self.timer.stop_time()
            chars_in_min = self.calc.chars_per_minute(len(self.user.get_text()),delta)
            self.counter_label.config(text ="{:.2f}".format( chars_in_min))
            self.user.clear_text()
        self.timer.start_time()


        return
        