import os
import streamlit as st

from graph.workflow import workflow

from tools.rag_tool import build_vector_store
from tools.pdf_generator import generate_pdf_report

from config import UPLOAD_DIR


st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Multi-Agent Research Assistant")
st.markdown(
    "Research, verify information, retrieve knowledge from uploaded PDFs, and generate professional reports."
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

# ------------------------
# Sidebar
# ------------------------

with st.sidebar:

    st.header("Document Upload")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        save_path = os.path.join(
            UPLOAD_DIR,
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner(
            "Processing document..."
        ):

            result = build_vector_store(
                save_path
            )

        st.success(
            f"Document processed successfully."
        )

        st.info(
            f"Chunks created: {result['chunks_created']}"
        )

# ------------------------
# Main Section
# ------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Future of Agentic AI in Healthcare"
)

generate_button = st.button(
    "Generate Report"
)

if generate_button:

    if not topic.strip():

        st.warning(
            "Please enter a research topic."
        )

    else:

        progress = st.progress(0)

        status = st.empty()

        status.info(
            "Running Research Agent..."
        )

        progress.progress(20)

        result = workflow.invoke(
            {
                "topic": topic
            }
        )

        progress.progress(80)

        status.info(
            "Generating PDF Report..."
        )

        pdf_path = generate_pdf_report(
            topic,
            result["final_report"]
        )

        progress.progress(100)

        status.success(
            "Report generated successfully."
        )

        st.subheader(
            "Report Preview"
        )

        st.markdown(
            result["final_report"]
        )

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="Download PDF Report",
                data=pdf_file,
                file_name=os.path.basename(pdf_path),
                mime="application/pdf"
            )