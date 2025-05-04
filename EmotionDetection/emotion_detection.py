import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()["emotionPredictions"][0]["emotion"]

    name = ""
    highest_score = 0
    for i in result.keys():
        if result[i] > highest_score:
            highest_score = result[i]
            name = i
    
    result["dominant_emotion"] = name

    return result
    
    
