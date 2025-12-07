# YPrompt

AI 透過對話挖掘使用者需求，並自動產生專業的提示詞，支援系統/使用者提示詞最佳化、效果對比、版本管理和支援即時渲染的操練場

## 功能特性

- AI 引導對話挖掘使用者需求後產生專業系統提示詞
- 系統/使用者（支援建構對話上下文）最佳化、效果對比
- 提示詞版本管理與歷史回滾
- 操練場支援多種輸出類型即時渲染，效果看得見
- 雙認證：本地使用者名稱密碼、`Linux.do OAuth`
- 雙資料庫：SQLite（預設）+ MySQL（可選）
- 響應式設計（桌面/行動端）

## 介面

![](imgs/1.gif)
![](imgs/2.gif)
![](imgs/3.gif)
![](imgs/4.gif)
![](imgs/5.gif)
![](imgs/6.gif)
![](imgs/7.gif)
![](imgs/8.gif)
![](imgs/9.gif)
![](imgs/10.gif)
![](imgs/11.gif)
![](imgs/12.gif)
![](imgs/13.gif)
![](imgs/14.gif)
![](imgs/15.gif)

## 系統架構

```
YPrompt/
├── frontend/                  # Vue 3 + TypeScript 前端
│   └── dist/                 # 建置產物
├── backend/                   # Sanic Python 後端
│   ├── apps/                 # 應用程式碼
│   ├── config/               # 配置檔案
│   └── migrations/           # 資料庫腳本
├── data/                      # 資料目錄（持久化）
│   ├── yprompt.db            # SQLite 資料庫
│   ├── cache/                # 快取檔案
│   ├── logs/                 # 日誌檔案
│   │   ├── backend/          # 後端日誌
│   │   └── nginx/            # Nginx 日誌
│   └── ssl/                  # SSL 憑證（可選）
│       ├── fullchain.pem     # 憑證鏈
│       └── privkey.pem       # 私鑰
├── Dockerfile                 # Docker 映像檔
├── docker-compose.yml         # Docker Compose 配置
└── start.sh                   # 容器啟動腳本
```

## 快速啟動

### Docker Run

```bash
docker run -d \
  --name yprompt \
  -p 80:80 \
  -v ./data:/app/data \
  -e DOMAIN=yourdomain.com \
  -e SECRET_KEY=your-random-secret-key \
  -e LINUX_DO_CLIENT_ID=your_client_id \
  -e LINUX_DO_CLIENT_SECRET=your_client_secret \
  -e LINUX_DO_REDIRECT_URI=https://yourdomain.com/auth/callback \
  ghcr.io/fish2018/yprompt:latest
```

### Docker Compose

建立 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  yprompt:
    image: ghcr.io/fish2018/yprompt:latest
    container_name: yprompt
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./data:/app/data
    environment:
      - DOMAIN=yourdomain.com
      - SECRET_KEY=your-random-secret-key
      - LINUX_DO_CLIENT_ID=your_client_id
      - LINUX_DO_CLIENT_SECRET=your_client_secret
      - LINUX_DO_REDIRECT_URI=https://yourdomain.com/auth/callback
```

啟動：

```bash
docker-compose up -d
```

## 環境變數說明

### 必需參數

| 變數 | 說明 | 範例 |
|------|------|------|
| `SECRET_KEY` | JWT 密鑰（至少 32 位隨機字元） | `a1b2c3d4e5f6...` |

### 伺服器配置

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `DOMAIN` | `localhost` | 網域名稱或 IP 位址 |

### 資料庫配置

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `DB_TYPE` | `sqlite` | 資料庫類型：`sqlite` 或 `mysql` |
| `SQLITE_DB_PATH` | `../data/yprompt.db` | SQLite 資料庫檔案路徑 |
| `DB_HOST` | `localhost` | MySQL 主機位址 |
| `DB_USER` | `root` | MySQL 使用者名稱 |
| `DB_PASS` | - | MySQL 密碼 |
| `DB_NAME` | `yprompt` | MySQL 資料庫名稱 |
| `DB_PORT` | `3306` | MySQL 連接埠 |

### `Linux.do OAuth` 配置（可選）

| 變數 | 說明 | 範例 |
|------|------|------|
| `LINUX_DO_CLIENT_ID` | 應用程式 Client ID | `WMYxs1aE2NOdBkj1le...` |
| `LINUX_DO_CLIENT_SECRET` | 應用程式 Client Secret | `QGl30etmvXbLM0d...` |
| `LINUX_DO_REDIRECT_URI` | OAuth 回呼位址 | `https://yourdomain.com/auth/callback` |

申請網址：https://connect.linux.do/my/preferences/apps

### 本地認證配置

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `ADMIN_USERNAME` | `admin` | 預設管理員使用者名稱 |
| `ADMIN_PASSWORD` | `admin123` | 預設管理員密碼 |

### 健康檢查配置

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `HEALTH_CHECK_INTERVAL` | `30` | 健康檢查間隔（秒） |
| `HEALTH_CHECK_TIMEOUT` | `10` | 健康檢查逾時（秒） |
| `HEALTH_CHECK_RETRIES` | `3` | 健康檢查重試次數 |

## HTTPS 配置

將 SSL 憑證放置在資料目錄：

```bash
data/ssl/
├── fullchain.pem    # 完整憑證鏈
└── privkey.pem      # 私鑰
```

容器啟動時會自動偵測並啟用 HTTPS。

## 授權證書

MIT License