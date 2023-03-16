import random
import string

import allure


def generate_random_email(
        domain=None,
        prefix=None
):
    email_length = 10
    if not domain:
        domain = "gmail.com"
    if not prefix:
        prefix = "lsqateam_"

    random_string = "".join(
        random.choices(
            string.ascii_lowercase,
            k=email_length
        )
    )
    random_email = f"{prefix}{random_string}@{domain}"

    with allure.step(f"Generate random email: {random_email}"):
        return random_email


def generate_random_password():
    password_length = 20
    random_password = "".join(
        random.choices(
            string.ascii_letters,
            k=password_length
        )
    )
    with allure.step(f"Generate random password: {random_password}"):
        return random_password


def generate_random_string(
        length=10,
        prefix=None,
        suffix=None
):
    random_string = "".join(
        random.choices(
            string.ascii_lowercase,
            k=length
        )
    )
    if prefix:
        random_string = prefix + random
    if suffix:
        random_string = random_string + suffix

    with allure.step(f"Generate random string: {random_string}"):
        return random_string
