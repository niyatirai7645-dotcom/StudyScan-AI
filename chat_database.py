from supabase_client import supabase


# ============================================================
# SAVE CHAT
# ============================================================

def save_chat_to_database(
    user_id,
    title,
    feature,
    study_level,
    language,
    file_names,
    content
):

    if not user_id:
        return None

    if not content:
        return None

    try:

        response = supabase.table(
            "chats"
        ).insert(
            {
                "user_id": str(user_id),
                "title": title,
                "feature": feature,
                "study_level": study_level,
                "language": language,
                "file_names": file_names,
                "content": content
            }
        ).execute()

        if response.data:
            return response.data[0]

        return None

    except Exception as e:

        print(
            "Supabase chat save error:",
            str(e)
        )

        return None


# ============================================================
# LOAD USER CHATS
# ============================================================

def load_user_chats(user_id):

    if not user_id:
        return []

    try:

        response = (
            supabase
            .table("chats")
            .select("*")
            .eq("user_id", str(user_id))
            .order(
                "created_at",
                desc=True
            )
            .execute()
        )

        return response.data or []

    except Exception as e:

        print(
            "Supabase chat load error:",
            str(e)
        )

        return []


# ============================================================
# DELETE ONE CHAT
# ============================================================

def delete_chat(
    chat_id,
    user_id
):

    if not chat_id or not user_id:
        return False

    try:

        (
            supabase
            .table("chats")
            .delete()
            .eq("id", str(chat_id))
            .eq("user_id", str(user_id))
            .execute()
        )

        return True

    except Exception as e:

        print(
            "Supabase chat delete error:",
            str(e)
        )

        return False


# ============================================================
# DELETE ALL USER HISTORY
# ============================================================

def delete_all_chats(user_id):

    if not user_id:
        return False

    try:

        (
            supabase
            .table("chats")
            .delete()
            .eq("user_id", str(user_id))
            .execute()
        )

        return True

    except Exception as e:

        print(
            "Supabase history delete error:",
            str(e)
        )

        return False