from config.settings import ADMIN_NAME


def check_admin_role(username: str) -> bool:
    return True if username == ADMIN_NAME else False
