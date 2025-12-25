FROM tensorflow/serving:latest

# 安裝 curl 和 tar 用於下載與解壓模型
RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*

# 建立模型資料夾
RUN mkdir -p /models/my_model

# 設定環境變數，告訴 TensorFlow Serving 模型名稱
ENV MODEL_NAME=my_model

# 下載並解壓模型，啟動 TensorFlow Serving
CMD curl -L -o /tmp/model.tar.gz "https://your-storage-url/model.tar.gz" && \
    tar -xzf /tmp/model.tar.gz -C /models/my_model && \
    tensorflow_model_server rest_api_port=8501 model_name=${MODEL_NAME} model_base_path=/models/${MODEL_NAME}
