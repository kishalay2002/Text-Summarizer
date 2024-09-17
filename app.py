# app.py
from flask import Flask, request, jsonify,render_template
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="KishalayGhoshKIIT/bbc_news_summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get the text data from the frontend
        data = request.json['input_content']

        # Call the summarizer function to generate the summary
        summary = summarizer(data)[0]
        #print(summary)
        # Return the summary as JSON
        return jsonify({'summary': summary["summary_text"]})

    except Exception as e:
        # Handle exceptions as needed
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)
    #app.run(debug=True)
