import torch
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # 测试 CLIP 和 PyTorch 是否正常工作
    device = "cuda" if torch.cuda.is_available() else "cpu"

    return {
        "message": "Hello from Docker!",
        "pytorch_version": torch.__version__,
        "device": device,
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)