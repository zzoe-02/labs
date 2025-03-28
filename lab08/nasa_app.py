from flask import Flask, render_template, request
from apod_calls import get_apod_data
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.now().strftime('%Y-%m-%d')
    apod_data = get_apod_data(today)
    return render_template('home.html', apod=apod_data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'POST':
        date = request.form.get('date')
        try:
            apod_data = get_apod_data(date)
            return render_template('history.html', apod=apod_data)
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template('history.html', apod=None)

if __name__ == "__main__":
    app.run(debug=True)
