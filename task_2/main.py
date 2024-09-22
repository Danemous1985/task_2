from google.cloud import bigquery
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query1')
def query1():
    client = bigquery.Client()
    query = """
    SELECT time_ref, SUM(import_value + export_value) AS trade_value
    FROM `assignment1_dataset.gsquarterlySeptember20`
    GROUP BY time_ref
    ORDER BY trade_value DESC
    LIMIT 10
    """
    query_job = client.query(query)
    results = query_job.result()
    return render_template('results.html', results=results)

# Add more query routes if needed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
