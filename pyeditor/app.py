import tkinter as tk
from tkinter import filedialog


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.menubar = tk.Menu()
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Salvar", command=self.on_save_file)
        filemenu.add_command(label="Abrir", command=self.on_open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=self.master.quit)
        self.menubar.add_cascade(label="Arquivo", menu=filemenu)

        self.content = tk.Text(
            self,
            # Will fill screen as it is resized
            width=self.master.winfo_vrootwidth(),
            height=self.master.winfo_vrootheight()
        )
        self.content.focus()
        self.content.pack(
            fill=tk.BOTH,
            expand=True
        )

    def on_save_file(self):
        curr_content = self.content.get("1.0", "end-1c")
        filename = filedialog.asksaveasfilename(
            filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")]
        )
        if filename:
            with open(filename, "w") as f:
                f.write(curr_content)
            f.close()

    def on_open_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")]
        )

        if filename != "":
            self.content.delete("1.0", "end-1c")
            with open(filename, "r", encoding="UTF-8") as f:
                text = f.read()
                self.content.insert("end-1c", text)
            f.close()


def main():
    root = tk.Tk()
    root.update()
    
    # Define initial size
    root.geometry("800x400")

    app = App(root)
    app.master.config(menu=app.menubar)
    app.master.title("Pyeditor")
    app.mainloop()


if __name__ == "__main__":
    main()
