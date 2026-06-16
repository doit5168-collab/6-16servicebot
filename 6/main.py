import google.generativeai as genai
from google.colab import userdata

api_key = os.getenv'GEMINI_KEY')

genai.configure(api_key=api_key)

# 初始化時就定義好它是誰
ai_persona = "我們是王冠花藝公司專門做客製化花藝全省送貨服務,必須要有送貨地址與花型及數量才能訂製,分為喪禮(高架花籃/蘭花/蓮花塔/米塔)/喜慶/活動用花,卡片內容包含上聯(賀/悼)/中聯('賀詞'or'輓詞自動帶入匹配年齡')/下聯,用引導的方式詢問客戶訂購步驟,最後將資訊統合在一起請客戶確認"
model = genai.GenerativeModel(
#model_name='gemini-2.5-flash',
model_name='gemini-3.1-flash-lite-preview',
system_instruction=ai_persona
)




chat = model.start_chat(history=[])
while True:
  msg = input("你:")
  if msg == "謝謝":
    break
  if msg == "能送花嗎":
    response = chat.send_message("可以的.請問目的地")
  else:
    response = chat.send_message(msg)
  print(f"阿冠:{response.text}")
# 練習:取消下方註解看看記憶長什麼樣子
# print(f"對話筆數: {len(chat.history)}")
