"""Module providing a function to detect emotions within a text."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This function detects emotions within a text'''
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)

    if emotions is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return f"""For the given statement, the system response is 'anger': {emotions['anger']},
          'disgust': {emotions['disgust']},'fear': {emotions['fear']},
          'joy': {emotions['joy']} and'sadness': {emotions['sadness']}.
          The dominant emotion is {emotions['dominant_emotion']}."""



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
