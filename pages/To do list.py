import streamlit as st
from streamlit.components.v1 import html

# Initialize session state for todo list
if "todo_list" not in st.session_state:
    st.session_state["todo_list"] = []

# HTML, CSS, and JavaScript code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To do list</title>
    <style>
        .completed {
            text-decoration: line-through;
            opacity: 0.4;
        }
        .del {
            color: red;
            cursor: pointer;
        }
        .todo-button {
            width: 100px;
            height: 52px;
            border-radius: 0 20px 20px 0;
            line-height: 52px;
            text-align: center;
            background: linear-gradient(to right, rgb(113, 65, 168), rgb(44, 114, 251, 1));
            color: #fff;
            cursor: pointer;
            user-select: none;
        }
        .todo-input {
            margin-bottom: 20px;
            padding-left: 15px;
            border: 1px solid #dfe1e5;
            outline: none;
            width: 60%;
            height: 50px;
            border-radius: 20px 0 0 20px;
        }
        .todo-from {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-sizing: border-box;
            width: 80%;
            height: 50px;
            margin: 8px auto;
            padding: 16px;
            border-radius: 20px;
            box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 20px;
        }
        body {
            background: linear-gradient(to right, rgb(113, 65, 168), rgb(44, 114, 251, 1));
        }
        .todo-app {
            width: 98%;
            padding: 30px 0 30px 0;
            box-sizing: border-box;
            background-color: #fff;
            border-radius: 5px;
            margin-top: 40px;
            margin-left: 1%;
        }
        .title {
            font-size: 30px;
            font-weight: 700;
            text-align: center;
        }
        .todo-items {
            padding-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="todo-app">
        <div class="title">Jason To do list</div>
        <div class="todo-from">
            <input class="todo-input" type="text" placeholder="add a to do">
            <div class="todo-button">add</div>
        </div>
        <div class="todo-items"></div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const input = document.querySelector('.todo-input');
            const addButton = document.querySelector('.todo-button');
            const todoItemsContainer = document.querySelector('.todo-items');

            // Load tasks from Streamlit session
            const loadTasks = () => {
                const tasks = window.localStorage.getItem("todo_list");
                if (tasks) {
                    JSON.parse(tasks).forEach(task => {
                        addItemToList(task.text, task.completed);
                    });
                }
            };

            // Add task to the list
            const addTask = () => {
                const taskText = input.value.trim();
                if (taskText) {
                    addItemToList(taskText);
                    input.value = '';
                    saveTasksToBackend();
                }
            };

            // Create task element and add it to the list
            const addItemToList = (text, completed = false) => {
                const newItem = document.createElement('div');
                newItem.classList.add('item');
                newItem.innerHTML = `
                    <div>
                        <input type="checkbox" ${completed ? 'checked' : ''} />
                        <span class="name">${text}</span>
                    </div>
                    <div class="del">🗑️</div>
                `;
                todoItemsContainer.appendChild(newItem);
            };

            // Save tasks to Streamlit backend
            const saveTasksToBackend = () => {
                const tasks = Array.from(todoItemsContainer.children).map(item => {
                    const checkbox = item.querySelector('input[type="checkbox"]');
                    return {
                        text: item.querySelector('.name').textContent,
                        completed: checkbox.checked
                    };
                });
                window.localStorage.setItem("todo_list", JSON.stringify(tasks));
                fetch("/save", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ tasks })
                });
            };

            // Event listener for adding a task
            addButton.addEventListener('click', addTask);
            input.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    addTask();
                }
            });

            // Event listener for task completion and deletion
            todoItemsContainer.addEventListener('click', (e) => {
                if (e.target.tagName === 'INPUT' && e.target.type === 'checkbox') {
                    const task = e.target.closest('.item');
                    task.classList.toggle('completed');
                    saveTasksToBackend();
                } else if (e.target.classList.contains('del')) {
                    const task = e.target.closest('.item');
                    task.remove();
                    saveTasksToBackend();
                }
            });

            // Load tasks on startup
            loadTasks();
        });
    </script>
</body>
</html>
"""

# Embed the HTML in Streamlit
html(html_code, height=800, scrolling=True)

# Save tasks to session state
def save_tasks_to_session(tasks):
    st.session_state["todo_list"] = tasks

# When data is sent from the front end
tasks = st.query_params.get("tasks", [])
if tasks:
    save_tasks_to_session(tasks)
