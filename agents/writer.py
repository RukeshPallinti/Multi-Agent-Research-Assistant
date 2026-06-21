from langchain_ollama import ChatOllama

from config import MODEL_NAME


class WriterAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model=MODEL_NAME,
            temperature=0.3
        )

    def write_report(
        self,
        topic: str,
        verified_content: str,
        document_context: str = ""  # ← receives PDF chunks
    ):

        prompt = f"""
Create a professional research report.

Topic:
{topic}

IMPORTANT: The Document Context below comes from the uploaded PDF.
Treat it as your PRIMARY source. Use Verified Findings only to
supplement any gaps not covered by the document.

Document Context (from uploaded PDF — use this first):
{document_context}

Verified Findings (supplementary only):
{verified_content}

Structure:

# Executive Summary

# Key Findings

# Detailed Analysis

# Conclusion

# References

Use professional language. Where information comes from the uploaded
document, reflect that accurately. Do not invent facts not present
in the sources above.
"""

        response = self.llm.invoke(prompt)

        return response.content