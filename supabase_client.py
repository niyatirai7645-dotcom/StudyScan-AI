import os

from dotenv import load_dotenv
from supabase import create_client, Client


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# ============================================================
# VALIDATION
# ============================================================

if not SUPABASE_URL:

    raise ValueError(
        "SUPABASE_URL was not found. "
        "Please check your .env file."
    )


if not SUPABASE_KEY:

    raise ValueError(
        "SUPABASE_KEY was not found. "
        "Please check your .env file."
    )


# ============================================================
# SUPABASE CLIENT
# ============================================================

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)