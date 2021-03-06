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

### mosquitto.conf 參數說明

設定檔設置於        /etc/mosquitto/mosquitto.conf

詳細的參數說明如下：

        # ================================================= ================
        # General configuration
        # ================================================= ================
  
        # 客戶端心跳的間隔時間
        #retry_interval 20
  
        # 系統狀態的刷新時間
        #sys_interval 10
  
        # 系統資源的回收時間，0表示盡快處理
        #store_clean_interval 10
  
        # 服務進程的PID
        #pid_file /var/run/mosquitto.pid
  
        # 服務進程的系統用戶
        #user mosquitto
  
        # 客戶端心跳消息的最大並發數
        #max_inflight_messages 10
          
        # 客戶端心跳消息緩存隊列
        #max_queued_messages 100
  
        # 用於設置客戶端長連接的過期時間，默認永不過期
        #persistent_client_expiration
  
        # ================================================= ================
        # Default listener
        # ================================================= ================
  
        # 服務綁定的IP地址
        #bind_address
  
        # 服務綁定的端口號
        #port 1883
  
        # 允許的最大連接數，-1表示沒有限制
        #max_connections -1
  
        # cafile：CA證書文件
        # capath：CA證書目錄
        # certfile：PEM證書文件
        # keyfile：PEM密鑰文件
        #cafile
        #capath
        #certfile
        #keyfile
  
        # 必須提供證書以保證數據安全性
        #require_certificate false
  
        # 若require_certificate值為true，use_identity_as_username也必須為true
        #use_identity_as_username false
  
        # 啟用PSK（Pre-shared-key）支持
        #psk_hint
  
        # SSL/TSL加密算法，可以使用“openssl ciphers”命令獲取
        # as the output of that command.
        #ciphers
  
        # ================================================= ================
        # Persistence
        # ================================================= ================
  
        # 消息自動保存的間隔時間
        #autosave_interval 1800
  
        # 消息自動保存功能的開關
        #autosave_on_changes false
  
        # 持久化功能的開關
        persistence true
  
        # 持久化DB文件
        #persistence_file mosquitto.db
  
        # 持久化DB文件目錄
        #persistence_location /var/lib/mosquitto/
          
        # ================================================= ================
        # Logging
        # ================================================= ================
          
        # 4種日誌模式：stdout、stderr、syslog、topic
        # none 則表示不記日誌，此配置可以提升些許性能
        log_dest none
  
        # 選擇日誌的級別（可設置多項）
        #log_type error
        #log_type warning
        #log_type notice
        #log_type information
  
        # 是否記錄客戶端連接信息
        #connection_messages true
  
        # 是否記錄日誌時間
        #log_timestamp true
  
        # ================================================= ================
        # Security
        # ================================================= ================
          
        # 客戶端ID的前綴限制，可用於保證安全性
        #clientid_prefixes
  
        # 允許匿名用戶
        #allow_anonymous true
  
        # 用戶/密碼文件，默認格式：username:password
        #password_file
  
        # PSK格式密碼文件，默認格式：identity:key
        #psk_file
          
        # pattern write sensor/%u/data
        # ACL權限配置，常用語法如下：
        # 用戶限制：user <username>
        # 話題限制：topic [read|write] <topic>
        # 正則限制：pattern write sensor/%u/data
        #acl_file
          
        # ================================================= ================
        # Bridges
        # ================================================= ================
          
        # 允許服務之間使用“橋接”模式（可用於分佈式部署）
        #connection <name>
        #address <host>[:<port>]
        #topic <topic> [[[out | in | both] qos-level] local-prefix remote-prefix]
  
        # 設置橋接的客戶端ID
        #clientid
  
        # 橋接斷開時，是否清除遠程服務器中的消息
        #cleansession false
  
        # 是否發布橋接的狀態信息
        #notifications true
  
        # 設置橋接模式下，消息將會發佈到的話題地址
        # $SYS/broker/connection/<clientid>/state
        #notification_topic
  
        # 設置橋接的keepalive數值
        #keepalive_interval 60
  
        # 橋接模式，目前有三種：automatic、lazy、once
        #start_type automatic
  
        # 橋接模式automatic的超時時間
        #restart_timeout 30
  
        # 橋接模式lazy的超時時間
        #idle_timeout 60
  
        # 橋接客戶端的用戶名
        #username
  
        # 橋接客戶端的密碼
        #password
        # bridge_cafile：橋接客戶端的CA證書文件
        # bridge_capath：橋接客戶端的CA證書目錄
        # bridge_certfile：橋接客戶端的PEM證書文件
        # bridge_keyfile：橋接客戶端的PEM密鑰文件
        #bridge_cafile
        #bridge_capath
        #bridge_certfile
        #bridge_keyfile
  
        # 自己的配置可以放到以下目錄中
        include_dir /etc/mosquitto/conf.d
參考來源 :

Mosquitto簡要教程（安裝/使用/測試）
Tutorial: IOT / Installing and Testing Mosquitto MQTT on the Raspberry Pi
認證方式

Broker的認證方式，Mosquitto端提供了四種認證方法分別為

無認證
帳號/密碼
預先共享密鑰(Pre-shared Key)加密
憑證加密
