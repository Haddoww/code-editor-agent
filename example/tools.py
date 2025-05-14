
from openai import OpenAI
from config import client



#add error handling

def add_inline_text(original):
    prompt = f"""

You are an expert code documentation specialist. Analyze the provided code and add clear, concise explanatory comments that:

- Describe what each function/method does and why
- Explain complex algorithms or logic
- Clarify the purpose of important variables
- Document assumptions and constraints
- Highlight key design decisions
- Provide context that helps understand the code's purpose

Focus on adding explanations where they provide the most value. Use plain language that would help a developer who is 
unfamiliar with the codebase.

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

Add only test cases without modifying the original functionality.

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


