from ollama import chat
from dotenv import load_dotenv
import os



class AI_Agent:
    def __init__(self):
        self.model = "granite3.2:8b"
    
    def summarize(self, content):
        response = chat(
            model=self.model,
            messages = [
                {
                    "role": "system",
                    "content": """
                You are the article summarizer
                You job is taking the provided content of an article then summarize to make it less than 300 words
                You have to keep the summary to cover all essential content of the original article
                You must not omit any bullet points
                Just return me paragraphs of text with NO markdown or decorations. Paragraphs are separated
                """
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
            )
        return response["message"]["content"]

    def get_keyword(self, prompt):
        prompt = prompt.strip()
        if len(prompt.split(" ")) < 5:
            return prompt
        if not prompt: 
            return ""
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
                You are the keyword generator,
                You will be provided a text
                From that text, you will create NO more than 3 words to effectively search for news on the Internet
                The returning string MUST NOT include any quotes or double quotes wrapping

                Strict Rules:
                - ALWAYS return NO more than 3 words
                - NEVER return anything rather than 3 words
                - Return keyword WITHOUT quotes or double quotes
                """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ])
        return response["message"]["content"]