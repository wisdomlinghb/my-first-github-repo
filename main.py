from fastapi import FastAPI
import uvicorn

# 创建一个 API 实例（想象成你的餐厅开张了）
app = FastAPI()

# 写一个最基础的 GET 接口（想象成菜单上的第一道菜）
@app.get("/")
def read_root():
    return {"status": "Surviving", "message": "这是我写的第一个 API 接口"}

# 模拟一个 Agent 的对话接口（这就是你以后要把 AI 接进来的地方）
@app.get("/agent/chat")
def chat_endpoint(user_input: str):
    # 真实情况这里会调用大模型，现在我们先写死返回结果
    bot_reply = f"你刚才说了: '{user_input}'。Agent 正在待命中。"
    return {"user_message": user_input, "agent_response": bot_reply}