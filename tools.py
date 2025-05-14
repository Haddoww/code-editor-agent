
from openai import OpenAI
from config import client
from google_auth import get_docs_service




#add error handling

def add_inline_text(original):
    prompt = f"""

You are an expert software engineer. Analyze the provided code and add clear, concise explanatory inline comments that

Focus on adding explanations where they provide the most value. Use plain language that would help a developer who is 
unfamiliar with the codebase. They do not have to be on every line, keep the code looking clean.

Code: {original}
"""
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def add_inline_testcases(original):
    prompt = f"""
You are an expert test engineer specialized in adding meaningful test cases to code. Analyze the provided code and add inline test cases that verify the functionality works correctly.

Focus on:
- Testing edge cases and common failure points
- Creating clear assertions with descriptive messages
- Adding tests that demonstrate expected behavior
- Making tests that are easy to understand and maintain
- Placing tests in appropriate locations within the code

Add only five test cases without modifying the original functionality.

Code: {original}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def add_todos(original):
    prompt = f"""

    You are an expert code reviewer with a keen eye for code improvements. Analyze the provided code and add inline TODO comments that highlight:

- Potential bugs or edge cases not handled
- Optimization opportunities
- Areas that need better error handling
- Code that should be refactored for clarity or maintainability
- Documentation needs
- Security considerations

Keep TODO comments specific, actionable, and constructive. Format them consistently as: "TODO: [brief description of the issue and suggested improvement]"

Code: {original}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


    

def refactor_variables(original):
    prompt = f"""
You are an expert at refactoring code. Improve the variable naming scheme of the code below.
Use best practices for consistent naming and simplify where needed.

Code: {original}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content



def add_print_statements(original):
    prompt = f"""
You are an expert at debugging code. Add print statements at critical sections of the code where understanding
the output is critical.

Code: {original}
"""
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def add_error_handling(original):
    prompt = f"""
You are a senior software engineer reviewing code. Add robust error handling for the code given, so that it is production ready.
Only add the necessary error handling and only return the new code.
Code: {original}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
    

def pause_and_reassess(current_code, original_code, goal, remaining_steps):
    prompt = f"""
You are an expert software agent helping with code improvement.

User's original goal:
"{goal}"

Current code state:
{current_code}

Original code:
{original_code}

Remaining steps: {remaining_steps}

Your available tools are: {list(TOOLS.keys())}.

Have we satisfied the user's goal already? If yes, return "STOP". If not, return the list of remaining steps (possibly modified).
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content.strip()
    if "STOP" in result.upper():
        return "STOP"
    return eval(result)


def create_new_doc(title):
    service = get_docs_service()
    body = {'title': title}
    doc = service.documents().create(body=body).execute()
    return doc.get('documentId')


def add_google_documentation(original):
    prompt = f"""""
    You are an expert code documentation specialist. Analyze the provided code and add clear, concise explanatory comments that:

- Describe what each function/method does and why
- Explain complex algorithms or logic
- Clarify the purpose of important variables
- Document assumptions and constraints
- Highlight key design decisions
- Provide context that helps understand the code's purpose

Use plain language that would help a developer who is 
unfamiliar with the codebase. You do not have to return the code itself, just the explanation

Code: {original}
"""
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content



def append_to_doc(doc_id, text):
    service = get_docs_service()
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        }
    ]
    service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()


def generate_documentation_tool(code, doc_id=None):

    if not doc_id:
        doc_id = create_new_doc("Code Assistant Documentation2")

        summary = add_google_documentation(code)

    append_to_doc(doc_id, summary)

    return f"Documentation generated at: https://docs.google.com/document/d/{doc_id}/edit"

TOOLS =  {
    "refactor" : refactor_variables,
    "test" : add_inline_testcases,
    "todo" : add_todos,
    "explain" : add_inline_text,
    "debug" : add_print_statements,
    "pause" : pause_and_reassess,
    "documentation" : generate_documentation_tool,
    "error" : add_error_handling,
}

