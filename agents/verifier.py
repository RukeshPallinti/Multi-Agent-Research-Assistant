from langchain_ollama import ChatOllama

from config import MODEL_NAME


class VerificationAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model=MODEL_NAME,
            temperature=0
        )

    def verify(
        self,
        topic: str,
        research_summary: str
    ):

        prompt = f"""
You are a fact-checking assistant.

Topic:
{topic}

Research Summary:
{research_summary}

Tasks:

1. Remove duplicate information.
2. Remove weak claims.
3. Highlight important findings.
4. Improve readability.
5. Keep references if available.

Return only the improved report.
"""

        response = self.llm.invoke(prompt)

        return response.content