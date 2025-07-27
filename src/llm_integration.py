from gpt4all import GPT4All
from rag_pipeline import retrieve_relevant_chunks, build_prompt

def initialize_llm(model_name: str = "mistral-7b-instruct-v0.1.Q4_0.gguf"):
    """
    Initializes and returns a GPT4All language model.

    Args:
        model_name: The name of the model file to use.

    Returns:
        An instance of the GPT4All model.
    """
    print(f"Initializing LLM with model: {model_name}")
    # The first time you run this, it will download the model (a few GB).
    # Subsequent runs will use the cached model.
    model = GPT4All(model_name)
    print("LLM initialized successfully.")
    return model

def generate_answer(model: GPT4All, prompt: str) -> str:
    """
    Generates an answer using the LLM based on the provided prompt.

    Args:
        model: The initialized GPT4All model.
        prompt: The full prompt including context and the user's question.

    Returns:
        The generated answer as a string.
    """
    print("Generating answer...")
    output = model.generate(
        prompt=prompt,
        max_tokens=512,  # Adjust as needed
        temp=0.7,       # Controls creativity, lower is more factual
        top_k=40,
        top_p=0.4,
        repeat_penalty=1.18,
        n_batch=8,
    )
    return output

def main():
    """
    Main function to run the full RAG pipeline and generate an answer.
    """
    # 1. Initialize the Language Model
    llm = initialize_llm()

    # 2. Get user query
    # You can make this interactive with input()
    user_query = "What are the common treatments for hypertension?"
    print(f"\nUser Query: {user_query}")

    # 3. Retrieve relevant context from ChromaDB
    context_chunks = retrieve_relevant_chunks(user_query)
    
    # 4. Build the prompt for the LLM
    prompt = build_prompt(user_query, context_chunks)
    
    # 5. Generate the answer
    answer = generate_answer(llm, prompt)

    # 6. Display the final answer
    print("\n--- Generated Answer ---")
    print(answer)
    print("\n--------------------------")


if __name__ == "__main__":
    main()