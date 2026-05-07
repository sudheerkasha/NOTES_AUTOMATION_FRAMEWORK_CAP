import os
import pytest
import allure

from fixtures.driver_fixture import create_driver
from fixtures.api_fixture import create_api_client, setup_test_user, cleanup_test_user
from api.api_client import APIClient
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.logger import get_logger
from utils.helpers import capture_screenshot, generate_random_email
from utils.config_reader import get_test_user

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def driver(request):
    logger.info("=" * 60)
    logger.info(f"STARTING TEST: {request.node.name}")
    logger.info("=" * 60)

    browser = create_driver()

    yield browser

    if hasattr(request.node, "rep_call") and request.node.rep_call and request.node.rep_call.failed:
        logger.error(f"TEST FAILED: {request.node.name}")
        capture_screenshot(browser, request.node.name)

    browser.quit()
    logger.info(f"Driver closed for: {request.node.name}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import pluggy
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(scope="function")
def api_client():
    client = create_api_client()
    yield client

@pytest.fixture(scope="function")
def authenticated_api(api_client):
    user_details = setup_test_user(api_client)
    yield api_client, user_details
    cleanup_test_user(api_client)

@pytest.fixture(scope="function")
def logged_in_ui(driver):
    api = APIClient()
    email = generate_random_email("ui_test")
    user_config = get_test_user()
    password = user_config.get("password", "TestPass@123")
    name = user_config.get("name", "Test Automation User")

    api.register_user(name, email, password)
    api.login(email, password)

    login_page = LoginPage(driver)
    login_page.full_login(email, password)

    notes_page = NotesPage(driver)
    user_info = {"name": name, "email": email, "password": password}

    yield driver, login_page, notes_page, user_info, api

    try:
        cleanup_test_user(api)
    except Exception as e:
        logger.warning(f"Cleanup warning: {e}")

@pytest.fixture(scope="function")
def e2e_setup(driver):
    api = APIClient()
    email = generate_random_email("e2e_test")
    user_config = get_test_user()
    password = user_config.get("password", "TestPass@123")
    name = user_config.get("name", "Test Automation User")

    api.register_user(name, email, password)
    api.login(email, password)

    login_page = LoginPage(driver)
    login_page.full_login(email, password)

    notes_page = NotesPage(driver)

    yield {
        "driver": driver,
        "api": api,
        "login_page": login_page,
        "notes_page": notes_page,
        "user_info": {"name": name, "email": email, "password": password},
    }

    try:
        cleanup_test_user(api)
    except Exception as e:
        logger.warning(f"E2E cleanup warning: {e}")
