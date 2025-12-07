// 提示詞規則統一匯出
// 從各個獨立檔案中匯入並匯出所有提示詞規則

import { SYSTEM_PROMPT_RULES } from './systemPromptRules'
import { SYSTEM_PROMPT_SLIM_RULES } from './systemPromptSlimRules'
import { USER_GUIDED_PROMPT_RULES } from './userGuidedRules'
import { REQUIREMENT_REPORT_RULES } from './requirementReportRules'
import { FINAL_PROMPT_GENERATION_RULES, FINAL_PROMPT_SYSTEM_MESSAGES } from './finalPromptGenerationRules'
import { PROMPT_OPTIMIZATION_CONFIG } from './promptOptimization'

// 匯出所有提示詞規則
export {
  SYSTEM_PROMPT_RULES,
  SYSTEM_PROMPT_SLIM_RULES,
  USER_GUIDED_PROMPT_RULES,
  REQUIREMENT_REPORT_RULES,
  FINAL_PROMPT_GENERATION_RULES,
  FINAL_PROMPT_SYSTEM_MESSAGES,
  PROMPT_OPTIMIZATION_CONFIG
}