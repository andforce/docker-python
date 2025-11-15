# build
sudo docker build -t ghcr.io/andforce/py_torch_clip_flask .

# test

# 运行容器
docker run -d -p 10000:10000 --name your-app-container your-app:latest

# 或者以交互模式运行（用于调试）
docker run -it -p 10000:10000 --name your-app-container your-app:latest
docker run -it -p 10000:10000 --name card ghcr.io/andforce/py_torch_clip_flask:latest

# 查看运行日志
docker logs your-app-container

# 进入容器内部
docker exec -it your-app-container bash



# push
## public
sudo docker push ghcr.io/andforce/py_torch_clip_flask:latest


## private
https://github.com/settings/tokens
# 生成 token 时，选择 read:packages 和 write:packages 权限

# 先登录（同上）
sudo docker login ghcr.io -u YOUR_GITHUB_USERNAME
sudo docker login ghcr.io -u andforce (input token as password)
# 然后拉取
sudo docker pull ghcr.io/andforce/py_torch_clip_flask:latest