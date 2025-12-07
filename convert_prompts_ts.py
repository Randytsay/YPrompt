# -*- coding: utf-8 -*-
"""
prompts.ts 專用轉換腳本
"""

CONVERSION_MAP = {
    # 單字對照
    "独": "獨",
    "规": "規",
    "载": "載",
    "维": "維",
    "护": "護",
    "拆": "拆",
    "获": "獲",
    "终": "終",
    "默": "默",
    "认": "認",
    "质": "質",
    "更": "更",
    "保存": "儲存",
    "修改": "修改",
    "无": "無",
    "跳过": "跳過",
    "标记": "標記",
    "云端": "雲端",
    "失败": "失敗",
    "删除": "刪除",
    "加载": "載入",
    "向后": "向後",
    "兼容": "相容",
    "旧版": "舊版",
    "脏": "髒",
    
    # 詞組對照
    "独立": "獨立",
    "规则": "規則",
    "维护": "維護",
    "目录": "目錄",
    "获取": "獲取",
    "最终": "最終",
    "默认": "預設",
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
    file_path = "d:/Coding/prompt_opti/YPrompt/frontend/src/config/prompts.ts"
    
    print("開始轉換 prompts.ts...")
    if convert_file(file_path):
        print("\n✅ 轉換完成！")
    else:
        print("\n❌ 轉換失敗！")
