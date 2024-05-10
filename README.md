# Software_Engineering

## 前端运行
pnpm install

pnpm update(不一定，报错试一下，我node版本较新为v20.10.0，原来环境的包已经被我升级过了)

pnpm run serve


## 后端运行
我使用的是anaconda创建环境,Python版本为3.6:

conda create -n myenv python=3.6

pip install -r requirements.txt

conda activate激活后

python manage.py migrate

python manage.py runserver