from langchain_ollama import ChatOllama

from config import MODEL_NAME
from tools.search_tool import search_tool
from tools.wiki_tool import wiki_tool
from tools.rag_tool import search_documents


class ResearchAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model=MODEL_NAME,
            temperature=0.2
        )

    def _get_web_data(self, topic: str) -> str:
        try:
            return search_tool.run(topic)
        except Exception as err:
            return f"Web search failed: {err}"

    def _get_wiki_data(self, topic: str) -> str:
        try:
            return wiki_tool.run(topic)
        except Exception as err:
            return f"Wikipedia search failed: {err}"

    def _get_document_data(self, topic: str) -> str:
        try:
            return search_documents(topic)
        except Exception as err:
            return f"Document retrieval failed: {err}"

    def collect_information(self, topic: str):

        web_results = self._get_web_data(topic)
        wiki_results = self._get_wiki_data(topic)
        document_context = self._get_document_data(topic)

        prompt = f"""
You are a research analyst.

Your task is to gather information from multiple sources and create
a clean research summary.

Research Topic:
{topic}

WEB SEARCH RESULTS:
{web_results}

WIKIPEDIA RESULTS:
{wiki_results}

DOCUMENT RESULTS:
{document_context}

Instructions:

1. Extract the most relevant information.
2. Remove duplicates.
3. Highlight important insights.
4. Mention statistics if available.
5. Mention recent developments if available.
6. Keep the response concise and factual.

Return the output in this format:

Topic:
Key Findings:
Important Facts:
Recent Developments:
Sources Used:
"""

        response = self.llm.invoke(prompt)

        return {
            "topic": topic,
            "web_results": web_results,
            "wiki_results": wiki_results,
            "document_context": document_context,
            "research_summary": response.content
        }