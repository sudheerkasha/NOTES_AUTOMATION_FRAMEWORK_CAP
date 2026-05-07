import pytest
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from utils.logger import get_logger
from utils.helpers import generate_note_title, generate_note_description

logger = get_logger(__name__)


@allure.epic("Notes Application")
@allure.feature("End-to-End Hybrid Tests")
class TestE2E:

    # =========================================================
    # COMMON HELPERS
    # =========================================================

    def wait_for_page(self, driver, timeout=20):

        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def safe_note_check(self, notes_page, title):

        try:
            return notes_page.is_note_displayed(title)

        except TimeoutException:
            return False

        except Exception:
            return False

    # =========================================================
    # TC-27
    # UI CREATE -> API VERIFY
    # =========================================================

    @allure.story("UI to API Consistency")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    @pytest.mark.smoke
    def test_ui_create_api_verify(self, e2e_setup):

        ctx = e2e_setup

        notes_page = ctx["notes_page"]
        api = ctx["api"]
        driver = ctx["driver"]

        title = generate_note_title()
        description = generate_note_description()
        category = "Work"

        # CREATE NOTE IN UI
        with allure.step("Create note via UI"):

            notes_page.create_note(
                title,
                description,
                category
            )

            self.wait_for_page(driver)

            assert self.safe_note_check(
                notes_page,
                title
            ), f"Note '{title}' not displayed"

        # VERIFY IN API
        with allure.step("Verify note in API"):

            api_response = api.get_all_notes()

            assert api_response.status_code == 200

            notes = api_response.json()["data"]

            api_note = next(
                (
                    n for n in notes
                    if n["title"] == title
                ),
                None
            )

            assert api_note is not None, \
                f"Note '{title}' not found in API"

            assert api_note["description"] == description

            assert api_note["category"] == category

        logger.info("TC-27 PASSED")

    # =========================================================
    # TC-28
    # API DELETE -> UI VERIFY
    # =========================================================

    @allure.story("API to UI Sync")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    @pytest.mark.smoke
    def test_api_delete_ui_verify(self, e2e_setup):

        ctx = e2e_setup

        notes_page = ctx["notes_page"]
        api = ctx["api"]
        driver = ctx["driver"]

        title = generate_note_title()
        description = generate_note_description()

        # CREATE NOTE VIA API
        with allure.step("Create note via API"):

            create_resp = api.create_note(
                title,
                description,
                "Home"
            )

            assert create_resp.status_code == 200

            note_id = create_resp.json()["data"]["id"]

        # LOAD PAGE SAFELY
        with allure.step("Verify note appears in UI"):

            driver.get(driver.current_url)

            self.wait_for_page(driver)

            assert self.safe_note_check(
                notes_page,
                title
            ), f"Note '{title}' should appear"

        # DELETE NOTE VIA API
        with allure.step("Delete note via API"):

            del_resp = api.delete_note(note_id)

            assert del_resp.status_code == 200

        # RELOAD PAGE SAFELY
        with allure.step("Verify note removed from UI"):

            driver.get(driver.current_url)

            self.wait_for_page(driver)

            assert not self.safe_note_check(
                notes_page,
                title
            ), f"Deleted note '{title}' still visible"

        logger.info("TC-28 PASSED")

    # =========================================================
    # TC-29
    # FULL CRUD
    # =========================================================

    @allure.story("Full CRUD Cycle")
    @pytest.mark.e2e
    @pytest.mark.regression
    def test_full_crud_hybrid(self, e2e_setup):

        ctx = e2e_setup

        notes_page = ctx["notes_page"]
        api = ctx["api"]
        driver = ctx["driver"]

        title = generate_note_title()
        description = generate_note_description()

        # CREATE
        with allure.step("Create note via UI"):

            notes_page.create_note(
                title,
                description,
                "Personal"
            )

            self.wait_for_page(driver)

            assert self.safe_note_check(
                notes_page,
                title
            )

        # READ
        with allure.step("Read note via API"):

            resp = api.get_all_notes()

            assert resp.status_code == 200

            notes = resp.json()["data"]

            note = next(
                (
                    n for n in notes
                    if n["title"] == title
                ),
                None
            )

            assert note is not None

            note_id = note["id"]

        # UPDATE
        updated_title = f"Updated - {title}"

        with allure.step("Update note via API"):

            update_resp = api.update_note(
                note_id,
                updated_title,
                description,
                False,
                "Work"
            )

            assert update_resp.status_code == 200

        # VERIFY UPDATE
        with allure.step("Verify update in UI"):

            driver.get(driver.current_url)

            self.wait_for_page(driver)

            assert self.safe_note_check(
                notes_page,
                updated_title
            ), "Updated title not found"

        # DELETE
        with allure.step("Delete note via API"):

            del_resp = api.delete_note(note_id)

            assert del_resp.status_code == 200

        # VERIFY DELETE
        with allure.step("Verify deletion in UI"):

            driver.get(driver.current_url)

            self.wait_for_page(driver)

            assert not self.safe_note_check(
                notes_page,
                updated_title
            ), "Deleted note still visible"

        logger.info("TC-29 PASSED")

    # =========================================================
    # TC-30
    # PERFORMANCE
    # =========================================================

    @allure.story("UI Performance")
    @pytest.mark.e2e
    @pytest.mark.performance
    def test_ui_page_load_performance(self, e2e_setup):

        ctx = e2e_setup

        notes_page = ctx["notes_page"]
        driver = ctx["driver"]

        driver.get(driver.current_url)

        self.wait_for_page(driver)

        load_time = notes_page.get_page_load_time()

        assert load_time < 10.0, \
            f"Page load too high: {load_time:.2f}s"

        logger.info(
            f"TC-30 PASSED - Load time {load_time:.2f}s"
        )
