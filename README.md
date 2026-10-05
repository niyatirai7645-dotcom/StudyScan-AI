# StudyScan AI

A study helper that takes your actual notes (photos, handwritten pages, PDFs) and turns them into clean notes, summaries, flashcards and practice questions.

I built it for the **Lenovo LEAP Generative AI & Agentic Systems Engineering Internship and Hackathon 2026**. It's still a work in progress, so some parts are rough.

---

## Why I made this

Most of my own studying doesn't start from clean, typed text. It's a photo of the board I took at the end of class, a page from a textbook, a friend's handwritten notes, or a PDF the teacher shared. To get an AI to help with any of that, I had to:

1. Take photos of the notes
2. Retype or organize them
3. Paste them into a chatbot and ask for a summary
4. Ask again separately for flashcards
5. Ask again for practice questions
6. Repeat for every chapter

That's a lot of effort before the actual studying even begins. StudyScan AI is my attempt to cut those steps down to one: upload your material and get something you can revise from.

---

## What it does

- **Takes real study material.** JPG, JPEG, PNG and PDF files all work, so both photos and digital documents are fine.
- **Cleans up your notes.** It reads the content and reorganizes it into something tidier and easier to follow.
- **Writes summaries.** Useful when you have a long chapter and only a little time before an exam.
- **Makes flashcards** from your own material, so you're revising what you actually need to learn.
- **Generates practice questions** from the same material.
- **Handles PDFs page by page**, so you don't have to upload every page as a separate image.

Under the hood, the workflow is built with LangGraph. Reading the file, understanding it and generating each type of output run as separate stages instead of one giant prompt, which makes it easier to extend later.

---

## How it fits together

```text
Student
   │
   ▼
Streamlit UI (upload)
   │
   ▼
File processing (image / PDF)
   │
   ▼
LangGraph workflow
   │
   ▼
Gemini 2.5 Flash (multimodal)
   │
   ├── Clean notes
   ├── Summary
   └── Flashcards / questions
```

## Tech stack

| Tool | What it's used for |
| --- | --- |
| Python | Main application logic |
| Streamlit | The web interface |
| Google Gemini 2.5 Flash | Reading images and generating content |
| LangGraph | Orchestrating the workflow |
| Supabase | Authentication and data storage |
| PyMuPDF | Reading PDFs |
| python-dotenv | Loading environment variables |

## Project structure

```text
StudyScanAI/
├── app.py                # Main Streamlit app
├── ai.py                 # Gemini integration
├── prompts.py            # Prompts used for each task
├── pdf_utils.py          # PDF handling
│
├── auth.py               # Login / authentication
├── chat_database.py      # Chat-related database code
├── chat_db.py            # More chat database code
├── supabase_client.py    # Supabase setup
│
├── requirements.txt
├── .env.example
├── .gitignore
├── .streamlit/config.toml
└── README.md
```

---

## Running it locally

**1. Clone the repo**

```bash
git clone https://github.com/niyatirai7645-dotcom/StudyScan-AI.git
cd StudyScan-AI
```

**2. Create and activate a virtual environment**

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install the dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a `.env` file in the project root (`.env.example` shows the format):

```text
GOOGLE_API_KEY=your_google_api_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here
```

> Please don't push your real `.env` file to GitHub. It's already in `.gitignore`, but it's worth double-checking.

**5. Start the app**

```bash
streamlit run app.py
```

Streamlit will print a local URL in the terminal. Open it in your browser and you're good to go.

---

## A typical session

1. Open the app
2. Upload a photo of your notes or a PDF
3. Wait a moment while it's processed
4. Get cleaned-up notes, a summary, flashcards and questions
5. Use them to revise

---

## Why this approach

A lot of AI study tools start with a blank chat box and "ask me anything." I wanted to start from the other end: *here's what I'm studying, now help me with it.* Students shouldn't have to turn everything into perfectly typed text before an AI can be useful.

This also ties into **UN Sustainable Development Goal 4 (Quality Education)**. When it takes less work to turn messy material into something usable, more people can study efficiently, whatever format their notes happen to be in.

---

## What I'd like to add next

- Better OCR for student material, especially messy handwriting
- Stronger understanding of diagrams and tables
- More languages
- Chat that remembers the context of your notes
- Organizing notes by chapter
- Revision plans and quizzes that adapt to how you're doing
- Answers that point back to the source page
- Mind maps
- Saved study history for each user
- More specialized agents for different study tasks

---

## About the hackathon

Built for the **Lenovo LEAP Generative AI & Agentic Systems Engineering Internship, 2026**, under the theme **AI in Education & Skilling**. The aim was to see how multimodal AI and agentic workflows could make studying a bit less painful.

## Author

**Niyati Rai**
B.Tech, Information Technology
AISSMS Institute of Information Technology, Pune

I'm interested in AI, generative AI, agentic systems, software development and ed-tech.

## Status

Still under active development, so things may change as I keep working on it. If you try it out and have feedback or ideas, I'd love to hear them. A ⭐ on the repo is always appreciated.
