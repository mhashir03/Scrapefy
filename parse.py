from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# prompt template for instructing the LLM on how to parse the DOM content
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# initialize the LLM using Ollama
model = OllamaLLM(model="llama3.1")

# function to parse the DOM content using the LLM
def parse_with_ollama(dom_chunks, parse_description):
    # generate a parsing prompt based on the template
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model 
   
    parsed_results = []
    
    # iterate through the DOM chunks and parse each one
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}") # log the parsing progress
        parsed_results.append(response)
    
    # combine the parsed results from all chunks and return as a single string    
    return "\n".join(parsed_results)
        