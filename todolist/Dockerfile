FROM ubuntu:18.04
RUN     apt-get -y update 
RUN     apt-get -y dist-upgrade 
ARG     DEBIAN_FRONTEND=noninteractive
ENV     TZ=Asia/Seoul
RUN     apt-get install -y tzdata

RUN     apt-get install -y python-pip git vim 


RUN     apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev 
RUN     curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV     PATH /root/.pyenv/bin:$PATH
RUN     pyenv install 3.8.0


RUN     apt-get install -y zsh
RUN     wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN     chsh -s /usr/bin/zsh


RUN         echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.zshrc
RUN         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
RUN         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc


RUN     pyenv virtualenv 3.8.0 todolist

