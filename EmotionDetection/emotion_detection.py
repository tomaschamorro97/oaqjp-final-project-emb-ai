import json
import requests

def emotion_detector(text_to_analyze):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = my_obj, headers=header)

    if response.status_code == 200:

        formatted_response = json.loads(response.text)

        emotion_data = formatted_response["emotionPredictions"][0]["emotion"]

        anger_score = emotion_data["anger"]
        disgust_score = emotion_data["disgust"]
        fear_score = emotion_data["fear"]
        joy_score = emotion_data["joy"]
        sadness_score = emotion_data["sadness"]

        highest_emotion = max(emotion_data, key=emotion_data.get)

        response_dic = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': highest_emotion
        }
        return response_dic
    elif response.status_code == 400:
        return None 

    
