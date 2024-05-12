# Software_Engineering——海洋牧场监测可视化系统

## 一、项目简介

该项目为软件工程第7组团队项目代码仓库。

海洋牧场监测可视化系统是一个用于监测海洋牧场活动的可视化工具，将处理后的数据以图形化的方式展示出来，使得用户可以直观地了解海洋牧场的运行状况和趋势，同时也包含了用户的注册与登录功能。

## 二、项目框架

```
├─ README.md                        // 项目说明文档
├─ babel.config.js                  // Babel配置文件
├─ backend                          // 后端目录
│  ├─ __init__.py                  // 后端包初始化文件
│  ├─ api
│  │  ├─ __init__.py               // API包初始化文件
│  │  ├─ admin.py                  // 后台管理相关视图
│  │  ├─ apps.py                   // 应用配置
│  │  ├─ migrations                // 数据库迁移目录
│  │  ├─ models.py                 // 数据库模型
│  │  ├─ tests.py                  // 测试文件
│  │  └─ views.py                  // 视图处理函数
│  ├─ settings
│  │  ├─ __init__.py               // Django设置初始化文件
│  │  ├─ dev.py                    // 开发环境设置
│  │  └─ prod.py                   // 生产环境设置
│  ├─ urls.py                      // URL配置
│  └─ wsgi.py                      // WSGI配置
├─ manage.py                        // Django管理脚本
├─ package-lock.json                // npm包版本锁定文件
├─ package.json                     // 项目依赖配置文件
├─ pnpm-lock.yaml                  // pnpm包版本锁定文件
├─ public                           // 公共资源目录
│  ├─ data
│  │  └─ asset
│  │     └─ image
│  │        └─ situation
│  │           ├─ errorimage.jpg   // 错误图片
│  │           ├─ fish.jpg         // 鱼类图片
│  │           └─ hardware.jpg     // 硬件图片
│  ├─ favicon.ico                  // 网站图标
│  ├─ image.png                    // 图片文件
│  ├─ index.html                   // 入口HTML文件
│  ├─ other_image.png              // 其他图片文件
│  └─ other_image2.png             // 其他图片文件
├─ requirements.txt                 // Python依赖列表
├─ src                              // 前端源码目录
│  ├─ App.vue                      // 根组件
│  ├─ assets                        // 资源文件夹
│  ├─ common                        // 公共组件目录
│  │  ├─ echart                     // ECharts组件
│  │  │  ├─ index.vue               // ECharts组件入口文件
│  │  │  └─ theme.json              // ECharts主题配置文件
│  │  └─ map                        // 地图组件
│  ├─ components                   // 组件目录
│  ├─ main.js                      // 主程序入口文件
│  ├─ router                       // 路由配置目录
│  │  └─ index.js                  // 路由配置文件
│  ├─ services                     // 服务目录
│  ├─ store                        // 状态管理目录
│  ├─ utils                        // 工具目录
│  └─ views                        // 视图目录
│     ├─ Aindex.vue                // 管理员页面视图组件
│     ├─ Login.vue                 // 登录页面视图组件
│     ├─ Register.vue              // 注册页面视图组件
│     ├─ Uindex.vue                // 用户页面视图组件
│     ├─ admin                     // 后台管理页面目录
│     │  ├─ component              // 组件目录
│     │  │  ├─ GaugeChart.vue     // 仪表图组件
│     │  │  ├─ Situation.vue      // 情况组件
│     │  │  ├─ Userdata.vue       // 用户数据组件
│     │  │  ├─ bottom.vue         // 底部组件
│     │  │  ├─ centerMap.vue      // 中心地图组件
│     │  │  ├─ leftContent.vue    // 左侧内容组件
│     │  │  └─ rightContent.vue   // 右侧内容组件
│     │  └─ index.vue             // 后台管理首页视图组件
│     ├─ datacenter                // 数据中心页面目录
│     │  ├─ components             // 组件目录
│     │  │  ├─ envCenter.vue      // 数据中心组件
│     │  │  ├─ envLeft.vue        // 数据中心左侧组件
│     │  │  ├─ envMap.vue         // 数据中心地图组件
│     │  │  └─ envRight.vue       // 数据中心右侧组件
│     │  └─ index.vue             // 数据中心首页视图组件
│     ├─ information               // 信息中心页面目录
│     │  ├─ component              // 组件目录
│     │  │  ├─ info_left.vue      // 信息中心左侧组件
│     │  │  ├─ info_mid.vue       // 信息中心中间组件
│     │  │  └─ info_right.vue     // 信息中心右侧组件
│     │  └─ index.vue             // 信息中心首页视图组件
│     ├─ intelligent               // 智能系统页面目录
│     │  ├─ components             // 组件目录
│     │  │  ├─ ecoCenter.vue      // 智能系统组件
│     │  │  ├─ ecoLeft.vue        // 智能系统左侧组件
│     │  │  └─ ecoRight.vue       // 智能系统右侧组件
│     │  └─ index.vue             // 智能系统首页视图组件
│     └─ underwater                // 水下页面目录
│        ├─ components             // 组件目录
│        │  ├─ water_left.vue     // 水下系统左侧组件
│        │  ├─ water_mid.vue      // 水下系统中间组件
│        │  └─ water_right.vue    // 水下系统右侧组件
│        └─ index.vue             // 水下系统首页视图组件
├─ test                             // 测试目录
│  └─ test.txt                      // 测试文件
├─ vue.config.js                    // Vue配置文件
└─ yarn.lock                        // Yarn包版本锁定文件

```
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

https://github.com/BinGeHaoShuai/big-screen-datav?tab=readme-ov-file

https://github.com/gtalarico/django-vue-template

https://github.com/goodgoodgreat/Digital-twin-big-screen