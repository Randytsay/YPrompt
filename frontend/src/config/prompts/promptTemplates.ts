// 提示詞模板統一匯出
// 提供對所有獨立提示詞檔案的便捷存取

export * from './thinkingPointsExtraction'
export * from './systemPromptGeneration'
export * from './optimizationAdvice'
export * from './optimizationApplication'

// 為了向後相容，重新匯出原有的結構
export { FINAL_PROMPT_GENERATION_RULES, FINAL_PROMPT_SYSTEM_MESSAGES } from './finalPromptGenerationRules'