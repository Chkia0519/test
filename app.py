from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# TensorFlow Serving REST API URL
TF_SERVING_URL = "http://localhost:8501/v1/models/my_model:predict"

@app.route('/predict', methods=['POST'])
def predict():
    # 從前端取得輸入資料（假設是 JSON 格式）
    input_data = request.json

    # 建立 TensorFlow Serving 所需的請求格式
    # 假設模型輸入名稱是 'instances'，資料格式依模型而定
    payload = {
        "instances": input_data["instances"]
    }

    # 發送 POST 請求給 TensorFlow Serving
    response = requests.post(TF_SERVING_URL, json=payload)

    if response.status_code == 200:
        prediction = response.json()
        return jsonify(prediction)
    else:
        return jsonify({"error": "TensorFlow Serving request failed", "details": response.text}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
