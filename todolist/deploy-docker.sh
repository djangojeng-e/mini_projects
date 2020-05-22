# !/usr/bin/env sh 
IDENTITY_FILE="$HOME/.ssh/newtodolist.pem"
HOST="ubuntu@52.79.175.188"
ORIGIN_SOURCE="$HOME/mini_projects/todolist/"
DEST_SOURCE="/home/ubuntu/todolist/"
DOCKER_REPO="headfat1218/todolist"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${HOST}"


echo "=== Docker 배포 ==="

# 서버 초기 설정 
echo "apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt update && sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y && apt -y autoremove'
echo "apt install docker.io"
${SSH_CMD} -C 'sudo apt -y install docker.io'


# pip freeze 
echo "pip freeze"
"$HOME"/.pyenv/versions/3.8.0/envs/to-do-list/bin/pip freeze > "$HOME"/mini_projects/todolist/requirements.txt




# docker build 
echo "Docker build"
docker build -q -t ${DOCKER_REPO} -f Dockerfile "$HOME"/mini_projects/todolist/

# docker push 
echo "docker push"
docker push ${DOCKER_REPO}

# docker stop 
echo "docker stop"
${SSH_CMD} -C "sudo docker stop todolist"

# 
