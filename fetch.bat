@echo off
git pull origin main
python mcp.py
git add .
git commit -m "daily commit"
git push origin main