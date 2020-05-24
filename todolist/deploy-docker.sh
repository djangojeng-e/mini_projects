# !/usr/bin/env sh 
IDENTITY_FILE="$HOME/.ssh/newtodolist.pem"
HOST="ubuntu@3.34.3.36"
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
docker build -t todolist ~/mini_projects/todolist

# docker image tag 
echo "Docker image tag"
docker tag todolist:latest headfat1218/todolist:latest

# docker push 
echo "docker push"
docker push headfat1218/todolist:latest

# docker stop 
echo "docker stop"
${SSH_CMD} -C "sudo docker stop todolist"

# docker pull 
echo "docker pull"
${SSH_CMD} -C "sudo docker pull headfat1218/todolist:latest"

# screen 에서 docker run 
echo "screen settings"
${SSH_CMD} -C 'screen -X -S docker quit'

# screen 실행 
${SSH_CMD} -C 'screen -S docker -d -m'

# 실행중인 세션에 명령어 전달 
${SSH_CMD} -C "screen -r docker -X stuff 'sudo docker run --rm -it -p 80:8000 --name todolist headfat1218/todolist:latest\n'"

echo "Finish!"