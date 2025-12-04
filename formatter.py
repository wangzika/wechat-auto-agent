# formatter.py
import markdown
import re
from typing import Tuple

def markdown_to_html(md_text: str) -> Tuple[str, str]:
    """
    将 Markdown 文本转换为基础 HTML，并进行微信公众号优化。

    Returns:
        Tuple[str, str]: (文章标题, 适用于微信公众号的 HTML 内容)
    """
    if not md_text:
        return "", ""

    # 1. 提取文章标题 (假设第一个 # 后的内容是主标题)
    match_title = re.search(r'^#\s*(.+)', md_text, re.MULTILINE)
    article_title = match_title.group(1).strip() if match_title else "AI 自动化生成文章"
    
    # 2. 基础 Markdown 转换
    html_content = markdown.markdown(md_text, extensions=['extra'])
    
    # 3. 微信排版优化（添加行内样式）
    # 为段落添加行高
    html_content = re.sub(r'<p>', '<p style="line-height: 1.8; margin-bottom: 1em;">', html_content)
    
    # 为 H2 标题添加样式
    html_content = re.sub(
        r'<h2>(.*?)</h2>', 
        r'<h2 style="font-size: 1.4em; border-left: 5px solid #007bff; padding-left: 10px; margin: 20px 0; color: #333;">\1</h2>', 
        html_content
    )
    
    # 优化列表项
    html_content = re.sub(r'<li>', '<li style="margin-bottom: 0.5em;">', html_content)

    return article_title, html_content