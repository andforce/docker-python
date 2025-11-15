import clip
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # 测试 CLIP 和 PyTorch 是否正常工作
    model, preprocess = clip.load("ViT-B/32", device="cpu")

    return {
        "message": "Hello from Docker!",
        "clip_loaded": True
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10002, debug=True)