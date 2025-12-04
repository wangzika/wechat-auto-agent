import os
from openai import OpenAI
from openai.types.chat import ChatCompletion

# --- DeepSeek API 配置 ---
# DeepSeek 官方 API 基础地址
DEEPSEEK_BASE_URL = "https://api.deepseek.com" 

# 你的 DeepSeek API Key (建议通过环境变量获取)
# DEEPSEEK_API_KEY=os.environ["DEEPSEEK_API_KEY"] = ""DEEPSEEK_API_KEY", "YOUR_API_KEY")"
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-eeadd97971ef4880a814477be5940d42") # 替换为你的真实 Key

# 初始化 OpenAI 客户端，指向 DeepSeek API
try:
    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL
    )
except Exception as e:
    print(f"❌ 初始化 OpenAI 客户端失败：{e}")
    client = None

# 使用 DeepSeek 推荐的模型
DEEPSEEK_MODEL = "deepseek-chat" # 推荐使用 deepseek-chat 或 deepseek-coder (如果需要编程主题)


def generate_article(topic: str, word_count: int = 1500) -> str:
    """
    使用 DeepSeek 模型生成一篇公众号文章草稿。
    """
    if not client:
        print("❌ 客户端未成功初始化，无法调用 API。")
        return ""

    # 构造给模型的系统提示词
    system_prompt = (
        "你是一位专业的公众号文章创作者。请围绕用户给定的主题，"
        "撰写一篇引人入胜、结构清晰的深度文章。文章应该包含清晰的标题、"
        "小标题，并使用Markdown格式输出。风格应积极、专业、富有洞察力。"
    )
    
    # 构造用户输入
    user_input = f"主题：{topic}。请务必用中文撰写一篇适合公众号发布的文章，内容深度足够，预期字数约{word_count}字。"

    print(f"-> 正在调用 DeepSeek API 生成文章：【{topic}】...")

    try:
        completion: ChatCompletion = client.chat.completions.create(
            model=DEEPSEEK_MODEL, 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7 # 调整创造性
        )
        
        # 检查响应并提取内容
        if completion.choices:
            article_content = completion.choices[0].message.content
            print("-> 文章生成成功。")
            return article_content
        else:
            print("-> API 调用成功，但未返回内容。")
            return ""

    except Exception as e:
        print(f"-> 调用 DeepSeek API 时发生错误: {e}")
        return ""

if __name__ == '__main__':
    # 示例：生成一篇关于AI Agent的文章
    # 注意：运行前请确保 DEEPSEEK_API_KEY 已替换或设置到环境变量中
    article = generate_article("DeepSeek 模型在内容自动化生成中的应用优势", 2000)
    if article:
        print("\n--- 生成的文章初稿 ---\n")
        print(article)
        print("\n-----------------------\n")