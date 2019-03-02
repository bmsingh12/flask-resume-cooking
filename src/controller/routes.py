from flask import send_file, render_template
from src import app

# @app.route('/')
@app.route('/return-file/')
def return_file():
    return send_file(
        '/home/infotmt-user/PycharmProjects/flask-resume-cooking/src/RandomResumeGenerate/2019-02-20_18:20:52.308464_Samantha Murray')


@app.route('/file-downloads/')
def file_downloads():
    return render_template('downloads.html')


# if __name__ == '__main__':
#         app.run('localhost', 5555)