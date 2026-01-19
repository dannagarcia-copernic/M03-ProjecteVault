def check_password(pwd):
    # Requisits NIST
    if len(pwd) < 8:
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    if not any(char.isupper() for char in pwd):
        return False
    if "admin" in pwd.lower():
        return False

    return True
