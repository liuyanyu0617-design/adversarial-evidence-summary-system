import re

class TextNormalizer:
    def __init__(self):
        # 建立特殊術語與口語對話的模擬字典（僅作技術演示，完全不涉及真實敏感資訊）
        self.slang_dict = {
            "維他命A": "目標物A款",
            "冰糖": "高純度結晶體",
            "拿貨": "進行交易接洽",
            "老地方": "預定交貨地點"
        }

    def clean_text(self, text: str) -> str:
        """去除文本中的特殊雜音字元與前後多餘空格"""
        if not text:
            return ""
        # 將多個空格或換行符號替換為單一空格
        text = re.sub(r'[\s\t\n]+', ' ', text)
        return text.strip()

    def normalize_slang(self, text: str) -> str:
        """將模擬的口語詞彙替換為標準結構化分析術語"""
        normalized = text
        for slang, standard in self.slang_dict.items():
            normalized = normalized.replace(slang, f"{slang}(編譯註解: {standard})")
        return normalized

    def process(self, text: str) -> str:
        """主處理流程：先清洗文本，再進行術語正規化"""
        cleaned = self.clean_text(text)
        return self.normalize_slang(cleaned)

if __name__ == "__main__":
    # 本地測試程式碼
    normalizer = TextNormalizer()
    test_text = "  今天在 老地方 拿貨，順便帶點 冰糖 。  "
    print("【原始對話文本】:", test_text)
    print("【正規化後文本】:", normalizer.process(test_text))
