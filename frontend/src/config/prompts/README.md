# 提示詞配置檔案說明

## 檔案結構

```
src/config/prompts/
├── index.ts                  # 統一匯出檔案
├── systemPromptRules.ts      # 系統提示詞規則
└── userGuidedRules.ts        # 使用者引導規則
```

## 檔案說明

### index.ts
- 統一匯出所有提示詞規則
- 作為其他模組匯入的入口點

### systemPromptRules.ts
- 包含完整的精英提示詞工程指南
- 基於《Architecting Intelligence》的系統提示詞規則
- 匯出 `SYSTEM_PROMPT_RULES` 常數

### userGuidedRules.ts  
- AI 需求收集助手的提示詞規則
- 用於引導使用者有效描述 AI 自動化需求
- 包含輸入驗證和對話控制邏輯
- 匯出 `USER_GUIDED_PROMPT_RULES` 常數

## 擴展指南

### 新增新的 AI 助手類型

1. 在 `prompts/` 目錄下建立新的規則檔案，例如 `codeReviewRules.ts`
2. 匯出相應的常數，例如 `CODE_REVIEW_PROMPT_RULES`
3. 在 `index.ts` 中新增匯出

範例：

```typescript
// prompts/codeReviewRules.ts
export const CODE_REVIEW_PROMPT_RULES = `你是一個專業的程式碼審查助手...`

// prompts/index.ts
import { CODE_REVIEW_PROMPT_RULES } from './codeReviewRules'

export {
  SYSTEM_PROMPT_RULES,
  USER_GUIDED_PROMPT_RULES,
  CODE_REVIEW_PROMPT_RULES 
}
```

### 修改現有規則

1. 直接編輯對應的規則檔案
2. 儲存後會自動套用到系統中
3. 使用者在設定介面中的自訂會覆蓋預設值

## 命名規範

- 所有常數使用 `UPPER_SNAKE_CASE` 命名
- 檔案名稱使用 `camelCase` 命名，以 `Rules.ts` 結尾
- 匯出的常數名稱應該以 `_RULES` 結尾，例如：
  - `SYSTEM_PROMPT_RULES`
  - `USER_GUIDED_PROMPT_RULES`
  - `CODE_REVIEW_PROMPT_RULES`