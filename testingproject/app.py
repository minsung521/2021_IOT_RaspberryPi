from flask import Flask, render_template, redirect
import os
import dir_search

PIN = 17# 핀 번호

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

imageNameSet = []

# 라우팅을 위한 뷰 함수
@app.route("/")
def home():
    try: 
        path = ''.join([os.getcwd(),"/static/images"])
        imageNameSet = dir_search.search(path)
        print(imageNameSet)
    except Exception as e: 
        print(e)
    return render_template("index.html", imageNames = imageNameSet)


@app.route("/delete/<imgFile>")
def imgDel(imgFile):
    path = ''.join(["./static/images/",imgFile])
    if os.path.isfile(path) : 
        os.remove(path)

# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")