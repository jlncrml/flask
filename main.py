from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "running"})

@app.route('/transcript')
def transcript():
    video_identifier = request.args.get("video_id")
    language = request.args.get("language", default="sv")
    if not video_identifier:
        return jsonify({"error": "missing video_id"}), 400
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_identifier, languages=[language])
        return jsonify(transcript_data)
    except Exception as exception:
        return jsonify({"error": str(exception)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
