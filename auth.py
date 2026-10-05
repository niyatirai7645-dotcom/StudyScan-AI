import streamlit as st

from supabase_client import supabase


# ============================================================
# SIGN UP
# ============================================================

def sign_up(email, password):

    if not email or not email.strip():
        return False, "Please enter your email address."

    if not password:
        return False, "Please enter a password."

    try:

        response = supabase.auth.sign_up(
            {
                "email": email.strip(),
                "password": password
            }
        )

        if response.user is not None:

            return True, (
                "Account created successfully. "
                "Please check your email to verify your account."
            )

        return False, "Could not create the account."

    except Exception as e:

        return False, str(e)


# ============================================================
# LOGIN
# ============================================================

def login(email, password):

    if not email or not email.strip():

        return False, "Please enter your email address."


    if not password:

        return False, "Please enter your password."


    try:

        response = supabase.auth.sign_in_with_password(
            {
                "email": email.strip(),
                "password": password
            }
        )


        if response.user is not None:

            st.session_state.authenticated = True

            st.session_state.user = response.user

            st.session_state.chats_loaded = False

            return True, "Login successful."


        return False, "Invalid email or password."


    except Exception as e:

        return False, str(e)




# ============================================================
# FORGOT PASSWORD
# ============================================================

def forgot_password(email):

    if not email or not email.strip():

        return False, "Please enter your email address."

    try:

        supabase.auth.reset_password_for_email(
            email.strip(),
            options={
                "redirect_to": "http://localhost:8501"
            }
        )

        return True, (
            "Password reset instructions have been "
            "sent to your email."
        )

    except Exception as e:

        return False, str(e)


# ============================================================
# VERIFY PASSWORD RECOVERY TOKEN
# ============================================================

def verify_password_recovery(token_hash):

    if not token_hash:

        return False, None, "Password recovery token is missing."

    try:

        response = supabase.auth.verify_otp(
            {
                "token_hash": token_hash,
                "type": "recovery"
            }
        )

        if response.user is not None:

            return (
                True,
                response.user,
                "Password recovery verified."
            )

        return (
            False,
            None,
            "Could not verify the password recovery link."
        )

    except Exception as e:

        return False, None, str(e)

# ============================================================
# UPDATE PASSWORD AFTER RECOVERY
# ============================================================

def update_password(new_password):

    if not new_password:
        return False, "Please enter a new password."

    try:

        response = supabase.auth.update_user(
            {
                "password": new_password
            }
        )

        if response.user is not None:

            return True, "Password updated successfully."

        return False, "Could not update the password."

    except Exception as e:

        return False, str(e)

# ============================================================
# LOGOUT
# ============================================================

def logout():

    try:

        supabase.auth.sign_out()

    except Exception:

        pass


    st.session_state.authenticated = False

    st.session_state.user = None

    st.session_state.chats_loaded = False

    st.session_state.generated_output = None

    st.session_state.chat_history = []

    st.session_state.active_chat_id = None

    st.session_state.current_feature = None

    st.session_state.current_study_level = None

    st.session_state.current_language = None

    st.session_state.current_file_names = []

    st.session_state.ask_history = []

    st.session_state.ask_studyscan_open = False

    st.session_state.current_chat_saved = False

    st.session_state.current_mode = "Study Material"

    st.session_state.document_type = None

    st.session_state.document_level = None

# ============================================================
# CURRENT USER
# ============================================================

def get_current_user():

    try:

        response = supabase.auth.get_user()

        if response and response.user:

            return response.user

    except Exception:

        pass

    return None