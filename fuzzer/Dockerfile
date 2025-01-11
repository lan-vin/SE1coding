FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y libtool build-essential cmake python3 gcc llvm clang file binutils

WORKDIR /app
COPY . /app

CMD ["python3", "src/main.py"]

# 使用 Docker 构建并运行项目
# docker build -t fuzz-testing-tool
# docker run fuzz-testing-tool