import os
import time
import string
import random
from datetime import datetime
import allure
from faker import Faker
from utils.logger import get_logger

logger = get_logger(__name__)
fake = Faker()

SCREENSHOT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "reports",
    "screenshots",
)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def generate_random_email(prefix="testuser"):
    timestamp = int(time.time() * 1000)
    random_suffix = ''.join(random.choices(string.ascii_lowercase, k=5))
    email = f"{prefix}_{timestamp}_{random_suffix}@expandtesting.com"
    logger.debug(f"Generated random email: {email}")
    return email

def generate_random_password(length=12):
    if length < 8:
        length = 8
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*"),
    ]
    password += random.choices(
        string.ascii_letters + string.digits + "!@#$%^&*",
        k=length - 4,
    )
    random.shuffle(password)
    return ''.join(password)

def generate_note_title():
    title = f"AutoTest - {fake.catch_phrase()}"
    logger.debug(f"Generated note title: {title}")
    return title

def generate_note_description():
    description = fake.paragraph(nb_sentences=3)
    logger.debug(f"Generated note description: {description[:50]}...")
    return description

def get_random_category():
    return random.choice(["Home", "Work", "Personal"])

def capture_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    try:
        driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved: {filepath}")
        with open(filepath, "rb") as f:
            allure.attach(
                f.read(),
                name=f"Screenshot - {test_name}",
                attachment_type=allure.attachment_type.PNG,
            )
        return filepath
    except Exception as e:
        logger.error(f"Failed to capture screenshot: {e}")
        return ""

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"Execution time for {func.__name__}: {elapsed:.2f} seconds")
        return result
    return wrapper

def ai_generate_test_data(data_type="note"):
    if data_type == "note":
        return {
            "title": generate_note_title(),
            "description": generate_note_description(),
            "category": get_random_category(),
        }
    elif data_type == "user":
        return {
            "name": fake.name(),
            "email": generate_random_email(),
            "password": generate_random_password(),
        }
    else:
        logger.warning(f"Unknown data type: {data_type}")
        return {}

def ai_analyze_failure(error_message, screenshot_path=""):
    analysis = {
        "error_type": "unknown",
        "possible_cause": "",
        "suggested_action": "",
        "confidence": 0.0,
    }
    error_lower = error_message.lower()
    if "timeout" in error_lower or "timed out" in error_lower:
        analysis["error_type"] = "timeout"
        analysis["possible_cause"] = "Element not found or page load too slow"
        analysis["suggested_action"] = "Increase wait time or check element locator"
        analysis["confidence"] = 0.85
    elif "nosuchelement" in error_lower or "no such element" in error_lower:
        analysis["error_type"] = "element_not_found"
        analysis["possible_cause"] = "Locator changed or element not rendered"
        analysis["suggested_action"] = "Update locator or add explicit wait"
        analysis["confidence"] = 0.90
    elif "stale" in error_lower:
        analysis["error_type"] = "stale_element"
        analysis["possible_cause"] = "DOM was refreshed after element was located"
        analysis["suggested_action"] = "Re-locate element before interaction"
        analysis["confidence"] = 0.88
    elif "401" in error_lower or "unauthorized" in error_lower:
        analysis["error_type"] = "authentication_failure"
        analysis["possible_cause"] = "Token expired or invalid credentials"
        analysis["suggested_action"] = "Re-authenticate and retry"
        analysis["confidence"] = 0.92
    else:
        analysis["possible_cause"] = "Unclassified failure - manual review needed"
        analysis["suggested_action"] = "Check logs and screenshot for details"
        analysis["confidence"] = 0.30
    logger.info(f"AI Failure Analysis: {analysis['error_type']} "
                f"(confidence: {analysis['confidence']:.0%})")
    return analysis
