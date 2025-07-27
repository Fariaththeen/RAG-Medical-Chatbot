# Phase 10: Testing & Evaluation Plan

**Tester:** Fariaththeen
**Date:** 2025-07-24

## 1. Objective
To systematically evaluate the performance of the Medical RAG Assistant based on a series of test queries. The primary goal is to assess accuracy, relevance, and the system's ability to avoid hallucinations.

## 2. Evaluation Criteria

For each test query, we will assess the response based on the following:

*   **Accuracy:** Is the answer factually correct according to the source documents? (Scale 1-5, 5 being perfectly accurate).
*   **Relevance:** Does the answer directly address the question asked? (Scale 1-5, 5 being perfectly relevant).
*   **Contextual Soundness:** Does the answer come *only* from the retrieved context? Check the "Show Retrieved Context" expander in the app to verify.
*   **Hallucination Check:** Did the model invent any information not present in the context? (Yes/No).
*   **Responsiveness:** How long did it take to get an answer? (Subjective: Fast, Medium, Slow).

## 3. Testing Procedure

1.  Launch the Streamlit application: `streamlit run app.py`
2.  Ask the assistant a question from the "Test Cases" table below.
3.  Record the generated answer.
4.  Open the "Show Retrieved Context" expander and check if the retrieved chunks are relevant to the question.
5.  Rate the answer based on the criteria above and fill in the table.
6.  Repeat for all test cases.

## 4. Test Cases & Results Log

Copy the template below for each question you ask.

---

### Test Case 1: Factual Recall
*   **Question:** *<ins>Ask a very specific question that has a clear answer in your documents, e.g., "What is the recommended dosage of Paracetamol for an adult?"</ins>*
*   **Generated Answer:**
*   **Retrieved Context (Is it relevant?):**
*   **Accuracy (1-5):**
*   **Relevance (1-5):**
*   **Hallucination?:**
*   **Comments:**

---

### Test Case 2: Summarization
*   **Question:** *<ins>Ask for a summary of a topic, e.g., "Summarize the primary symptoms of hypertension."</ins>*
*   **Generated Answer:**
*   **Retrieved Context (Is it relevant?):**
*   **Accuracy (1-5):**
*   **Relevance (1-5):**
*   **Hallucination?:**
*   **Comments:**

---

### Test Case 3: Negative Testing (Out-of-Scope)
*   **Question:** *<ins>Ask a question that you are certain is NOT covered in your documents, e.g., "What are the rules of baseball?"</ins>*
*   **Generated Answer:**
*   **Retrieved Context (Is it relevant?):**
*   **Accuracy (1-5):** (A "5" here means the model correctly states it doesn't know).
*   **Relevance (1-5):**
*   **Hallucination?:**
*   **Comments:** The ideal response should be "I cannot find the information in the provided documents."

---