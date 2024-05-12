# Software_Engineering——海洋牧场监测可视化系统

## 项目简介

该项目为软件工程第7组团队项目代码仓库。

海洋牧场监测可视化系统是一个用于监测海洋牧场活动的可视化工具，将处理后的数据以图形化的方式展示出来，使得用户可以直观地了解海洋牧场的运行状况和趋势，同时也包含了用户的注册与登录功能。

## 功能实现

- 用户注册与登录：实现了数据库的连接，能够创建和储存用户信息。
- 权限管理：实现了用户和管理员两种角色，针对不同的角色提供相应的功能和界面。
- 页面框架：主要页面有主要信息、水下系统、数据中心、智能中心、管理员管理界面五个界面，实现了页面跳转功能，并且构建基本布局。

## 安装

### 运行环境

- Node.js: 20.13.0
- pnpm: 9.1.0
- Python: 3.6
- SQLite3

### 前端安装环境和运行

```
pnpm install

pnpm update

pnpm run serve
```

### 后端安装环境和运行

```
安装

pip install -r requirements.txt

运行后端

python manage.py migrate

python manage.py runserver
```

## 友情链接

https://github.com/BinGeHaoShuai/big-screen-datav?tab=readme-ov-file
