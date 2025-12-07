# AGENTS 總覽

YPrompt 是一個雙端協同的提示詞管理系統：前端採用 Vue 3 + Pinia + Tailwind 建構響應式 UI，後端由 Sanic 提供基於 SQLite/MySQL 的 API 服務，並支援 Linux.do OAuth 與本地認證。此文件定義了各角色 Agent 的工作範圍、關鍵入口以及協作方式，便於後續二次開發快速分工。

## 專案快照
- **目錄結構**：`frontend/` 承載 Vue 應用（模組化元件 + composables）；`backend/` 承載 Sanic 應用（apps/modules/* 藍圖自動註冊）；`data/` 保存 SQLite、日誌與快取。
- **執行鏈路**：瀏覽器命中 `frontend/src/main.ts` 配置的路由和守衛，認證後透過 `frontend/src/services/apiService.ts` 呼叫後端 REST 介面，後端在 `backend/apps/__init__.py` 中初始化資料庫/JWT/藍圖並暴露 `/api/**`。
- **核心功能**：AI 引導產生、提示詞最佳化、個人庫與版本管理、雙認證、雙資料庫、響應式佈局。

## Agent 分工

### 前端 Agent
- **職責**：
  - 維護路由、佈局與模組頁面（Generate/Optimize/Playground/Library），位於 `frontend/src/main.ts` 與 `frontend/src/components/modules/`。
  - 維護 Pinia stores（認證、提示詞、導航、設定、最佳化等），確保狀態與 API 契約一致，入口 `frontend/src/stores/`。
  - 擴展 AI 服務、Provider、串流解析，集中在 `frontend/src/services/ai/` 及 `aiService.ts`。
  - 管理提示詞配置與規則（`frontend/src/config/prompts.ts` 及其子目錄），同步雲端/本地版本。
- **關鍵工作流**：
  1. 認證：`authStore` 負責 Linux.do OAuth code 登入、本地使用者名稱密碼登入、token 更新、使用者復原。
  2. API：`apiService.ts` 統一封裝 fetch，自動附帶 token 與錯誤處理；模組服務（如 `versionService.ts`）基於它實作業務。
  3. 模組：GenerateModule 整合聊天、預覽面板；OptimizeModule 負責系統/使用者提示詞的品質檢測；LibraryModule 提供清單、版本、收藏、標籤等視圖。
- **常用命令**：`npm install`、`npm run dev`、`npm run build`、`npm run type-check`。

### 後端 Agent
- **職責**：
  - 維護 Sanic 應用程式生命週期（`backend/apps/__init__.py`），包括日誌、CORS、JWT、資料庫、藍圖自動註冊。
  - 編寫/維護業務模組（`backend/apps/modules/*`），每個模組包含 `models.py`（OpenAPI 模型）、`services.py`、`views.py`。
  - 維護工具層（`backend/apps/utils/`）：資料庫適配器、JWT、OAuth、密碼工具、認證中介軟體等。
  - 保障配置（`backend/config/*.py`）與遷移腳本（`backend/migrations/*.sql`）正確，涵蓋 SQLite 自動初始化、管理員同步、MySQL 配置。
- **核心能力點**：
  1. **雙資料庫**：`db_utils.py` + `db_adapter.py` 統一介面，SQLite 首次啟動自動建庫並建立/同步 admin 帳號；MySQL 透過 ezmysql 連線池。
  2. **雙認證**：`apps/modules/auth/views.py` 同時提供 Linux.do OAuth `/api/auth/linux-do/login` 與本地 `/api/auth/local/login`/`register` 入口；`LinuxDoOAuth` & `PasswordUtil` & `JWTUtil` 提供支援。
  3. **提示詞/版本/標籤** 模組提供 REST API（`/api/prompts`, `/api/versions`, `/api/tags`）；`prompt_rules` 模組負責系統內建規則管理。
- **常用命令**：`python3 -m venv venv && source venv/bin/activate`、`pip install -r requirements.txt`、`python run.py`（可加 `--workers=4`）。

### 協調/整合 Agent
- **職責**：
  - 定義前後端契約，確保 `apiService` 中的請求與後端回傳的資料結構一致，如 `/api/prompts` 清單回傳 `total/page/limit/items`。
  - 管理配置與部署：對接 `.env` / `config/base.py` / `config/settings.py`，保證環境變數（資料庫、JWT、OAuth、預設管理員）在兩個端正確暴露。
  - 監控資料目錄（`data/yprompt.db`, `data/logs/**`），統一備份策略，並在多環境之間同步遷移腳本。
  - 推動測試/驗證：組織前端 E2E、後端 API/單元測試、介面對齊檢查。

## 協作基線
- **API 契約**：遵循 `/api/*` REST 設計，成功回傳 `{'code':200,'data':...}`，失敗回傳 `{'code':xxx,'message':...}`；前端遇到 `401` 時需清理本地憑證並重新導向登入。
- **認證鏈路**：前端透過 `/api/auth/config` 取得可用認證方式；Linux.do 回呼頁面負責提取 `code` 並呼叫 `/api/auth/linux-do/login`；本地模式透過 `/api/auth/local/login` 與 `/register` 完成。
- **資料一致性**：提示詞與版本模組需要維護 `current_version`、`total_versions`、版本快照，前端 Library/Version 面板依賴這些欄位；標籤模組依賴 `tags` 欄位的逗號分隔格式。
- **配置安全**：永遠不要提交真實金鑰到 repo；本地除錯使用 `.env.local` / `builtin-providers.json`；生產環境透過環境變數覆蓋 `SECRET_KEY`、資料庫、OAuth、管理員密碼。

## 快速啟動備忘
1. **前端**：在 `frontend/` 執行 `npm install && npm run dev`，確保 `.env.local` 中的 `VITE_API_BASE_URL` 指向執行中的後端；必要時複製 `builtin-providers.example.json`。
2. **後端**：在 `backend/` 中安裝依賴並執行 `python run.py`；預設使用 `../data/yprompt.db`，首次啟動會自動建立表結構與管理員帳號；需要 MySQL 時在 `config/base.py` 或環境變數中切換。
3. **聯調**：保證瀏覽器可存取 `http://localhost:5173`，後端預設 `http://localhost:8888`；Swagger 文件在 `/docs`，OpenAPI JSON 在 `/openapi.json`。

## 後續開發提示
- 規劃中的模組（如 Playground 擴展、多模型對比）已在目錄中占位，可由前端 Agent 接手實作 UI + 呼叫；後端 Agent 需要配套 API。
- MySQL 初始化腳本仍需補充/驗證，若啟用 MySQL 需先編寫/執行遷移。
- 考慮在後續迭代中加入信箱驗證、二次驗證、權限系統、Redis 快取及資料備份機制。

> 使用本文件快速定位職責、入口和啟動方式，確保多 Agent 協作時對系統整體有一致的 mental model。
