
### 📄 README.md

````markdown
# 🤖 Wechat Tech Curation Agent: 微信科技策展与自动化发布平台

## 🚀 项目简介 (Project Overview)

本项目是一个基于 **AI Agent** 架构的自动化内容策展与发布系统。它旨在解决科技媒体和公众号运营中内容获取、总结、配图和发布流程耗时耗力的问题。

本 Agent 每日自动执行以下核心任务：

1.  **自动化搜索：** 监控 SLAM、NeRF、3DGS、大模型等前沿科技领域的最新文章。
2.  **AI 总结：** 调用 **DeepSeek API** 总结文章核心亮点，并撰写引人入胜的公众号介绍文。
3.  **智能配图：** 调用 **DeepSeek 图像生成 API** 为文章自动生成配图，并上传至微信永久素材库。
4.  **自动化发布：** 处理文章格式、标题截断、图片链接替换，最终通过微信 API 自动上传草稿并提交群发。

---

## 🛠️ 核心功能与技术栈 (Features & Stack)

| 模块 | 功能描述 | 主要技术 |
| :--- | :--- | :--- |
| **内容生成** | 文章总结、亮点提炼、新标题生成。 | DeepSeek (或兼容 OpenAI 接口的 LLM) |
| **图像处理** | 图像生成、下载、上传至微信永久素材库。 | DeepSeek Image V2 (或 DALL-E) + `requests` |
| **微信发布** | Access Token 管理、图文草稿上传、群发提交。 | 微信公众号高级 API |
| **调度管理** | 每日定时执行搜索、策展、发布全流程。 | Python `schedule` 库 |
| **格式化** | Markdown 到符合微信排版规范的 HTML 转换。 | Python `markdown` |

---

## ⚙️ 快速安装与配置 (Installation & Setup)

### 1. 克隆仓库 (Clone Repository)

```bash
git clone YOUR_REPO_URL
cd wechat-auto-agent
````

### 2\. 环境准备 (Environment Setup)

创建并激活 Python 虚拟环境，并安装所需依赖：

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

pip install openai requests markdown schedule
```

### 3\. 配置密钥 (Configuration)

打开 `config.py` 文件，替换所有占位符 (`YOUR_...`)：

  * `DEEPSEEK_API_KEY`: 你的 DeepSeek API 密钥。
  * `APP_ID` / `APP_SECRET`: 你的微信公众号开发者 ID 和密钥。
  * `COVER_IMAGE_MEDIA_ID`: 文章封面图的永久素材 ID。
  * **[重要]** 微信公众号后台需配置运行环境的 **IP 白名单**。

### 4\. 集成搜索 API (Search API Integration)

打开 `search_api.py`，将模拟数据替换为你选择的**真实搜索 API**（如 Google Custom Search, Bing API 或垂直领域的 API）调用逻辑，以确保 Agent 能够获取最新的文章链接和摘要。

-----

## ▶️ 如何运行 (Usage)

### 首次测试 (Manual Run)

在命令行中直接运行主文件，将立即执行一次策展和发布流程：

```bash
python main_agent.py
```

### 自动化调度 (Scheduled Task)

如果你希望 Agent 每日定时运行，请取消注释 `main_agent.py` 文件末尾 `if __name__ == '__main__':` 块中的 `schedule` 相关代码。默认设置为每日 **09:30** 执行：

```python
# main_agent.py
if __name__ == '__main__':
    # ...
    schedule.every().day.at("09:30").do(automated_curation_and_publishing_task)
    print("定时任务已启动，每日 09:30 将自动执行科技文章策展。")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
```

-----

## 📂 文件结构 (Project Structure)

| 文件名 | 职责 |
| :--- | :--- |
| `main_agent.py` | 任务调度中心，定义执行流程。 |
| `config.py` | 存储所有密钥、ID 和配置常量。 |
| `search_api.py` | 负责与外部搜索 API 交互。 |
| `generator.py` | 调用 LLM 进行文章总结和介绍。 |
| `image_processor.py`| 调用图像 API，并上传图片到微信素材库。 |
| `publisher.py` | 处理所有微信 API 请求（Token、上传、群发）。 |
| `formatter.py` | Markdown 到 HTML 的格式转换和排版优化。 |

-----

## 贡献 (Contributing)

欢迎提交 Issue 和 Pull Request 来改进 Agent 的功能，例如：

  * 集成更多图像生成服务。
  * 优化 HTML 渲染样式。
  * 增加对多平台的自动发布支持。

-----

```
```
