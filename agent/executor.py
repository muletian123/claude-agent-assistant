import anthropic
import os

class ExecutorAgent:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = "claude-3-5-sonnet-20241022"

    def execute(self, plan: str) -> str:
        """根据计划执行任务"""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": f"""你是一个任务执行专家。
请根据以下计划，逐步执行并给出详细结果：

计划：
{plan}

请详细执行每个步骤并输出结果。
"""
                }
            ]
        )
        return message.content[0].text
