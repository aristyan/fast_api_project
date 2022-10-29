# Feature Engineering API project

### Instructions on how to setup, build and execute all modules.

### 1. Install packages using the following commands

```bash
pip install featuretools
pip install pandas
pip install json
pip install fastapi
pip install uvicorn
pip install gunicorn
```

### 2. Create Docker container

```bash
docker build -t feature-extraction-app .

docker run -p 80:80 feature-extraction-app
```

### 3. Create Git repo

If you clone this repo this step is not needed. Or you can delete this git repo with `rm -rf .git` and start with a new one:

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
```
