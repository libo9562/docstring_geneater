import re
from textwrap import dedent

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain


@chain
def extract_func_header(text: str) -> str:
    pattern = r"```python(.*?)```"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()
    return ""


def get_docstring_chain(llm):
    msg = dedent("""\
    Generate a detailed google style docstring and provide type hints for the parameters and return type \
    of the following Python function:

    {function_signature}

    Do not change the default value, do not add imports. Please respond with only the updated function \
    signature with docstring No other text or code needed
    """)
    prompt = ChatPromptTemplate.from_messages(("human", msg))
    chain = prompt | llm | StrOutputParser() | extract_func_header
    return chain
