# get_media_id_tool.py
import os
from publisher import get_access_token, upload_image_material

# ⚠️ 确保你的图片路径正确
IMAGE_FILE_PATH = "/Users/wangzhibo/mycode/WuTa_2019-07-04_12-22-59_1.jpg" 

def run_media_id_acquisition():
    print("--- 启动封面图 Media ID 获取工具 ---")
    
    # 1. 获取 Access Token (前提是 IP 白名单已解决)
    token = get_access_token()
    
    if not token:
        print("❌ 无法获取 Access Token，请检查 IP 白名单和 AppID/AppSecret。")
        return

    # 2. 上传图片并获取 Media ID
    if not os.path.exists(IMAGE_FILE_PATH):
        print(f"❌ 错误：未找到图片文件：{IMAGE_FILE_PATH}。请检查文件是否存在。")
        return
        
    cover_media_id = upload_image_material(token, IMAGE_FILE_PATH)
    
    if cover_media_id:
        print("\n=======================================================")
        print("🎉 恭喜！封面图上传成功！")
        print(f"🔑 请将以下 ID 复制并粘贴到 config.py 中：\n\n{cover_media_id}\n")
        print("=======================================================")
        
    else:
        print("❌ 图片上传失败，请检查图片格式和大小是否符合微信要求（JPG，小于 2MB）。")

if __name__ == '__main__':
    run_media_id_acquisition()