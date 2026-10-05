from supabase_client import supabase


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
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )

        return response.data or []

    except Exception as e:

        print("Could not load chats:", e)

        return []


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

    try:

        chat_data = {

            "user_id":
                user_id,

            "title":
                title,

            "feature":
                feature,

            "study_level":
                study_level,

            "language":
                language,

            "file_names":
                file_names,

            "content":
                content
        }


        response = (
            supabase
            .table("chats")
            .insert(chat_data)
            .execute()
        )


        if response.data:

            return response.data[0]


        return None


    except Exception as e:

        print(
            "Could not save chat to supabase:"
        )
        print(
            repr(e)
        )

        return None


# ============================================================
# DELETE ONE CHAT
# ============================================================

def delete_chat_from_database(
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
            .eq("id", chat_id)
            .eq("user_id", user_id)
            .execute()
        )

        return True

    except Exception as e:

        print("Could not delete chat:", e)

        return False


# ============================================================
# DELETE ALL USER CHATS
# ============================================================

def delete_all_user_chats(user_id):

    if not user_id:

        return False

    try:

        (
            supabase
            .table("chats")
            .delete()
            .eq("user_id", user_id)
            .execute()
        )

        return True

    except Exception as e:

        print("Could not delete chat history:", e)

        return False