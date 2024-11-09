import json
from datetime import datetime, timedelta

DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, name, due_date, priority):
    task = {
        "name": name,
        "due_date": due_date,
        "priority": priority
    }
    tasks.append(task)
    print(f"任务“{name}”已添加！")

def view_tasks(tasks):
    if tasks:
        print("\n所有任务：")
        for idx, task in enumerate(sorted(tasks, key=lambda x: (x["priority"], x["due_date"])), 1):
            print(f"{idx}. 任务：{task['name']} | 到期时间：{task['due_date']} | 优先级：{task['priority']}")
    else:
        print("没有待办任务。")

def view_due_soon(tasks):
    print("\n即将到期的任务：")
    now = datetime.now()
    due_soon = [task for task in tasks if datetime.strptime(task['due_date'], "%Y-%m-%d") <= now + timedelta(days=3)]
    
    if due_soon:
        for idx, task in enumerate(sorted(due_soon, key=lambda x: x["due_date"]), 1):
            print(f"{idx}. 任务：{task['name']} | 到期时间：{task['due_date']} | 优先级：{task['priority']}")
    else:
        print("没有即将到期的任务。")

if __name__ == "__main__":
    tasks = load_tasks()
    print("欢迎使用任务管理器！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加新任务")
        print("2. 查看所有任务")
        print("3. 查看即将到期的任务")
        print("4. 退出")

        choice = input("请输入选项（1/2/3/4）：")

        if choice == "1":
            name = input("请输入任务名称：")
            due_date = input("请输入到期时间（格式YYYY-MM-DD）：")
            priority = int(input("请输入优先级（1-高，2-中，3-低）："))
            add_task(tasks, name, due_date, priority)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_due_soon(tasks)
        elif choice == "4":
            print("感谢使用任务管理器，再见！")
            break
        else:
            print("无效选项，请重新选择。")
