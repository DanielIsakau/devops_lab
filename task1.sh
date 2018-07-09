#!/bin/bash
yum install git gcc gcc-c++ zlib libffi-devel openssl-devel zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel mysql-devel -y

#curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
#echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.bash_profile
#echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
#echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

pyenv install 2.7.15
pyenv install 3.5.5

pyenv virtualenv 2.7.15 python2 
pyenv virtualenv 3.5.5 python3

