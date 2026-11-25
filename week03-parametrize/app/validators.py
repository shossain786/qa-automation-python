"""A simple email check. Known bug: "sara@example" (no dot) is accepted."""


def is_valid_email(email):
    if email.count("@") != 1 or " " in email:
        return False
    name, domain = email.split("@")
    return bool(name) and bool(domain)
