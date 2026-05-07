import time
import allure
import requests

from api.endpoints import Endpoints
from utils.logger import get_logger
from utils.config_reader import get_api_config, get_app_config

logger = get_logger(__name__)

class APIClient:

    def __init__(self, base_url=None):

        app_config = get_app_config()

        self.base_url = base_url or app_config.get(

            "api_base_url",

            "https://practice.expandtesting.com/notes/api"

        )

        self.api_config = get_api_config()

        self.timeout = self.api_config.get("timeout", 30)

        self.token = None

        self.session = requests.Session()

        logger.info(f"API Client initialized: {self.base_url}")

    def build_url(self, endpoint):

        return f"{self.base_url}{endpoint}"

    def get_headers(self):

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        if self.token:

            headers["x-auth-token"] = self.token

        return headers

    def log_response(self, response, method, endpoint):

        elapsed = response.elapsed.total_seconds()

        logger.info(

            f"API {method} {endpoint} -> "

            f"Status: {response.status_code} | Time: {elapsed:.2f}s"

        )

        allure.attach(

            f"Method: {method}\nURL: {response.url}\n"

            f"Status: {response.status_code}\n"

            f"Time: {elapsed:.2f}s\n"

            f"Response: {response.text[:500]}",

            name=f"API Response - {method} {endpoint}",

            attachment_type=allure.attachment_type.TEXT,

        )

    @allure.step("API: Register user - {email}")

    def register_user(self, name, email, password):

        data = {"name": name, "email": email, "password": password}

        response = self.session.post(

            self.build_url(Endpoints.REGISTER),

            data=data,

            timeout=self.timeout,

        )

        self.log_response(response, "POST", Endpoints.REGISTER)

        return response

    @allure.step("API: Login user - {email}")

    def login(self, email, password):

        data = {"email": email, "password": password}

        response = self.session.post(

            self.build_url(Endpoints.LOGIN),

            data=data,

            timeout=self.timeout,

        )

        self.log_response(response, "POST", Endpoints.LOGIN)

        if response.status_code == 200:

            resp_json = response.json()

            self.token = resp_json.get("data", {}).get("token", "")

            if self.token:

                logger.info("Auth token acquired successfully")

            else:

                logger.warning("Login succeeded but no token in response")

        return response

    @allure.step("API: Get user profile")

    def get_profile(self):

        response = self.session.get(

            self.build_url(Endpoints.PROFILE),

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "GET", Endpoints.PROFILE)

        return response

    @allure.step("API: Logout user")

    def logout(self):

        response = self.session.delete(

            self.build_url(Endpoints.LOGOUT),

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "DELETE", Endpoints.LOGOUT)

        if response.status_code == 200:

            self.token = None

        return response

    @allure.step("API: Delete user account")

    def delete_account(self):

        response = self.session.delete(

            self.build_url(Endpoints.DELETE_ACCOUNT),

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "DELETE", Endpoints.DELETE_ACCOUNT)

        return response

    @allure.step("API: Create note - {title}")

    def create_note(self, title, description, category="Home"):

        data = {

            "title": title,

            "description": description,

            "category": category,

        }

        response = self.session.post(

            self.build_url(Endpoints.NOTES),

            data=data,

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "POST", Endpoints.NOTES)

        return response

    @allure.step("API: Get all notes")

    def get_all_notes(self):

        response = self.session.get(

            self.build_url(Endpoints.NOTES),

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "GET", Endpoints.NOTES)

        return response

    @allure.step("API: Get note by ID - {note_id}")

    def get_note_by_id(self, note_id):

        endpoint = Endpoints.note_by_id(note_id)

        response = self.session.get(

            self.build_url(endpoint),

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "GET", endpoint)

        return response

    @allure.step("API: Update note - {note_id}")

    def update_note(self, note_id, title, description,

                    completed=False, category="Home"):

        data = {

            "title": title,

            "description": description,

            "completed": str(completed).lower(),

            "category": category,

        }

        endpoint = Endpoints.note_by_id(note_id)

        response = self.session.put(

            self.build_url(endpoint),

            data=data,

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "PUT", endpoint)

        return response

    @allure.step("API: Delete note - {note_id}")

    def delete_note(self, note_id):

        endpoint = Endpoints.note_by_id(note_id)

        response = self.session.delete(

            self.build_url(endpoint),

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "DELETE", endpoint)

        return response

    @allure.step("API: Toggle note completion - {note_id}")

    def update_note_status(self, note_id, completed):

        endpoint = Endpoints.note_by_id(note_id)

        data = {"completed": str(completed).lower()}

        response = self.session.patch(

            self.build_url(endpoint),

            data=data,

            headers=self.get_headers(),

            timeout=self.timeout,

        )

        self.log_response(response, "PATCH", endpoint)

        return response

    @allure.step("API: Health check")

    def health_check(self):

        response = self.session.get(

            self.build_url(Endpoints.HEALTH_CHECK),

            timeout=self.timeout,

        )

        self.log_response(response, "GET", Endpoints.HEALTH_CHECK)

        return response
