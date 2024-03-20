from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 유튜브 영상 ID를 저장할 변수
current_video_id = None

# 채팅 기록을 저장할 변수
chat_history = []

@app.route('/')
def index():
    return render_template('index.html', current_video_id=current_video_id, chat_history=chat_history)

@app.route('/play', methods=['POST'])
def play_video():
    global current_video_id
    video_id = request.form['video_id']
    current_video_id = video_id
    return jsonify({'success': True})

@app.route('/chat', methods=['POST'])
def chat():
    global chat_history
    message = request.form['message']
    chat_history.append(message)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
