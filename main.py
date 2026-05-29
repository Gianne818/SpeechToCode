from customtkinter import *
import customtkinter
from database import init_db, save_key
from outputs import OutputWindow

class MainWindow(customtkinter.CTk):
    def __init__(self, on_success_callback):
        super().__init__()
        self.geometry("600x200")
        self.title("AI Formatter")
        self.resizable(0, 0)
        self.on_success = on_success_callback

        self.welcome_title = CTkLabel(master=self, text="Welcome!", font=("Arial", 28, "bold"))
        self.welcome_title.pack(pady=10)

        self.text1 = CTkLabel(master=self, text="Your Gemini API Key")
        self.api_key_entry = CTkEntry(master=self, width=500, placeholder_text="Your gemini API key goes here...")
        self.api_key_entry.pack(pady=(40, 10))

        saved_key = init_db()
        if saved_key:
            self.api_key_entry.insert(0, saved_key)
            

        button = CTkButton(master=self, text="Continue", command = self.on_continue)
        button.pack(pady=10)



    def on_continue(self):
        user_key = self.api_key_entry.get().strip()
        if(user_key):
            save_key(user_key)
            self.on_success(user_key)

class AppController:
    def __init__(self):
        self.api_key = None
        self.setup_win = None
        self.main_win = None

        self.run_flow()

    def run_flow(self):
        self.setup_win = MainWindow(on_success_callback=self.show_outputs)
        self.setup_win.focus_force()
        self.setup_win.lift()
        self.setup_win.mainloop()

    def show_outputs(self, api_key):
        self.api_key = api_key;
        self.setup_win.destroy()
        self.main_win = OutputWindow(api_key=self.api_key)
        self.main_win.lift()
        self.main_win.mainloop()


if __name__ == "__main__":
    app = AppController()