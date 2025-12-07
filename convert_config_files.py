# -*- coding: utf8 -*-
"""
Config 檔案簡繁轉換腳本
"""

# 簡繁對照表
CONVERSION_MAP = {
    # 單字
    "专": "專",
    "简": "簡",
    "为": "為",
    "于": "於",
    "评":"評",
    "严": "嚴",
    "对": "對",
    "与": "與",
    "个": "個",
    "过": "過",
    "内": "內",
    "获": "獲",
    "编": "編",
    "这": "這",
    "响": "響",
    "强": "強",
    "删": "刪",
    "提示词": "提示詞",
    "专家": "專家",
    "质量": "品質",
    "生成": "產生",
    "优化": "最佳化",
    "认": "認",
    "请": "請",
    "数据": "資料",
    "响应": "回應",
    "图": "圖",
    "导": "導",
    "长": "長",
    "删除": "刪除",
}

def convert_s2t(text):
    """簡體轉繁體"""
    for s, t in CONVERSION_MAP.items():
        text = text.replace(s, t)
    return text

def convert_file(input_path):
    """轉換單個檔案"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        converted = convert_s2t(content)
        
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(converted)
        
        print(f"✅ 已轉換: {input_path}")
        return True
    except Exception as e:
        print(f"❌ 轉換失敗 {input_path}: {e}")
        return False

if __name__ == "__main__":
    files = [
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/builtinProviders.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/playgroundInstructions.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/promptGenerator.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/qualityAnalysis.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/userGuidedRules.ts",
        "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts/userPromptOptimization.ts",
    ]
    
    print("開始轉換 config 檔案...")
    success = 0
    for f in files:
        if convert_file(f):
            success += 1
    
    print(f"\n完成！成功 {success}/{len(files)} 個")
