from tkinter import *
from tkinter import messagebox
import base64
import os
import code




def main_screen():
    screen = Tk()
    screen.geometry("375x398")
    screen.title("DE App")

    def decrypt():
        password = code.get()

        if password == "1234":
            screen2 = Toplevel(screen)
            screen2.title("DECRYPTION")
            screen2.geometry("400x200")
            screen2.config(bg="#00bd58")

            message = text1.get(1.0, END)
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypt)

        elif password == "":
            messagebox.showerror("DECRYPTION", "Enter the password")

        elif password != "1234":
            messagebox.showerror("DECRYPTION ", "invalid password")

    def encrypt():
        password = code.get()

        if password == "1234":
            screen1 = Toplevel(screen)
            screen1.title("ENCRYPTION")
            screen1.geometry("400x200")
            screen1.config(bg="#ed3833")

            message = text1.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode("ascii")

            Label(screen1, text="ENCRYPTION", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = Text(screen1, font="roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, encrypt)

        elif password == "":
            messagebox.showerror("Encryption", "Enter the password")


        elif password != "1234":
            messagebox.showerror("Encryption", "invalid password")

    def reset():
        code.get()
        text1.delete(1.0, END)

    Label(text="Enter the text to be encrypted and decrypted", fg="black", font=13).place(x=10, y=10)
    text1 = Text(font="roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter the secret code for decryption", fg="black", font=13).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=45, bd=0, font=45, show="*").place(x=10, y=200, width=355, height=30)

    Button(text="ENCRYPTION", height=2, bg="#ed3833", width=23, fg="black", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPTION", height=2, bg="#00bd58", width=23, fg="black", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, bg="#1089ff", width=50, fg="black", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
