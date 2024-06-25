from flask import Flask, request, render_template
from telethon import TelegramClient

api_id = 12345
api_hash = 'abc'
client = TelegramClient('anon', api_id, api_hash)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def index():
    if request.method == 'POST':

        file = request.files['file1']
        file_path = 'C:/Users/vijay/temp/' + file.filename
        # file.save(file_path)
        # sending files
        await client.send_file('me', file_path)

        # send photos without compression
        await client.send_file('me', file_path, force_document=True)
        
        return render_template('success.html')
    else:
        return render_template('form.html')


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(app.run())
        # app.run()