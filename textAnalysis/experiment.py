import json


def parse_json(tone_json):

    tones = tone_json["document_tone"]["tone_categories"][0]["tones"]

    feelings = {
        "anger": float(tones[0]["score"]),
        "disgust": float(tones[1]["score"]),
        "fear": float(tones[2]["score"]),
        "joy": float(tones[3]["score"]),
        "sadness": float(tones[4]["score"])
    }

    print(feelings)

    return feelings


if __name__ == "__main__":
    json_text = {}

    with open('example_output.json') as file:
        json_text = json.load(file)

    parse_json(json_text)
