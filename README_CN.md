# MinecraftServerPage 我的世界服务器页面
[English](https://github.com/xiaofan3p/MinecraftServerPage/blob/master/README.md) | Chinese

MinecraftServerPages 是基于 [mcstatus](https://github.com/Dinnerbone/mcstatus) 库与 Django 构建的网页应用，他可以通过生成图片的方式展示你的服务器状态。
# 安装
你需要安装 Python3 以上版本，然后下载或克隆本项目，之后使用如下指令安装依赖库。
```
pip install -r requirements.txt
```
之后打开 START.BAT 本项目就正式开始运行，你可以在以下网址看见生成的动态图片：
```
http://{YOUR SERVER DOWMIANNAME}/stats.php?ip={YOUR IP ADDRESS}&title={YOUR SERVER NAME}&motd={A DESCRIPTION}
```
如果你服务器的端口为25565，那么你不需要在网址后面添加端口，如：  example.com  / exmaple.com:2333.
# 依赖库
```
mcstatus==4.0.0
Django==3.0.6
Pillow==7.2.0
```
# 协议
Apache 2.0. 

[![avatar](https://camo.githubusercontent.com/a72e7743f15db219a6aba534f9de456e86268dd6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d416e74692532303939362d626c75652e7376673f7374796c653d666c61742d737175617265)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
