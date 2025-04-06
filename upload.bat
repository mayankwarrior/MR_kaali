@echo off
echo Uploading project to GitHub...

git add .
git commit -m "Auto upload"
git push origin main

echo Upload completed!
pause
