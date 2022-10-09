if __name__ == "__main__":
    phones = {
        "Bob Marley": "11-22-33",
        "Britney Spears": "44-55-66",
        "Justin Bieber": "12-21-12",
    }
    phone_inv = {
        value: key
        for key, value in phones.items()
        if key != "Justin Bieber"
    }
    print(phone_inv)