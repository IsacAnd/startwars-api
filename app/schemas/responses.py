def normalize_person(person: dict):
    return {
        "name": person["name"],
        "height": int(person["height"]) if person["height"].isdigit() else None,
        "mass": int(person["mass"]) if person["mass"].isdigit() else None,
        "gender": person["gender"],
        "films": person["films"],
        "url": person["url"]
    }