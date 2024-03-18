import os
from pathlib import Path

from dotenv import load_dotenv
from instructor import patch
from openai import OpenAI

from dreamai_gen.llms import ModelName, oai_response
from dreamai_gen.message import assistant_message, system_message, user_message
from dreamai_gen.prompting.prompt_fns import process_prompt

load_dotenv()

PROMPTS_DIR = Path("prompts")
QUESTIONS_DIR = Path("questions")
FUNCTIONS_DIR = Path("functions")
MODEL = ModelName.GPT_4
TEMPERATURE = 0.3

ASK_GPT = patch(OpenAI()).chat.completions.create

os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(QUESTIONS_DIR, exist_ok=True)
os.makedirs(FUNCTIONS_DIR, exist_ok=True)


def question_to_functions(
    question: str | Path, messages: list[dict[str, str]] | None = None
) -> tuple[str, str]:
    question = QUESTIONS_DIR / question
    assert question.exists(), f"{question} does not exist"
    question_name = Path(question).stem
    question = process_prompt(question)
    creator_prompt = process_prompt(PROMPTS_DIR / "creator.txt")
    validator_prompt = process_prompt(PROMPTS_DIR / "validator.txt")
    messages = messages or [system_message(creator_prompt)]
    messages += [
        user_message(question),
        user_message(
            "Remember to not change the question. Just copy and paste it. But the parameters should be generated randomly every time the function is called."
        ),
        assistant_message("```python"),
    ]
    creator = oai_response(
        ASK_GPT(messages=messages, model=MODEL, temperature=TEMPERATURE)
    )
    messages += [
        assistant_message(creator),
        user_message(validator_prompt),
        user_message(
            f"Remember to import the function you just created from {question_name}_creator.py"
        ),
        assistant_message("```python"),
    ]
    validator = oai_response(
        ASK_GPT(messages=messages, model=MODEL, temperature=TEMPERATURE)
    )
    messages.append(assistant_message(validator))
    try:
        creator = creator.split("```python")[1].split("```")[0]
    except Exception:
        pass
    try:
        validator = validator.split("```python")[1].split("```")[0]
    except Exception:
        pass
    Path(FUNCTIONS_DIR / f"{question_name}_creator.py").write_text(creator)
    Path(FUNCTIONS_DIR / f"{question_name}_validator.py").write_text(validator)
    return messages
