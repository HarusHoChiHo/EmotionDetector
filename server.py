"""Flask application for detecting emotions from text using Watson NLP."""
from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    """Handles POST requests to detect emotion from input text."""
    result = emotion_detector("")

    if result is None:
        result = {
            'anger': None, 
        'disgust': None, 
        'fear': None, 
        'joy': None, 
        'sadness': None, 
        'dominant_emotion': None}

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    text_result1 = "For the given statement, "
    text_result2 = f"the system response is 'anger': {result['anger']}, "
    text_result3 = f"'disgust': {result['disgust']}, "
    text_result4 = f"'fear': {result['fear']}, "
    text_result5 = f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
    text_result6 = f"The dominant emotion is {result['dominant_emotion']}."
    return text_result1+text_result2+text_result3+text_result4+text_result5+text_result6
    