import streamlit as st
from transformers import pipeline

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering")

# Streamlit app layout
def main():
    st.title("Question Answering System")

    # Text input for context
    context = st.text_area("Enter the context:", height=300)

    # Text input for the question
    question = st.text_input("Enter your question:")

    # Perform question-answering when context and question are provided
    if context and question:
        with st.spinner('Processing...'):
            result = qa_pipeline(question=question, context=context)
            st.write("Answer:", result['answer'])
            st.write("Score:", result['score'])

# Run the Streamlit app
if __name__ == "__main__":
    main()
