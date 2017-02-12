import json
from watson_developer_cloud import ToneAnalyzerV3


def process_text(text):
    tone = get_tone(text)
    feelings = parse_json(tone)
    category = get_category(feelings)
    return category


def get_category(feelings):
    category = ""
    for mood in feelings.keys():
        if feelings[mood] > .5:
            # This might change to get the strongest feeling
            category = mood

    return category


def get_tone(text_body):
    tone_analyzer = ToneAnalyzerV3(
        username='66260cef-76f6-4959-96e6-8ddb4fd9238c',
        password='J0kNZv3s0Jzj',
        version='2017-02-11')

    tone_json = tone_analyzer.tone(text=text_body)

    print(json.dumps(tone_json, indent=2))

    # Since the number of requests is limited, I wanted to
    # automatically keep track of them
    with open('request_count.txt', 'r') as file:
        count = int(file.readline())

    with open('request_count.txt', 'w') as file:
        file.writelines(str(count + 1))

    return tone_json


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


if __name__ == '__main__':
    test_text = "I am very happy and I don't feel so well."
    get_tone(test_text)
