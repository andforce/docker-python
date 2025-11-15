# 使用 Python 3.10 官方镜像作为基础
# 指定 linux/amd64 平台以便在 Ubuntu x86_64 上运行
FROM ubuntu:22.04

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 安装 PyTorch 和 CLIP 依赖
# 这里使用 CPU 版本的 PyTorch，如果你需要 GPU 版本可以调整
RUN pip3 install --no-cache-dir --upgrade pip

# # 配置 pip 源和超时时间
# RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
#     pip3 config set global.timeout 120

# 复制 requirements.txt 文件（先复制这个文件以便利用 Docker 缓存）
COPY requirements.txt .

# 安装 Python 依赖
RUN pip3 install --no-cache-dir -r requirements.txt


# 复制应用代码
COPY . .

# 暴露端口（根据你的应用调整）
EXPOSE 10000

# 设置启动命令（根据你的应用调整）
CMD ["python3", "app.py"]