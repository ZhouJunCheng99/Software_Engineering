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



```
Software_Engineering
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ branches
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-applypatch
│  │  ├─ post-checkout
│  │  ├─ post-commit
│  │  ├─ post-merge
│  │  ├─ post-receive
│  │  ├─ post-rewrite
│  │  ├─ post-update
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-auto-gc
│  │  ├─ pre-commit
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout
│  │  ├─ sendemail-validate
│  │  ├─ update
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  ├─ main
│  │     │  └─ ztz
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           ├─ front-end
│  │           ├─ glb
│  │           ├─ main
│  │           ├─ test
│  │           ├─ ypf
│  │           ├─ zjc
│  │           └─ ztz
│  ├─ objects
│  │  ├─ 03
│  │  │  └─ b12ebc9b732eda19a25bb9e72a1f3f9b50a0c8
│  │  ├─ 07
│  │  │  └─ 64c91944d6468ae1f032e02abe72e8066777d2
│  │  ├─ 08
│  │  │  └─ 4cf6ea776269f79c5d159ccae999a665bdd780
│  │  ├─ 0c
│  │  │  └─ 4c20858bf0d10e3387be572a4e152f78281907
│  │  ├─ 0d
│  │  │  ├─ 776f8fc5bf1c63da1c8a3d9307219eb1e71181
│  │  │  └─ ec3988d22adc0693202a25f50d846265a10437
│  │  ├─ 0e
│  │  │  ├─ 3c2a50157e42916030af40ade591ce3d907e21
│  │  │  ├─ bf3a13e5113a0aad5110e124cf71c833e028f1
│  │  │  └─ f7af6b3a1b342f0f361e34fc4122e8776ec43d
│  │  ├─ 11
│  │  │  ├─ 0e061958f1bb01857809a21f04c7737ca808c1
│  │  │  ├─ 50fa1207058b9898f07e5bc06d327be9a43293
│  │  │  └─ a770cdbc00ddfb741a84e1658633449363dc70
│  │  ├─ 12
│  │  │  ├─ 3f065d97561eb1e6bfa1fe9fc787d006c5a1e1
│  │  │  └─ 9ab9f0f2aa18afdc99ca3da18d993aa8391892
│  │  ├─ 13
│  │  │  ├─ 0aa27e5e473b43b8de65ff72e3a2b2363af5f8
│  │  │  └─ 7f1caf71e17b299de9028ea2e473a2790e9053
│  │  ├─ 16
│  │  │  ├─ 907ac47e5d688fedf422ad8384074ff6977e3f
│  │  │  └─ a21a5801983989890ba3585783d6ca115602fa
│  │  ├─ 1a
│  │  │  └─ ae644857f703a7db08a39ebe73ad9577437ca3
│  │  ├─ 1c
│  │  │  └─ b107b8765aa99e969aea693fedf08834d8e6c9
│  │  ├─ 1e
│  │  │  ├─ 7711cb3032dd5a25079280c655375a957f7243
│  │  │  └─ 9025b98fb12eca153b25da794d66885efea4de
│  │  ├─ 1f
│  │  │  └─ 68e2e9ca38143e6bc36ae67ea1feeaaa83afb8
│  │  ├─ 21
│  │  │  └─ b0d0d28ffc13e76f6804eabb1ca8660e59fd10
│  │  ├─ 24
│  │  │  └─ 9b133004042f14428b406593ba43a76eb992a6
│  │  ├─ 27
│  │  │  ├─ 511c9d80ed02c21307448172e581d343d7dbbf
│  │  │  └─ a769feb383be7f5b72b30d99540e086d33db01
│  │  ├─ 29
│  │  │  ├─ 74674bae506200a7fd003a15bbdf7516c31181
│  │  │  └─ 868aeeae98c60d6965c8783c1a3e22db389639
│  │  ├─ 2a
│  │  │  └─ 9cff31280780e79638fd140ea4596850c4ee33
│  │  ├─ 2c
│  │  │  └─ f7569204f0ef351606186651f8c84fc4eee533
│  │  ├─ 2e
│  │  │  └─ 3e38eb3437ef8801e7ff0986a981c5c68aed5a
│  │  ├─ 32
│  │  │  └─ 2ab2af25dd78b15f198b462031a6008d393d9e
│  │  ├─ 36
│  │  │  └─ 57a4d18cdf0908548d39c142ed75aa9a5290db
│  │  ├─ 38
│  │  │  └─ 8bfe8fe043f9dada787119d5b482bd5f2fc476
│  │  ├─ 39
│  │  │  └─ f7d51adc4bc961eae41c1d04dc62594bd05e61
│  │  ├─ 3b
│  │  │  ├─ 4df31d40a5a239c8abc445349f491b4c391543
│  │  │  ├─ b378360fbdb4eace1302405c3cd3cd3db9b253
│  │  │  └─ d9439ae85ab412c1247bf455d7b44cc99c169d
│  │  ├─ 3c
│  │  │  ├─ 2bc32e89b38b31e5367c4ab9cf6b9650e568ef
│  │  │  ├─ 4c31d941e14011bde9cb4d67b12806879cebe4
│  │  │  ├─ b4a274409d6d968ea365c4bf9f1584f883ea22
│  │  │  └─ f250e42e1fbc4d0f7edce58fc55d20b79cc649
│  │  ├─ 3e
│  │  │  └─ b1b81c19b8775b8a3404ec65e575f18b40b4b0
│  │  ├─ 3f
│  │  │  └─ bb84fab781bd015610e214890c3736ea9780ec
│  │  ├─ 40
│  │  │  ├─ 0430812731af82af066be9e9df4d7cb9f1946b
│  │  │  └─ eb874a26d70f3eece7c139dba3f8750bd6e171
│  │  ├─ 41
│  │  │  └─ facd1f4e66b9f2a2e5debac2a435fad3d46013
│  │  ├─ 42
│  │  │  └─ 7064bfdaab3ca594b646f6c14ea6593c146f78
│  │  ├─ 48
│  │  │  └─ 95cc4f7ecadd742d396a92841979fed9ac80b3
│  │  ├─ 49
│  │  │  └─ cec6aa6ce8e40210ed31c1bb3eced5ab9afd01
│  │  ├─ 4f
│  │  │  └─ cf2df691922ea547860f017eb7708390ce053e
│  │  ├─ 51
│  │  │  ├─ 2fc078d8f2ef628b949ebf07d152217b5b75ae
│  │  │  ├─ d04cc078fad0d8d46fb11096e559507e37ec17
│  │  │  └─ fb269ffb65b9c3ed602f315ae353c7cbeb507b
│  │  ├─ 55
│  │  │  └─ 5007343ba468e69be126e31681ec9d3a6d5dd2
│  │  ├─ 57
│  │  │  └─ 66a1c8e5ac5c80fd2bf8943d72509eb9e2288d
│  │  ├─ 58
│  │  │  └─ a1da05d8373cf1eaf6203dfce3e55fe7917d94
│  │  ├─ 5a
│  │  │  └─ 0dd3d18e572d81f537c52f1784dea110062bd9
│  │  ├─ 5b
│  │  │  └─ 54119e7693a8865d028a6355092d60c9fcb172
│  │  ├─ 5d
│  │  │  └─ ce65bfdab66f6a5108db40fbd6f20c1981904c
│  │  ├─ 5e
│  │  │  ├─ 90162a5fca3e93b6448632f1130748d5d86638
│  │  │  └─ ac948cbb6950e48db56d147ff266e5ff70a90d
│  │  ├─ 5f
│  │  │  ├─ 1450ae952e572035c4748dcc1cb72d5baf82c9
│  │  │  └─ 786847bb11eb7ba463649887e5669cd8cd9970
│  │  ├─ 60
│  │  │  └─ 869f4484898c19014b0c7c0bc4f7b0c0ee88a7
│  │  ├─ 61
│  │  │  ├─ 05a61e3dc56701a946292d2ec918efb4e7d162
│  │  │  └─ 651117eff7860bc5427a2a79c65a3f0dfc8d2a
│  │  ├─ 62
│  │  │  └─ 7725ba130d3c5b1a43ecd8e31c379c15e7b3dd
│  │  ├─ 64
│  │  │  └─ c3803940b6b8f502d36a3153a05ae5b8babf4a
│  │  ├─ 66
│  │  │  ├─ 6c2d424fcb384574f35f8c85959097e100b4c1
│  │  │  └─ b7d2a4e6c4e21e6b6bfef1d3a8bb615f6bfe88
│  │  ├─ 6c
│  │  │  └─ bea4f4408d45142ae5141e125e828b1d9c08a2
│  │  ├─ 6e
│  │  │  ├─ 5be9111c556d8476b4f094c90cea0637b80f15
│  │  │  └─ b2b0b236418ee486646b661ca91df6e99a533c
│  │  ├─ 6f
│  │  │  └─ ecaf06540e0a94e05896a97e8d0951b847ff7a
│  │  ├─ 72
│  │  │  ├─ 0f97e9a90a1fc91199acb734f706bfea18b3db
│  │  │  └─ 68c84b85b91fdab3e2a6fe0f5b8c6edee972af
│  │  ├─ 76
│  │  │  └─ f73d04bc3dd00451b67ff909da9df8bbdf0794
│  │  ├─ 77
│  │  │  └─ 4e2bd6df45fc86da4b12662fb2157d70514670
│  │  ├─ 78
│  │  │  └─ 1245116fd7f224a98b7a85097878672172ee4a
│  │  ├─ 79
│  │  │  ├─ 016d3c2f81c34345fad3549e4f75b988c140c0
│  │  │  └─ 615d01c21d4b6f5f73f0d7d0f438252057b851
│  │  ├─ 7a
│  │  │  └─ 8cb2e4b66a1263f19358908948f5239c81b512
│  │  ├─ 7b
│  │  │  └─ d767b0ca160ce8476cff890d8d0c16185b5012
│  │  ├─ 7c
│  │  │  └─ e503c2dd97ba78597f6ff6e4393132753573f6
│  │  ├─ 7d
│  │  │  └─ 61e0b317c08e844794f367b875cbf629dcc226
│  │  ├─ 7f
│  │  │  └─ b5507f0fc27a34b7dc2b2f45a7f7959dea4cf6
│  │  ├─ 80
│  │  │  └─ 41da6c2e68bad8b84b785fbc21499a87d84a49
│  │  ├─ 88
│  │  │  └─ c08a3daf21dbf69a6109546185cb9e4b57ca99
│  │  ├─ 8c
│  │  │  └─ 38f3f3dad51e4585f3984282c2a4bec5349c1e
│  │  ├─ 92
│  │  │  └─ 8688f439fa9544145fbfbdf04e9840ef923a49
│  │  ├─ 94
│  │  │  └─ 47a9fbfa0a4df3749f0ad8cf1b3340ed47468f
│  │  ├─ 9a
│  │  │  ├─ 69edd3375d391cec7ad9a1a9933918a543de14
│  │  │  └─ 731726e4e07a7235fa330ed9186ad9a881694a
│  │  ├─ 9c
│  │  │  └─ 94a07541ed73f05035d9700ab0f4976f4e321c
│  │  ├─ 9d
│  │  │  └─ 7c64c2217cad346384eb85a8fdabe313206081
│  │  ├─ 9e
│  │  │  └─ c19888afa7ec9ae66d771f67f5da518c5c9df9
│  │  ├─ a1
│  │  │  └─ b84c2d0e7d212fb6e22fb0c2b03f8deca20bdb
│  │  ├─ a3
│  │  │  ├─ 19e25207065400d539d161ad68c27d10cb1407
│  │  │  └─ f772f9530f77f5de4797c509b82e05b1e3fc5a
│  │  ├─ a8
│  │  │  └─ ffd0c630a7fb1d5f99999892a934f1a89168b7
│  │  ├─ aa
│  │  │  ├─ a72d0eec146ba53517ca0945ba7c3eee70ec82
│  │  │  └─ f6249122b839bd9354f0e75e6415d4d855c2c2
│  │  ├─ ab
│  │  │  └─ 103bf651d125f428cc2272a8167241c0356f32
│  │  ├─ ae
│  │  │  └─ 0fde01df9ca3550052a2418e7b24b63633e101
│  │  ├─ b0
│  │  │  ├─ 38d95e26fae8683c02f25baf3bc53cb4866516
│  │  │  └─ c6a6b81ba565c577dc6defabef1740c2b38a63
│  │  ├─ b1
│  │  │  └─ d65f3d8147cb5409a33e70b4cfd53f3091387c
│  │  ├─ b4
│  │  │  └─ 7647b74c32fcca272be76808b15ae32321bf7f
│  │  ├─ b7
│  │  │  └─ 3f313fc4cbf1683a818fa63b6591644e3930c8
│  │  ├─ b9
│  │  │  └─ 6acfcb1333bfc795d0782b9a83c73ee1c522f7
│  │  ├─ be
│  │  │  └─ 8fe564d5e9899c837bb70a16eaece306a33627
│  │  ├─ c0
│  │  │  └─ 31bed356f182a34be2617b9c8ba7e455e178cc
│  │  ├─ c2
│  │  │  └─ 1468ec0c8c55362f5cc23bd649c14c2b97f837
│  │  ├─ c6
│  │  │  └─ 49afb63eceea06a7b8496fbd002ec4ec7e19b2
│  │  ├─ c8
│  │  │  └─ e3f95c8d0e448fad0c462f9e68d32bc6c41fa9
│  │  ├─ ca
│  │  │  ├─ ae6ec1a6ea1b63fe7022419f09bb205c10d9af
│  │  │  └─ dc311b48c5755aa512af6b44de7ac11febef99
│  │  ├─ cb
│  │  │  ├─ 6eb9eaa12a3d3fefee57acba4ec8341536cb5f
│  │  │  └─ ae1c9b5309d0de7f659ca92d52eff27db608b9
│  │  ├─ cc
│  │  │  ├─ 1d61d1421265daa872f04a31fbe8818ad04fde
│  │  │  ├─ a9f8038d285a46b87c0f1824584cd204d9c0b0
│  │  │  └─ b992cce58f74b544633430adf976ffdfa60b83
│  │  ├─ d0
│  │  │  └─ 25f7f12eb11f0b193bcb26ed0ef4a56efd6add
│  │  ├─ d6
│  │  │  └─ 0f0c4c40fc88f29c7466ca1e2e92f21c205afe
│  │  ├─ d8
│  │  │  ├─ 429ddff51d768bd97260b5953c8af65de2838d
│  │  │  ├─ bae1f3c17b8c6aaaaf9b9c73688cc6cae2bd85
│  │  │  └─ d1ac3a51c094210985ecb2c2d45a70c60318f5
│  │  ├─ da
│  │  │  ├─ 867d67a328edb6b0a6b8bac5387f2b73c8e55a
│  │  │  ├─ d9b897205065dc52e0252e0d245e76c7fb2516
│  │  │  └─ fb66874149e015f5b30a81a531f633a97a91fb
│  │  ├─ dc
│  │  │  ├─ 144ae5e20ef1b5b2b1370778eb9fd159100473
│  │  │  └─ 3a9b76d20ba41e32cb06100fa13fbc7c99d537
│  │  ├─ e1
│  │  │  ├─ 7a4556b5c68db5dfd4d67222c9eb2a480897f1
│  │  │  └─ fd005dd71ce789c2a76e20478c960fae517eea
│  │  ├─ e3
│  │  │  └─ 8c6fd99b2bd8da3a482a059584e1184489e021
│  │  ├─ e7
│  │  │  ├─ 15447844866395088d0c36520d634444cc4e06
│  │  │  └─ b5b432bad9be4d74153b4eb9dd746de5a41ef4
│  │  ├─ eb
│  │  │  └─ fdc4756739f0388b9291ee1a53ac936f617bef
│  │  ├─ ec
│  │  │  └─ 062d4e8bbd7938329adc98108d3fee3acb543f
│  │  ├─ ef
│  │  │  └─ 9c2df2ecf9cc1ed092e29e9392b7c5daf521a1
│  │  ├─ f0
│  │  │  ├─ 2d6c526a1f53ef7e8392704dc9988b93462b2f
│  │  │  └─ 34f3770122fb1f2102be179c8086fe3e22100e
│  │  ├─ f1
│  │  │  ├─ 26842c564c4accb94719299be17ac4aa0e7fed
│  │  │  └─ 4feea36d45727872b6443e82df0e7a412d3a80
│  │  ├─ f2
│  │  │  └─ 4695213932e1764ce0474c1d43d668ec8b7b64
│  │  ├─ f6
│  │  │  └─ feee8cc7ae2e5fb3c88edf08473d000bea2374
│  │  ├─ f7
│  │  │  └─ 834f66b8bc986c660452dbf9893cee8ae9c214
│  │  ├─ fb
│  │  │  └─ 8b8adabfdfc9f9a50221c0693ff0daeba79e3e
│  │  ├─ fe
│  │  │  ├─ 10a8b67851d929def508031efe0e6629d981fc
│  │  │  ├─ 47b44d33b8a9cb3f2ffc6817b6b65c04901a77
│  │  │  └─ b043df41d22fed78144b18d434eff0521eedb8
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-2e0be98ff78759855503a72c23766243ec655771.idx
│  │     ├─ pack-2e0be98ff78759855503a72c23766243ec655771.pack
│  │     ├─ pack-98368b7e9db0c2b54024ba7a060965ee86935c94.idx
│  │     └─ pack-98368b7e9db0c2b54024ba7a060965ee86935c94.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  ├─ main
│     │  └─ ztz
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     ├─ front-end
│     │     ├─ glb
│     │     ├─ main
│     │     ├─ test
│     │     ├─ ypf
│     │     ├─ zjc
│     │     └─ ztz
│     └─ tags
├─ .gitignore
├─ LICENSE
├─ README.md
├─ babel.config.js
├─ backend
│  ├─ __init__.py
│  ├─ api
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_auto_20240511_2150.py
│  │  │  ├─ 0003_message_permission.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  └─ views.py
│  ├─ settings
│  │  ├─ __init__.py
│  │  ├─ dev.py
│  │  └─ prod.py
│  ├─ urls.py
│  └─ wsgi.py
├─ manage.py
├─ package-lock.json
├─ package.json
├─ pnpm-lock.yaml
├─ public
│  ├─ data
│  │  └─ asset
│  │     └─ image
│  │        └─ situation
│  │           ├─ errorimage.jpg
│  │           ├─ fish.jpg
│  │           └─ hardware.jpg
│  ├─ favicon.ico
│  ├─ image.png
│  ├─ index.html
│  ├─ other_image.png
│  └─ other_image2.png
├─ requirements.txt
├─ src
│  ├─ App.vue
│  ├─ assets
│  │  ├─ iconfont
│  │  │  ├─ iconfont.css
│  │  │  ├─ iconfont.eot
│  │  │  ├─ iconfont.svg
│  │  │  ├─ iconfont.ttf
│  │  │  ├─ iconfont.woff
│  │  │  └─ iconfont.woff2
│  │  ├─ img
│  │  │  ├─ aml.png
│  │  │  ├─ back_chart.png
│  │  │  ├─ bg-1.png
│  │  │  ├─ bg-2.jpg
│  │  │  ├─ bg-4.jpg
│  │  │  ├─ bg-5.jpg
│  │  │  ├─ bj.jpg
│  │  │  ├─ bk_circle.png
│  │  │  ├─ bk_circle1.png
│  │  │  ├─ bk_circle2.png
│  │  │  ├─ brand
│  │  │  │  ├─ bg.jpg
│  │  │  │  ├─ head_bg.png
│  │  │  │  ├─ head_bg2.png
│  │  │  │  ├─ jt.png
│  │  │  │  ├─ lbx.png
│  │  │  │  ├─ lei.png
│  │  │  │  ├─ line.png
│  │  │  │  ├─ map.png
│  │  │  │  ├─ qing.png
│  │  │  │  ├─ shachen.png
│  │  │  │  ├─ wu.png
│  │  │  │  ├─ xue.png
│  │  │  │  ├─ yin.png
│  │  │  │  ├─ yu.png
│  │  │  │  └─ yun.png
│  │  │  ├─ chart1
│  │  │  │  ├─ compass-bg-1.png
│  │  │  │  ├─ compass-bg-2.png
│  │  │  │  ├─ compass-bg-3.png
│  │  │  │  ├─ compass-bg-4.png
│  │  │  │  └─ line-fs.png
│  │  │  ├─ chart2
│  │  │  │  ├─ icon_db01.png
│  │  │  │  ├─ icon_db02.png
│  │  │  │  ├─ icon_db03.png
│  │  │  │  ├─ icon_db04.png
│  │  │  │  ├─ icon_jt01.png
│  │  │  │  ├─ icon_jt02.png
│  │  │  │  ├─ icon_xfq01.png
│  │  │  │  ├─ icon_xfq02.png
│  │  │  │  ├─ icon_xfq03.png
│  │  │  │  └─ icon_xfq04.png
│  │  │  ├─ cir-1.png
│  │  │  ├─ cir-2.png
│  │  │  ├─ circle2.png
│  │  │  ├─ css565.png
│  │  │  ├─ dynamic
│  │  │  │  ├─ info-1-0.png
│  │  │  │  ├─ info-1-1.png
│  │  │  │  ├─ info-1-2.png
│  │  │  │  ├─ info-1-3.png
│  │  │  │  ├─ info-1-4.png
│  │  │  │  ├─ info-bg-01.png
│  │  │  │  ├─ info-bg-02.png
│  │  │  │  ├─ info-bg-03.png
│  │  │  │  ├─ info-bg-04.png
│  │  │  │  ├─ info-icon-1.png
│  │  │  │  ├─ info-icon-2.png
│  │  │  │  ├─ info-icon-3.png
│  │  │  │  ├─ info-icon-4.png
│  │  │  │  ├─ info-line-01.png
│  │  │  │  └─ info-line-02.png
│  │  │  ├─ economy.png
│  │  │  ├─ environment.png
│  │  │  ├─ icon_04.png
│  │  │  ├─ icon_05.png
│  │  │  ├─ icon_circle1.png
│  │  │  ├─ icon_circle2.png
│  │  │  ├─ icon_cs.png
│  │  │  ├─ icon_hs.png
│  │  │  ├─ icon_ls.png
│  │  │  ├─ icon_ml.png
│  │  │  ├─ icon_ql.png
│  │  │  ├─ icon_qql.png
│  │  │  ├─ icon_sl.png
│  │  │  ├─ icon_zs.png
│  │  │  ├─ inner.png
│  │  │  ├─ line-fs.png
│  │  │  ├─ online.png
│  │  │  ├─ pd-main-left-bg-2.png
│  │  │  ├─ pd-main-left-bg-tree.png
│  │  │  ├─ person-1.png
│  │  │  ├─ population.png
│  │  │  ├─ sn-title.png
│  │  │  ├─ tiao.png
│  │  │  ├─ top3.png
│  │  │  ├─ top4.png
│  │  │  ├─ top_nav.png
│  │  │  ├─ toptitle.png
│  │  │  ├─ traffic.png
│  │  │  ├─ tran.png
│  │  │  ├─ wg.png
│  │  │  ├─ whcircle.png
│  │  │  ├─ xie.png
│  │  │  └─ zd.png
│  │  ├─ js
│  │  │  ├─ china.js
│  │  │  ├─ echarts-wordcloud.min.js
│  │  │  ├─ flexible.js
│  │  │  └─ utils.js
│  │  ├─ logo-django.png
│  │  ├─ logo-vue.png
│  │  ├─ logo.png
│  │  ├─ mapStyle.json
│  │  ├─ pageBg.png
│  │  ├─ scss
│  │  │  ├─ _variables.scss
│  │  │  ├─ index.scss
│  │  │  └─ style.scss
│  │  ├─ styles
│  │  │  ├─ base.scss
│  │  │  ├─ common.scss
│  │  │  ├─ fonts
│  │  │  │  ├─ DIGITALDREAMFAT.ttf
│  │  │  │  ├─ DIGITALDREAMFAT.woff
│  │  │  │  └─ DIGITALDREAMFAT.woff2
│  │  │  └─ keyframes.scss
│  │  └─ webm
│  │     └─ CAMERAV.webm
│  ├─ common
│  │  ├─ echart
│  │  │  ├─ index.vue
│  │  │  └─ theme.json
│  │  └─ map
│  │     └─ chongqing.json
│  ├─ components
│  │  ├─ bar3d
│  │  │  └─ index.vue
│  │  ├─ bgAnimation
│  │  │  └─ index.vue
│  │  ├─ cakeLinkage
│  │  │  └─ index.vue
│  │  ├─ circleNesting
│  │  │  └─ index.vue
│  │  ├─ circleRunway
│  │  │  └─ index.vue
│  │  ├─ colorfulArea
│  │  │  └─ index.vue
│  │  ├─ colorfulRadar
│  │  │  └─ index.vue
│  │  ├─ companySummary
│  │  │  ├─ business.vue
│  │  │  ├─ distribution.vue
│  │  │  ├─ history.vue
│  │  │  ├─ income.vue
│  │  │  ├─ talent.vue
│  │  │  └─ wordCloud.vue
│  │  ├─ controlanml
│  │  │  └─ index.vue
│  │  ├─ dynamicLine
│  │  │  └─ index.vue
│  │  ├─ dynamicList
│  │  │  └─ index.vue
│  │  ├─ flashCloud
│  │  │  └─ index.vue
│  │  ├─ footer
│  │  │  ├─ footer.vue
│  │  │  └─ index.css
│  │  ├─ gauge
│  │  │  └─ index.vue
│  │  ├─ index.js
│  │  ├─ modal
│  │  │  └─ index.vue
│  │  ├─ pyramid
│  │  │  └─ index.vue
│  │  ├─ pyramidTrend
│  │  │  └─ index.vue
│  │  ├─ rainbow
│  │  │  └─ index.vue
│  │  ├─ ringPie
│  │  │  └─ index.vue
│  │  ├─ ringPin
│  │  │  └─ index.vue
│  │  ├─ rotateColorful
│  │  │  └─ index.vue
│  │  ├─ scanRadius
│  │  │  └─ index.vue
│  │  ├─ scrollArc
│  │  │  └─ index.vue
│  │  ├─ seamless
│  │  │  └─ index.vue
│  │  ├─ sinan
│  │  │  └─ index.vue
│  │  ├─ staffMix
│  │  │  └─ index.vue
│  │  ├─ szBar
│  │  │  └─ index.vue
│  │  ├─ toast
│  │  │  ├─ index.js
│  │  │  └─ index.vue
│  │  ├─ topanml
│  │  │  └─ index.vue
│  │  └─ waterPolo
│  │     └─ index.vue
│  ├─ main.js
│  ├─ router
│  │  └─ index.js
│  ├─ services
│  │  ├─ api.js
│  │  └─ messageService.js
│  ├─ store
│  │  ├─ index.js
│  │  └─ modules
│  │     └─ messages.js
│  ├─ utils
│  │  ├─ drawMixin.js
│  │  ├─ index.js
│  │  └─ resizeMixin.js
│  └─ views
│     ├─ Aindex.vue
│     ├─ Login.vue
│     ├─ Register.vue
│     ├─ Uindex.vue
│     ├─ admin
│     │  ├─ component
│     │  │  ├─ GaugeChart.vue
│     │  │  ├─ Situation.vue
│     │  │  ├─ Userdata.vue
│     │  │  ├─ bottom.vue
│     │  │  ├─ centerMap.vue
│     │  │  ├─ leftContent.vue
│     │  │  └─ rightContent.vue
│     │  └─ index.vue
│     ├─ datacenter
│     │  ├─ components
│     │  │  ├─ envCenter.vue
│     │  │  ├─ envLeft.vue
│     │  │  ├─ envMap.vue
│     │  │  └─ envRight.vue
│     │  └─ index.vue
│     ├─ information
│     │  ├─ component
│     │  │  ├─ info_left.vue
│     │  │  ├─ info_mid.vue
│     │  │  └─ info_right.vue
│     │  └─ index.vue
│     ├─ intelligent
│     │  ├─ components
│     │  │  ├─ ecoCenter.vue
│     │  │  ├─ ecoLeft.vue
│     │  │  └─ ecoRight.vue
│     │  └─ index.vue
│     └─ underwater
│        ├─ components
│        │  ├─ echarts
│        │  │  └─ heatMapEcharts.vue
│        │  ├─ water_left.vue
│        │  ├─ water_mid.vue
│        │  └─ water_right.vue
│        └─ index.vue
├─ test
│  └─ test.txt
├─ vue.config.js
└─ yarn.lock

```