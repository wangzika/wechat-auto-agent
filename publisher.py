# publisher.py
import requests
import json
import time
import os
from config import APP_ID, APP_SECRET, WECHAT_BASE_URL, COVER_IMAGE_MEDIA_ID

def get_access_token() -> str | None:
    """获取微信公众号的 Access Token。"""
    token_url = f"{WECHAT_BASE_URL}/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    
    try:
        response = requests.get(token_url)
        response.raise_for_status() 
        data = response.json()
        
        if 'access_token' in data:
            return data['access_token']
        else:
            print(f"-> Access Token 获取失败: {data.get('errmsg', '未知错误')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"-> 请求 Access Token 失败: {e}")
        return None

# publisher.py (新增函数)

def upload_permanent_image_material(access_token: str, image_path: str) -> str | None:
    """
    上传图片作为永久素材，并返回 media_id。
    永久素材 ID 永不过期，更稳定。
    """
    # 接口地址：/cgi-bin/material/add_material
    upload_url = f"{WECHAT_BASE_URL}/material/add_material?access_token={access_token}&type=image"
    
    try:
        with open(image_path, 'rb') as f:
            files = {
                'media': (os.path.basename(image_path), f, 'image/jpeg')
            }
            
            print(f"-> 正在尝试上传永久封面图: {image_path}...")
            
            response = requests.post(upload_url, files=files)
            response.raise_for_status()
            data = response.json()
            
            if 'media_id' in data:
                print(f"-> 永久封面图上传成功，Media ID: {data['media_id']}")
                return data['media_id']
            else:
                print(f"-> 永久封面图上传失败: {data.get('errmsg', '未知错误')}")
                # 微信可能返回：errcode:40001 (access_token invalid) 或 45001 (文件太大)
                return None
                
    except requests.exceptions.RequestException as e:
        print(f"-> 请求上传永久图片失败: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ 错误：未找到图片文件：{image_path}")
        return None

# publisher.py

def upload_material(access_token: str, title: str, html_content: str) -> str | None:
    """将图文内容上传到微信服务器，获取媒体 ID (media_id)。"""
    upload_url = f"{WECHAT_BASE_URL}/draft/add?access_token={access_token}"

    if COVER_IMAGE_MEDIA_ID == "YOUR_OBTAINED_COVER_IMAGE_MEDIA_ID":
        print("⚠️ 警告：请先上传封面图并替换 config.py 中的 COVER_IMAGE_MEDIA_ID！")
        return None

    article_data = {
        "articles": [
            {
                "title": title,
                "content": html_content,
                "author": "AI Agent", 
                "digest": title, 
                "thumb_media_id": COVER_IMAGE_MEDIA_ID, 
                "show_cover_pic": 1, 
            }
        ]
    }
    
    print(f"-> 正在尝试上传文章草稿：【{title}】...")
    
    # 🌟 关键修改：手动将 Python 字典转换为 JSON 字符串，并禁用 ASCII 编码
    # 1. 导入 json 库（如果之前没有导入，需要在文件顶部添加 `import json`）
    json_payload = json.dumps(article_data, ensure_ascii=False).encode('utf-8')
    
    try:
        # 2. 改用 data= 参数传递字节流，并设置 Content-Type 头部
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        
        # 将 json=article_data 替换为 data=json_payload, headers=headers
        response = requests.post(upload_url, data=json_payload, headers=headers)
        
        response.raise_for_status()
        data = response.json()
        if 'media_id' in data:
            return data['media_id']
        else:
            print(f"-> 文章草稿上传失败: {data.get('errmsg', '未知错误')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"-> 上传文章失败: {e}")
        return None

# def upload_material(access_token: str, title: str, html_content: str) -> str | None:
#     """将图文内容上传到微信服务器，获取媒体 ID (media_id)。"""
#     upload_url = f"{WECHAT_BASE_URL}/draft/add?access_token={access_token}"

#     if COVER_IMAGE_MEDIA_ID == "YOUR_OBTAINED_COVER_IMAGE_MEDIA_ID":
#         print("⚠️ 警告：请先上传封面图并替换 config.py 中的 COVER_IMAGE_MEDIA_ID！")
#         return None

#     article_data = {
#         "articles": [
#             {
#                 "title": title,
#                 "content": html_content,
#                 "author": "AI Agent", 
#                 "digest": title, 
#                 "thumb_media_id": COVER_IMAGE_MEDIA_ID, # 使用 config 中的 ID
#                 "show_cover_pic": 1, 
#             }
#         ]
#     }
    
#     print(f"-> 正在尝试上传文章草稿：【{title}】...")
        
#     try:
#         response = requests.post(upload_url, json=article_data)
#         response.raise_for_status()
#         data = response.json()

#         if 'media_id' in data:
#             return data['media_id']
#         else:
#             print(f"-> 文章草稿上传失败: {data.get('errmsg', '未知错误')}")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"-> 上传文章失败: {e}")
#         return None

def send_article(access_token: str, media_id: str) -> bool:
    """通过群发接口将文章发布给所有用户。"""
    send_url = f"{WECHAT_BASE_URL}/freepublish/submit?access_token={access_token}"
    
    payload = {
        "media_id": media_id,
        "send_ignore_reprint": 1 
    }
    
    print(f"-> 正在尝试群发文章，Media ID: {media_id}...")

    try:
        response = requests.post(send_url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if data.get('errcode') == 0:
            print("🎉🎉🎉 文章已提交发布！请稍后查看公众号后台确认状态。")
            return True
        else:
            print(f"-> 文章群发失败: {data.get('errmsg', '未知错误')}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"-> 群发请求失败: {e}")
        return False

# --- 辅助函数：上传图片（用于获取 COVER_IMAGE_MEDIA_ID） ---
def upload_image_material(access_token: str, image_path: str) -> str | None:
    """上传图片作为临时素材，并返回 media_id。"""
    upload_url = f"{WECHAT_BASE_URL}/media/upload?access_token={access_token}&type=image"
    try:
        with open(image_path, 'rb') as f:
            files = {'media': (os.path.basename(image_path), f, 'image/jpeg')}
            print(f"-> 正在尝试上传封面图: {image_path}...")
            response = requests.post(upload_url, files=files)
            response.raise_for_status()
            data = response.json()
            if 'media_id' in data:
                return data['media_id']
            else:
                print(f"-> 图片上传失败: {data.get('errmsg', '未知错误')}")
                return None
    except Exception as e:
        print(f"❌ 上传图片时发生错误: {e}")
        return None