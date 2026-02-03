import json
from urllib.request import urlopen

URL = "https://api.github.com"

def main():
    with urlopen(URL) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    with open("data/github_api_root.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Saved to data/github_api_root.json")

if __name__ == "__main__":
    main()
