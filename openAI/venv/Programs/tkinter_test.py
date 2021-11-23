import tkinter

tk = tkinter.Tk()
tk.geometry("500x200")
tk.title("Voice Assistant")
text = tkinter.Text(tk)
text.tag_configure("bold", font="Helvetica 10 bold")
text.pack()
text.insert(tkinter.END, "hello\n")
text.insert(tkinter.END, "hello")

text.insert("end", "Hello, ")
text.insert("end", "world", "bold")
tk.mainloop()
