/**
 * 提示詞產生器模块配置
 * 便於将来封装為独立子模块或集成到更大的项目中
 */

export interface PromptGeneratorConfig {
  // 欢迎消息配置
  welcomeMessage: string
  
  // 快速回复选项
  quickReplies: string[]
  
  // 對话设置
  maxConversationTurns: number
  typingDelay: number
}

// 默認配置
export const DEFAULT_PROMPT_GENERATOR_CONFIG: PromptGeneratorConfig = {
  welcomeMessage: "您好！我是提示詞工程專家，将通過几個问题帮您构建一個高品質的AI提示詞。請先告诉我：您希望用AI来解决什么问题或完成什么任务？",
  
  quickReplies: [
    '請使用相关最佳实践的推荐建议',
    '強制產生需求报告'
  ],
  
  maxConversationTurns: 5,
  typingDelay: 50
}

// 模块标识符
export const MODULE_INFO = {
  name: 'PromptGenerator',
  version: '1.0.0',
  description: '智能提示詞產生器',
  author: 'YPrompt Team'
}

// 導出配置獲取函数，便於将来扩展自定义配置
export function getPromptGeneratorConfig(customConfig?: Partial<PromptGeneratorConfig>): PromptGeneratorConfig {
  return {
    ...DEFAULT_PROMPT_GENERATOR_CONFIG,
    ...customConfig
  }
}
