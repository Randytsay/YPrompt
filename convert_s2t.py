# -*- coding: utf-8 -*-
"""
簡體轉繁體批次轉換腳本
用於轉換 YPrompt prompt 配置檔案
"""

# 簡繁對照表（常用術語）
CONVERSION_MAP = {
    # 使用者相關
    "用户": "使用者",
    "用於": "用於",
    
    # 系統相關
    "系统": "系統",
    "优化": "最佳化",
    "生成": "產生",
    "项目": "專案",
    "质量": "品質",
    "建议": "建議",
    "规则": "規則",
    "示例": "範例",
    "场景": "場景",
    "对话": "對話",
    "信息": "資訊",
    "程序": "程式",
    "代码": "程式碼",
    "配置": "配置",
    "导出": "匯出",
    "导入": "匯入",
    "统一": "統一",
    "默认": "預設",
    "变量": "變數",
    "函数": "函式",
    
    # 動詞
    "发现": "發現",
    "强调": "強調",
    "实践": "實踐",
    "扮演": "扮演",
    "续写": "續寫",
    "擅长": "擅長",
    "帮你": "幫你",
    "给出": "給出",
    "发给": "發給",
    "进行": "進行",
    "提供": "提供",
    "确保": "確保",
    "包含": "包含",
    "缺少": "缺少",
    "补充": "補充",
    "符合": "符合",
    
    # 形容詞
    "详细": "詳細",
    "简洁": "簡潔",
    "专业": "專業",
    "清晰": "清晰",
    "具体": "具體",
    "笼统": "籠統",
    "连贯": "連貫",
    "简略": "簡略",
    "错误": "錯誤",
    "正确": "正確",
    
    # 名詞
    "背景": "背景",
    "层次": "層次",
    "歧义": "歧義",
    "细节": "細節",
    "逻辑": "邏輯",
    "组织": "組織",
    "受众": "受眾",
    "格式": "格式",
    "标准": "標準",
    "评分": "評分",
    "维度": "維度",
    "草稿": "草稿",
    "诊断": "診斷",
    "患者": "患者",
    "医生": "醫生",
    "翻译": "翻譯",
    "文案": "文案",
    "营销": "行銷",
    "产品": "產品",
    "标题": "標題",
    "卖点": "賣點",
    "内容": "內容",
    "语言": "語言",
    "任务": "任務",
    "输出": "輸出",
    "输入": "輸入",
    "限制": "限制",
    "约束": "約束",
    "条件": "條件",
    "要求": "要求",
    "必须": "必須",
    "禁止": "禁止",
    "绝对": "絕對",
    "警告": "警告",
    "关键": "關鍵",
    "角色": "角色",
    "身份": "身分",
    "助手": "助手",
    "消息": "訊息",
    "表达": "表達",
    "历史": "歷史",
    "原因": "原因",
    "结构": "結構",
    "文档": "文件",
    "技术": "技術",
    "意图": "意圖",
    "语气": "語氣",
    "措辞": "措辭",
    "检查": "檢查",
    "清单": "清單",
    "扩展": "擴展",
    "比例": "比例",
    "阈值": "閾值",
    "模糊": "模糊",
    "实际": "實際",
    "标记": "標記",
    "章节": "章節",
    "控制": "控制",
    "长度": "長度",
    "相对": "相對",
    "字数": "字數",
    "文本": "文字",
    "风格": "風格",
    "活泼": "活潑",
    "促销": "促銷",
    "特点": "特點",
    "价格": "價格",
    "优势": "優勢",
    "总结": "總結",
    "决策": "決策",
    "待办": "待辦",
    "事项": "事項",
    "要点": "要點",
    "准确": "準確",
    "流畅": "流暢",
    "地道": "地道",
    "语境": "語境",
    "目标": "目標",
    "策略": "策略",
    
    # 標點符號和標記（保持原樣）
    "【": "【",
    "】": "】",
    "《": "《",
    "》": "》",
}

def convert_s2t(text):
    """簡體轉繁體"""
    for s, t in CONVERSION_MAP.items():
        text = text.replace(s, t)
    return text

def convert_file(input_path, output_path=None):
    """轉換單個檔案"""
    if output_path is None:
        output_path = input_path
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        converted = convert_s2t(content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted)
        
        print(f"✅ 已轉換: {input_path}")
        return True
    except Exception as e:
        print(f"❌ 轉換失敗 {input_path}: {e}")
        return False

if __name__ == "__main__":
    # 要轉換的檔案列表
    files_to_convert = [
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/userPromptOptimization.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/promptOptimization.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/qualityAnalysis.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/userGuidedRules.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/systemPromptSlimRules.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/systemPromptRules.ts",
    ]
    
    print("開始批次轉換...")
    success_count = 0
    for file_path in files_to_convert:
        if convert_file(file_path):
            success_count += 1
    
    print(f"\n完成！成功轉換 {success_count}/{len(files_to_convert)} 個檔案")
