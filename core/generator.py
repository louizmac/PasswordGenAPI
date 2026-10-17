import secrets
import string


def generate_password(
    length=20,
    uppercase=True,
    lowercase=True,
    numbers=True,
    symbols=True
):
    character_groups = []

    if uppercase:
        character_groups.append(string.ascii_uppercase)

    if lowercase:
        character_groups.append(string.ascii_lowercase)

    if numbers:
        character_groups.append(string.digits)

    if symbols:
        character_groups.append("!@#$%^&*()-_=+")

    if not character_groups:
        raise ValueError(
            "At least one character type must be enabled"
        )

    if not 8 <= length <= 128:
        raise ValueError(
            "Password length must be between 8 and 128"
        )

    alphabet = "".join(character_groups)

    password = [
        secrets.choice(group)
        for group in character_groups
    ]

    password.extend(
        secrets.choice(alphabet)
        for _ in range(length - len(password))
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
