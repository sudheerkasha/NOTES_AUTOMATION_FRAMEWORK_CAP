class Endpoints:

    HEALTH_CHECK = "/health-check"

    REGISTER = "/users/register"

    LOGIN = "/users/login"

    PROFILE = "/users/profile"

    FORGOT_PASSWORD = "/users/forgot-password"

    CHANGE_PASSWORD = "/users/change-password"

    LOGOUT = "/users/logout"

    DELETE_ACCOUNT = "/users/delete-account"

    NOTES = "/notes"

    NOTE_BY_ID = "/notes/{note_id}"

    @staticmethod

    def note_by_id(note_id):

        return f"/notes/{note_id}"
