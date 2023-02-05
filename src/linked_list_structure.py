# Linked List can be thought of as such a structure:
head = {
    "value": 10,
    "next": {
        "value": 20,
        "next": {
            "value": 30,
            "next": {
                "value": 40,
                "next": None
            }
        }
    }
}

print(head["next"]["next"]["value"])
