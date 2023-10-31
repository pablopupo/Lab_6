def decode(password):
    decoded = []
    for c in password:
        decoded_pass = (int(c) - 3) % 10
        decoded.append(str(decoded_pass))
    return "".join(decoded)