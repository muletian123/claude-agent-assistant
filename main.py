import os
from dotenv import load_dotenv
from agent.planner import PlannerAgent
from agent.executor import ExecutorAgent
from agent.reviewer import ReviewerAgent

load_dotenv()

def run_agent_pipeline(user_input: str):
    """
    多Agent协作主流程
    Planner -> Executor -> Reviewer
    """
    print(f"\n{'='*50}")
    print(f"📥 用户输入: {user_input}")
    print(f"{'='*50}\n")

    # Step 1: Planner 拆解任务
    planner = PlannerAgent()
    plan = planner.create_plan(user_input)
    print(f"📋 Planner 制定计划:\n{plan}\n")

    # Step 2: Executor 执行任务
    executor = ExecutorAgent()
    result = executor.execute(plan)
    print(f"⚙️ Executor 执行结果:\n{result}\n")

    # Step 3: Reviewer 审核结果
    reviewer = ReviewerAgent()
    final_output = reviewer.review(user_input, result)
    print(f"✅ Reviewer 最终输出:\n{final_output}\n")

    return final_output

if __name__ == "__main__":
    while True:
        user_input = input("\n请输入你的任务（输入 quit 退出）: ")
        if user_input.lower() == "quit":
            break
        run_agent_pipeline(user_input)
