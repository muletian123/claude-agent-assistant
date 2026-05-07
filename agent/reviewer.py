import anthropic
import os

class ReviewerAgent:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = "claude-3-5-sonnet-20241022"

    def review(self, original_input: str, execution_result: str) -> str:
        """审核执行结果，确保质量"""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"""你是一个质量审核专家。
请审核以下任务的执行结果是否符合要求：

原始任务：{original_input}

执行结果：{execution_result}

请：
1. 评估结果质量（1-10分）
2. 指出不足之处
3. 给出优化后的最终结果
"""
                }
            ]
        )
        return message.content[0].text
