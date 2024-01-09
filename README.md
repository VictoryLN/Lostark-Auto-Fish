# LostArk Auto Fish-命运方舟自动钓鱼/自动小游戏/自动工会任务

部分代码来自[LostArkFishingBot](https://github.com/DamienShahan/LostArkFishingBot). 在此之上补充了撒网小游戏和提交工会钓鱼任务

## 功能

- 自动钓鱼
- 自动撒网小游戏（有概率失败）
- 自动修理（需要贝拉的祝福）
- 自动接受与提交工会钓鱼任务

## 使用前提

**重要: 只能工作在1920x1080的窗口化环境中**

需要：

- python3.7+，
- pyautogui
- opencv-python
- PIL
- yaml

## 使用方法

1. 到贝隆南钓鱼点
2. 接受所有工会任务
3. 切换玩家比较少的线路（人多了干扰判断）
4. 按B切换到生活技能
5. 折叠聊天框，左上角事件活动框。最好设置事件不提醒。
6. 运行 `python main.py`
7. 5秒内切换到游戏窗口

## 配置

配置相关都在resources/config.yaml文件中，钓鱼默认e键，撒网默认d键，委托默认alt+j，宠物默认alt+p。

图片资源都在resources/1080中

## Reference

DamienShahan, https://github.com/DamienShahan/LostArkFishingBot

Minish144, https://github.com/Minish144/lost-ark-fishing-bot
