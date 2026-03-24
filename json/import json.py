import json

def load_data():
    data = []
    for i in range(50):
        entry = {
            "id": i,
            "name": f"user_{i}",
            "scores": [j * i % 100 for j in range(10)]
        }
        data.append(entry)
    return data

def process_data(data):
    results = []
    for item in data:
        avg = sum(item["scores"]) / len(item["scores"])
        results.append({
            "id": item["id"],
            "name": item["name"],
            "average": avg
        })
    return results

def save_data(results):
    with open("output.json", "w") as f:
        json.dump(results, f)

data = load_data()
results = process_data(data)
save_data(results)

print(len(results))