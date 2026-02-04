from app.clients.swapi_client import get_people

def gender_distribution():
    data = get_people()
    results = data["results"]

    stats = {}
    for p in results:
        gender = p.get("gender", "unknown")
        stats[gender] = stats.get(gender, 0) + 1

    total = sum(stats.values())

    return {
        "total_characters": total,
        "distribution": stats
    }


def average_height():
    data = get_people()
    results = data["results"]

    heights = []
    for p in results:
        try:
            heights.append(int(p["height"]))
        except:
            pass

    avg = sum(heights) / len(heights)

    return {
        "average_height": round(avg, 2),
        "sample_size": len(heights)
    }
