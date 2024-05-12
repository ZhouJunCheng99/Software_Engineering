# Software_Engineering——海洋牧场监测可视化系统

## 一、项目简介

该项目为软件工程第7组团队项目代码仓库。

海洋牧场监测可视化系统是一个用于监测海洋牧场活动的可视化工具，将处理后的数据以图形化的方式展示出来，使得用户可以直观地了解海洋牧场的运行状况和趋势，同时也包含了用户的注册与登录功能。

## 二、主要文件介绍
### 前端界面主要文件介绍
| 文件                | 作用/功能                                                              |
| ------------------- | --------------------------------------------------------------------- |
| main.js             | 主目录文件，引入 Echart/DataV 等文件                                    |
| utils               | 工具函数与 mixins 函数等                                                |
| views/ Aindex.vue    | 管理员项目主结构                                                             |
| views/ Login.vue    | 用户登录界面                                                             |
| views/ Register.vue    | 用户注册界面                                                             |
| views/ Uindex.vue    | 普通用户项目主结构                                                             |
| views/其余文件       | 界面各个区域组件（按照位置来命名）                                       |
| assets              | 静态资源目录，放置 logo 与背景图片                                       |
| assets / style.scss | 通用 CSS 文件，全局项目快捷样式调节                                      |
| assets / index.scss | Index 界面的 CSS 文件                                                  |
| components/echart   | 所有 echart 图表（按照位置来命名）                                      |
| common/...          | 全局封装的 ECharts 和 flexible 插件代码（适配屏幕尺寸，可定制化修改）     |

### 后端主要文件介绍
| 文件                | 作用/功能                                                              |
| ------------------- | --------------------------------------------------------------------- |
| urls.py             | URL配置                                    |
| wsgi.py             | WSGI配置                                    |
| api/admin.py             | 管理员相关视图                                    |
| api/apps.py             | 应用配置                                    |
| api/models.py             | 数据库模块                                    |
| api/tests.py             | 测试文件                                    |
| api/views.py             | 视图处理函数                                    |
| api/migrations             | 数据库迁移目录                                    |
| settings/             | 开发环境配置                                    |                           |


## 三、功能实现

- 用户注册与登录：实现了数据库的连接，能够创建和储存用户信息。
- 权限管理：实现了用户和管理员两种角色，针对不同的角色提供相应的功能和界面。
- 页面框架：主要页面有主要信息、水下系统、数据中心、智能中心、管理员管理界面五个界面，实现了页面跳转功能，并且构建基本布局。

## 四、环境配置

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

## 五、友情链接

https://github.com/BinGeHaoShuai/big-screen-datav