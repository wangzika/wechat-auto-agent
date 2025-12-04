# generator.py
import os
from openai import OpenAI
from openai.types.chat import ChatCompletion
from config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL

# 初始化 OpenAI 客户端，指向 DeepSeek API
try:
    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL
    )
except Exception as e:
    print(f"❌ 初始化 OpenAI 客户端失败：{e}")
    client = None

def generate_article(topic: str, word_count: int = 1500) -> str:
    """
    使用 DeepSeek 模型生成一篇公众号文章草稿。
    """
    if not client:
        print("❌ 客户端未成功初始化，无法调用 API。")
        return ""

    system_prompt = (
        "你是一位专业的公众号文章创作者。请围绕用户给定的主题，"
        "撰写一篇引人入胜、结构清晰的深度文章。文章应该包含清晰的标题、"
        "小标题，并使用Markdown格式输出。风格应积极、专业、富有洞察力。"
    )
    
    user_input = f"主题：{topic}。请务必用中文撰写一篇适合公众号发布的文章，内容深度足够，预期字数约{word_count}字。"

    print(f"-> 正在调用 DeepSeek API 生成文章：【{topic}】...")

    try:
        completion: ChatCompletion = client.chat.completions.create(
            model=DEEPSEEK_MODEL, 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7 
        )
        
        if completion.choices:
            return completion.choices[0].message.content
        else:
            print("-> API 调用成功，但未返回内容。")
            return ""

    except Exception as e:
        print(f"-> 调用 DeepSeek API 时发生错误: {e}")
        return ""