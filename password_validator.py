"""Lab 04: Password validator used for the pytest graded tasks.

Rules:
* length 8 to 64 characters
* at least one uppercase, one lowercase, one digit, one special character
* no spaces
"""

SPECIALS = "!@#$%^&*()-_=+[]{};:,.<>?/"
MIN_LENGTH = 8
MAX_LENGTH = 64


def validate_password(password):
    """Return a list of error messages. Empty list means the password is valid."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    errors = []
    if len(password) < MIN_LENGTH:
        errors.append("too short")
    if len(password) > MAX_LENGTH:
        errors.append("too long")
    if not any(ch.isupper() for ch in password):
        errors.append("missing uppercase")
    if not any(ch.islower() for ch in password):
        errors.append("missing lowercase")
    if not any(ch.isdigit() for ch in password):
        errors.append("missing digit")
    if not any(ch in SPECIALS for ch in password):
        errors.append("missing special character")
    if " " in password:
        errors.append("contains space")
    return errors


def is_valid_password(password):
    return not validate_password(password)


if __name__ == "__main__":
    for pwd in ("Abcdef1!", "weak", "NoDigits!!"):
        print(pwd, "->", validate_password(pwd) or "valid")
