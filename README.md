## Linux

安裝指令
1. wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
2. apt-key add mosquitto-repo.gpg.key
3. cd /etc/apt/sources.list.d/
4. sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list
5. sudo apt-get update
6. sudo apt-get install mosquitto
7. service mosquitto status （檢查mosquitto服務狀態）
8. netstat -tln （檢查port 1883）

## MacOS

安裝指令

Use Homebrew install
1. ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
2. brew install mosquitto
3. ln -sfv /usr/local/opt/mosquitto/*.plist ~/Library/LaunchAgents
4. launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mosquitto.plist
5. launchctl start homebrew.mxcl.mosquitto

### 測試

1. mosquitto_sub -t topic/state
2. 產生訂閱者 mosquitto_sub -d -t hello/world
3. 發佈者角色 mosquitto_pub -d -t hello/world -m "Hi, This test message."

測試工具（http://www.jensd.de/apps/mqttfx/）
