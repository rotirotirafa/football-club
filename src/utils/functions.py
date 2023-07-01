import bcrypt


def to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


def to_snake_case(string: str) -> str:
    return ''.join(['_' + i.lower() if i.isupper() else i for i in string]).lstrip('_')


def hash_pw(password: str) -> bytes:
    pw = password.encode('utf-8')
    salt = bcrypt.gensalt(10)
    pw_hashed = bcrypt.hashpw(pw, salt)
    return pw_hashed


def verify_password_hash(password: str) -> bool:
    pw = password.encode('utf-8')
    verified = bcrypt.checkpw(pw, hash_pw(password))
    if verified:
        return True
    return False


def compare_password_hash(input_password: str, user_password_hashed: bytes) -> bool:
    return bcrypt.checkpw(input_password.encode('utf-8'), user_password_hashed)
