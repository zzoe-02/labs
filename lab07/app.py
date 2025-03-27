from flask import Flask, render_template, request
import segno
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_qr_code():
    qr_code_data = None
    message = None
    if request.method == 'POST':
        message = request.form['data']
        if message:
            qr_code = segno.make(message)
            img_stream = BytesIO()
            qr_code.save(img_stream, kind='PNG')
            img_stream.seek(0)
            qr_code_data = base64.b64encode(img_stream.read()).decode('utf-8')
    
    return render_template('index.html', qr_code_data=qr_code_data, message=message)
if __name__ == '__main__':
    app.run(debug=True)
