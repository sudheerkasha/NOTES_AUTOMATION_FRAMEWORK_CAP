import os
import yaml
from utils.logger import get_logger

logger = get_logger(__name__)

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config",
    "config.yaml",
)

_config_cache = None

def load_config(config_path=None):
    global _config_cache
    if _config_cache is not None:
        return _config_cache
    path = config_path or CONFIG_PATH
    if not os.path.exists(path):
        logger.error(f"Configuration file not found: {path}")
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        _config_cache = yaml.safe_load(f)
        logger.info(f"Configuration loaded from: {path}")
    return _config_cache

def get_config_value(section, key, default=None):
    config = load_config()
    try:
        value = config[section][key]
        return value
    except KeyError:
        logger.warning(f"Config key '{section}.{key}' not found, using default: {default}")
        return default

def get_browser_config():
    return load_config().get("browser", {})

def get_api_config():
    return load_config().get("api", {})

def get_app_config():
    return load_config().get("app", {})

def get_test_user():
    return load_config().get("test_user", {})
