from google import genai

class AIBackend():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)

    def query(self, text_input):
        message = """Format the inputted text. It could be a normal text, or a code that you need to format properly. 
        Strictly output only the formatted text. Plain text only, no codeblocks or other formattings.
        If you think its a code, there might be times where the capitalizations are messed up. Use the coding name conventions."""
        content_parts = [message]

        content_parts.append(text_input)
        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=content_parts
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"