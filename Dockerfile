From python: 3:11-slim
wrokdir /app
copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt
copy . .
cmd ['python', 'app.py']