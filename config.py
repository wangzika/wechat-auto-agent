# config.py
import os
# from publisher import get_access_token, upload_image_material

# --- DeepSeek API 配置 ---
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1" 
# 替换为你的 DeepSeek 真实 Key
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "api_key") 
DEEPSEEK_MODEL = "deepseek-chat" 

# --- 微信公众号配置 ---
APP_ID = "APP_ID"       
APP_SECRET = "APP_SECRET " 
WECHAT_BASE_URL = "https://api.weixin.qq.com/cgi-bin"

# ⚠️ 必须替换：这是你通过 upload_image_material 函数获取到的封面图 media_id
# 运行 publisher.py 中的测试代码来获取它！
COVER_IMAGE_MEDIA_ID = "img_id"
