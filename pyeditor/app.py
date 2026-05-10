import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.saveas_btn = tk.Button(self, text="Salvar", command=self.on_save_file)
        self.saveas_btn.pack()

        self.content = tk.Text(self)
        self.content.pack()
    
    def on_save_file(self):
        content = self.content.get("1.0", "end-1c")
        print(content)

root = tk.Tk()
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

app = App(root)
app.master.title('Pyeditor')
app.mainloop()