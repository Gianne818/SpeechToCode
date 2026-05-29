from customtkinter import *
import customtkinter

from gemini import AIBackend

class OutputWindow(customtkinter.CTk):
    def __init__(self, api_key):
        super().__init__()
        self.geometry("600x200")
        self.resizable(0, 0)
        self.title("AI Formatter")

        self.ai_backend = AIBackend(api_key=api_key)

        self.text_label = CTkLabel(master=self, text="AI will format any text you entered below. Using your native text-to-speech is recommended.")
        self.text_label.pack(padx=10)

        self.entry_title = CTkLabel(master=self, text="Enter text to format below", font=("Arial", 20, "bold"))
        self.entry_title.pack(pady=(20, 0), padx=20, anchor="w")                           
        
        self.textbox = CTkTextbox(master=self, height=75)
        self.textbox.pack(padx=20, fill="x")

        self.button = CTkButton(master=self, text="Submit", command=self.process_text)
        self.button.pack(pady=10, padx=20, fill="x")

    def process_text(self):
        user_input = self.textbox.get("1.0", "end").strip()
        if not user_input: return

        self.button.configure(state="disabled", text="Processing...")
        self.update()

        response = self.ai_backend.query(user_input)
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", response)

        self.clipboard_append(response)
        self.update()
        self.button.configure(state="normal", text="Submit")



