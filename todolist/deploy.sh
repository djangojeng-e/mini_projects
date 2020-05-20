# !/usr/bin/env sh 
IDENTITY_FILE="$HOME/.ssh/newtodolist.pem"
HOST="ubuntu@52.79.175.188"
ORIGIN_SOURCE="$HOME/mini_projects/todolist/"
DEST_SOURCE="/home/ubuntu/todolist/"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${HOST}"

echo "== runserver 배포 =="

# pip freeze 
echo "pip freeze"
"$HOME"/.pyenv/versions/3.8.0/envs/to-do-list/bin/pip freeze > "$HOME"/mini_projects/todolist/requirements.txt

# 기존 폴더 삭제 
echo "remove server source"
${SSH_CMD} sudo rm -rf ${DEST_SOURCE}

# 로컬에 있는 파일 업로드 
echo "upload local source"
${SSH_CMD} mkdir /home/ubuntu/todolist
scp -q -i "${IDENTITY_FILE}" -r "${ORIGIN_SOURCE}" ${HOST}:${DEST_SOURCE}

# pip install 
echo "pip install"
${SSH_CMD} pip3 install -q -r /home/ubuntu/todolist/todolist/requirements.txt

echo "screen settings"
# 실행중이던 screen 세션 종료 
${SSH_CMD} -C 'screen -X -s runserver quit'
# screen 실행 
${SSH_CMD} -C 'screen -S runserver -d -m'
# 실행중인 세션에 명령어 전달 
${SSH_CMD} -C "screen -r runserver -X stuff 'sudo python3 /home/ubuntu/todolist/todolist/manage.py runserver 0:80\n'"


echo " Finish!"