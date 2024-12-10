import google.generativeai as genai

def llm_response(api_key,doc_data):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = doc_data + "read this and give some keywords from it"
    response = model.generate_content(prompt)
    print(response.text)
    
    
def read_and_parse_document(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        print("UTF-8 encoding failed. Trying with ISO-8859-1...")
        try:
            with open(file_path, 'r', encoding='iso-8859-1') as file:
                return file.read()
        except Exception as e:
            print(f"Failed to read file: {e}")
            return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


API_KEY = "your-api-key"
doc_data = read_and_parse_document("sample.pdf")
llm_response(API_KEY,doc_data)
