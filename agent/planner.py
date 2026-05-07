import anthropic
import os

class PlannerAgent:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = "claude-3-5-sonnet-20241022"

    def create_plan(self, user_input: str) -> str:
        """将用户任务拆解为可执行步骤"""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"""你是一个任务规划专家。
请将以下任务拆解为清晰的执行步骤：

任务：{user_input}

请按照以下格式输出：
1. 步骤一
2. 步骤二
3. 步骤三
...
"""
                }
            ]
        )
        return message.content[0].text
