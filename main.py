"""
Auto Translate Desktop App
This app will translate all information from file1 to English language and write it to file2
"""
from ctypes import windll

from googletrans import Translator
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.font


class App:
    """ Application class """

    def open_file1(self):
        """ Opens filedialog and writes user chosen file path to the variable """

        path = tkinter.filedialog.askopenfilename()
        if path:
            self.file1_path = path
        self.file1_path_label.config(text=self.file1_path)

    def open_file2(self):
        """ Opens filedialog and writes user chosen file path to the variable """

        path = tkinter.filedialog.askopenfilename()
        if path:
            self.file2_path = path
        self.file2_path_label.config(text=self.file2_path)

    def translate(self, event=None):
        """ Main function """

        print(event)
        self.translator = Translator()
        with open(self.file1_path, "r", encoding="utf-8") as file1:
            with open(self.file2_path, "w", encoding="utf-8") as file2:
                for line in file1.readlines():
                    translated = self.translator.translate(line, dest="ru").text
                    print(line, translated)
                    file2.write(translated + "\n")

    def app_config(self):
        """ Application configuration variables """

        self.bg = "#222223"
        self.font = tkinter.font.Font(self.root, family="Verdana", size=15)
        self.fg = "white"

    def app_settings(self):
        """ Application settings """

        # stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
        windll.shcore.SetProcessDpiAwareness(1)
        self.root.title(self.name)
        self.root.geometry("640x480")
        self.root.config(bg=self.bg)

    def __init__(self, app_name):
        self.name = app_name

        self.root = tkinter.Tk()

        self.app_config()

        self.app_settings()

        self.description_label = tkinter.Label(self.root, text=f"Welcome to {self.name}\n"
                                                               f"Quickly translate chosen file using Google translate")
        self.description_label.config(bg=self.bg, font=self.font, fg=self.fg)
        self.description_label.pack(ipadx=30, ipady=30)

        self.select_file1_button = tkinter.Button(self.root, text="Select file to translate", command=self.open_file1)
        self.select_file1_button.config(bg=self.bg, font=self.font, fg=self.fg)
        self.select_file1_button.pack(ipadx=50, ipady=20, padx=10, pady=10)

        self.file1_path_label = tkinter.Label(self.root)
        self.file1_path_label.config(bg=self.bg, font=self.font, fg=self.fg)
        self.file1_path_label.pack()

        self.select_file2_button = tkinter.Button(self.root, text="Select file to write the translation", command=self.open_file2)
        self.select_file2_button.config(bg=self.bg, font=self.font, fg=self.fg)
        self.select_file2_button.pack(ipadx=50, ipady=20, padx=10, pady=10)

        self.file2_path_label = tkinter.Label(self.root)
        self.file2_path_label.config(bg=self.bg, font=self.font, fg=self.fg)
        self.file2_path_label.pack()

        self.translate_button = tkinter.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.config(bg=self.bg, font=self.font, fg=self.fg)
        self.translate_button.pack(ipadx=50, ipady=20, padx=10, pady=10)

        self.root.mainloop()


if __name__ == '__main__':
    app = App("Auto Translate")
