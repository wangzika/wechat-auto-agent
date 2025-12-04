# get_media_id_tool.py (修改调用函数)
import os
# 确保从 publisher 导入了新的函数
from publisher import get_access_token, upload_permanent_image_material 

# 确保你的图片路径正确
IMAGE_FILE_PATH = "/Users/wangzhibo/mycode/WuTa_2019-07-04_12-22-59_1.jpg" # 建议用新的图片文件

def run_media_id_acquisition():
    print("--- 启动【永久】封面图 Media ID 获取工具 ---")
    
    token = get_access_token()
    if not token:
        print("❌ 无法获取 Access Token，请检查 IP 白名单和 AppID/AppSecret。")
        return

    if not os.path.exists(IMAGE_FILE_PATH):
        print(f"❌ 错误：未找到图片文件：{IMAGE_FILE_PATH}。请检查文件是否存在。")
        return
        
    # 🌟 调用新的永久素材上传函数
    cover_media_id = upload_permanent_image_material(token, IMAGE_FILE_PATH)
    
    if cover_media_id:
        print("\n=======================================================")
        print("🎉 恭喜！永久封面图上传成功！")
        print(f"🔑 请将以下 ID 复制并粘贴到 config.py 中：\n\n{cover_media_id}\n")
        print("=======================================================")
        
    else:
        print("❌ 永久素材上传失败，请检查公众号素材数量限制或图片是否合格。")

if __name__ == '__main__':
    run_media_id_acquisition()