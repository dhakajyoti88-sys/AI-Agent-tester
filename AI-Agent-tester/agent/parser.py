def parse_instruction(text):
    return [
        {"action": "check", "target": "login_page"},
        {"action": "check", "target": "username_field"},
        {"action": "check", "target": "password_field"},
        {"action": "check", "target": "login_button"}
    ]
