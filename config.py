# config.py
import os
# from publisher import get_access_token, upload_image_material

# --- DeepSeek API 配置 ---
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1" 
# 替换为你的 DeepSeek 真实 Key
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-eeadd97971ef4880a814477be5940d42") 
DEEPSEEK_MODEL = "deepseek-chat" 

# --- 微信公众号配置 ---
APP_ID = "wxb62e154940c3c7c3"       
APP_SECRET = "3641e31cd77fa5a7628d1abf01a88fa1" 
WECHAT_BASE_URL = "https://api.weixin.qq.com/cgi-bin"

# ⚠️ 必须替换：这是你通过 upload_image_material 函数获取到的封面图 media_id
# 运行 publisher.py 中的测试代码来获取它！
COVER_IMAGE_MEDIA_ID = "OzDw82ZGuV7j2GWA35lmho6uGNCEMrxQoR57yGZtp9RlC9ZxoN_ZlQ55cQAAL_ug"