from openai import OpenAI
import random
from config import client
from tools import TOOLS




def generate_user_goal():
    response = random.choice([
        "Can you help me understand what this section is talking about",
        "Simplify my code and make it more readable",
        "How can I expand this code to be more robust", 
        "What does this code actually do",
    ])

    return response
def generate_plan(user_goal, initial_code):
    prompt = f"""
You are an expert coding assistant that improves code using a set of tools. Your goal is to achieve the user’s intent **efficiently**, using the **least number of necessary steps**.
You have access to the following tools:
- add_inline_text: adds helpful comments and explanations
- add_inline_testcases: inserts useful test cases
- add_todos: highlights improvements or bugs using TODO comments
- refactor_variables: renames variables to improve readability
- add_print_statements: inserts print statements for debugging
- pause_and_reassess: use this if the goal may be complete or if you’re unsure whether more steps are needed
- generate_documentation_tool: Creates a google document with a detailed summary of the code given
- add_error_handling: this adds robust error handling to the code

use the tool names here : {list(TOOLS.keys())}

Before generating a plan, analyze the goal and the code. If a step might already fulfill the goal, use `pause_and_reassess` to check your progress.

Given the user's goal: "{user_goal}", and the initial code {initial_code},  generate a list (in Python syntax) of tool names to apply in logical order.
Consider 
Respond ONLY with the list of tool names.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    plan_text = response.choices[0].message.content
    try:
        plan = eval(plan_text)
        return [step for step in plan if step in TOOLS], plan_text
    except Exception:
        return []


def enhance_code(code, user_goal):
    plan = generate_plan(user_goal)
    memory = {"code": code, "log": []}

    for step in plan:
        tool = TOOLS[step]
        result = tool(memory["code"])
        memory["log"].append((step, result))
        memory["code"] = result

    return memory["code"], memory["log"], plan


def generate_plan_and_prepare(code, goal):
    plan, og_text = generate_plan(goal, code)
    return plan, code, og_text

def run_tool_on_code(tool_name, code):
    tool = TOOLS[tool_name]
    return tool(code)