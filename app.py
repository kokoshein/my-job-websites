import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

# ၁။ ဒါက အရင်ဆုံး လာရပါမယ် (Flask ကို စတင်သတ်မှတ်ခြင်း)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# ၂။ Database နဲ့ ချိတ်ဆက်ပေးမယ့် Function
def get_db_connection():
    conn = sqlite3.connect('jobs.db')
    conn.row_factory = sqlite3.Row
    return conn

# ၃။ ပြီးမှ Route (စာမျက်နှာတွေ) လာရပါမယ်
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    location = request.args.get('location', '')
    conn = get_db_connection()
    sql_query = "SELECT * FROM jobs WHERE title LIKE ? AND location LIKE ?"
    jobs = conn.execute(sql_query, ('%' + query + '%', '%' + location + '%')).fetchall()
    conn.close()
    return render_template('results.html', jobs=jobs, query=query)

@app.route('/post_job', methods=('GET', 'POST'))
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        salary = request.form['salary']
        phone = request.form['phone']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO jobs (title, location, salary, phone, description) VALUES (?, ?, ?, ?, ?)',
                    (title, location, salary, phone, description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('post_job.html')

# ၄။ ဒါက နောက်ဆုံးမှ လာရပါမယ် (Program ကို စတင် Run ခြင်း)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)