from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from agents.researcher import ResearchAgent
from agents.verifier import VerificationAgent
from agents.writer import WriterAgent

from tools.rag_tool import search_documents


research_agent = ResearchAgent()
verification_agent = VerificationAgent()
writer_agent = WriterAgent()


class ResearchState(TypedDict):

    topic: str

    research_summary: str

    document_context: str

    verified_content: str

    final_report: str


def research_node(state):

    result = research_agent.collect_information(
        state["topic"]
    )

    return {
        "research_summary": result["research_summary"]
    }


def retrieval_node(state):

    context = search_documents(
        state["topic"]
    )

    return {
        "document_context": context
    }


def verification_node(state):

    combined_content = f"""
Research Summary:

{state['research_summary']}

Document Context:

{state['document_context']}
"""

    verified = verification_agent.verify(
        state["topic"],
        combined_content
    )

    return {
        "verified_content": verified
    }


def writer_node(state):

    report = writer_agent.write_report(
        state["topic"],
        state["verified_content"],
        state["document_context"]  # ← FIXED: now passing PDF context to writer
    )

    return {
        "final_report": report
    }


graph_builder = StateGraph(
    ResearchState
)

graph_builder.add_node(
    "research",
    research_node
)

graph_builder.add_node(
    "retrieval",
    retrieval_node
)

graph_builder.add_node(
    "verification",
    verification_node
)

graph_builder.add_node(
    "writer",
    writer_node
)

graph_builder.set_entry_point(
    "research"
)

graph_builder.add_edge(
    "research",
    "retrieval"
)

graph_builder.add_edge(
    "retrieval",
    "verification"
)

graph_builder.add_edge(
    "verification",
    "writer"
)

graph_builder.add_edge(
    "writer",
    END
)

workflow = graph_builder.compile()