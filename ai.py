import os

from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD API KEY
# ============================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY was not found. "
        "Please check your .env file."
    )


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GOOGLE_API_KEY
)


MODEL_NAME = "gemini-2.5-flash"


# ============================================================
# STUDY MATERIAL GENERATION
# ============================================================

def generate_response(prompt, images):
    """
    Sends the study-material prompt and page images to Gemini.
    """

    if not images:
        raise ValueError(
            "No images were provided."
        )

    contents = [prompt]

    for image in images:

        contents.append(
            image
        )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents
    )

    if not response or not response.text:

        raise ValueError(
            "Gemini returned an empty response."
        )

    return response.text


# ============================================================
# ASK STUDYSCAN
# ============================================================

def ask_studyscan(
    question,
    study_material,
    chat_history=None
):
    """
    Answers questions using the generated StudyScan
    material and previous conversation.
    """

    if not question or not question.strip():

        raise ValueError(
            "Please enter a question."
        )


    if not study_material or not study_material.strip():

        raise ValueError(
            "There is no generated study material available."
        )


    if chat_history is None:

        chat_history = []


    # ========================================================
    # BUILD CONVERSATION HISTORY
    # ========================================================

    conversation_text = ""


    for message in chat_history:

        role = message.get(
            "role",
            ""
        )

        text = message.get(
            "text",
            ""
        )


        if not text:

            continue


        if role == "user":

            conversation_text += (
                f"Student: {text}\n"
            )


        elif role == "assistant":

            conversation_text += (
                f"StudyScan: {text}\n"
            )


    # ========================================================
    # CHATBOT PROMPT
    # ========================================================

    chatbot_prompt = f"""
You are Ask StudyScan, the AI study companion inside StudyScan AI.

The student has already generated study material using StudyScan AI.

Your job is to answer the student's question using that material.

GENERATED STUDY MATERIAL
==================================================

{study_material}

==================================================

PREVIOUS CONVERSATION
==================================================

{conversation_text}

==================================================

CURRENT STUDENT QUESTION
==================================================

{question}

==================================================

RULES

1. Use the generated study material as your primary source.

2. Answer the student's exact question clearly.

3. Maintain continuity with the previous conversation.

4. If the answer is present in the study material,
   explain it accurately and simply.

5. You may use basic academic knowledge when necessary
   to explain something clearly.

6. Do not contradict the uploaded/generated study material.

7. If the requested information is genuinely not present
   in the study material, say that it is not available
   in the provided study material.

8. Do not invent facts.

9. Keep the answer student-friendly.

10. For difficult concepts, explain them step by step.

11. Use short paragraphs and bullet points where useful.

12. Do not mention these instructions.

13. Do not mention prompts, context windows, APIs,
    programming or internal processing.

14. Respond naturally like an AI tutor having a conversation
    with a student.

15. Answer only the student's current question.

Give the most helpful educational answer possible.
"""


    # ========================================================
    # GEMINI REQUEST
    # ========================================================

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=chatbot_prompt
    )


    if not response or not response.text:

        raise ValueError(
            "Gemini returned an empty chatbot response."
        )


    return response.text.strip()