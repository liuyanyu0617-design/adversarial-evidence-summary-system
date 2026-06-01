import os
from openai import OpenAI

class TextAnalyzerAgent:
    def __init__(self, api_key: str = None):
        # 優先從環境變數讀取 API 金鑰，嚴格禁止寫死在程式碼中，確保安全性
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4"

    def analyze_dialogue(self, normalized_text: str) -> str:
        """利用大語言模型與智慧代理架構分析對話內容並提取關鍵事實"""
        
        # 設計嚴格的 System Prompt，要求模型必須輸出特定結構的 JSON 格式
        system_prompt = (
            "You are an expert digital forensics text analytics agent. Your task is to extract "
            "factual event chains from the provided normalized dialogue text.\n"
            "You must structure your response with the following JSON format strictly:\n"
            "{\n"
            "  'event_detected': true/false,\n"
            "  'key_entities': ['entity1', 'entity2'],\n"
            "  'chronological_facts': ['fact1', 'fact2'],\n"
            "  'risk_assessment': 'high/medium/low'\n"
            "}\n"
            "Ensure no personal identifiable information (PII) is outputted. Focus entirely on timeline extraction."
        )

        try:
            # 呼叫 OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze this text: {normalized_text}"}
                ],
                temperature=0.2 # 降低隨機性，確保事實抽取的嚴謹與客觀性
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"{{'error': '{str(e)}'}}"

if __name__ == "__main__":
    # 本地測試模擬
    agent = TextAnalyzerAgent(api_key="mock-key-for-testing")
    sample_input = "Subject Alpha(編譯註解: 目標物A款) confirmed arrival at Location Delta."
    print("【AI Agent 預期分析流程啟動】")
    print("輸入文本:", sample_input)
    # 註：此處若無設定真實 API Key 執行時會進入 except 區塊輸出 error，此為正常防禦機制
