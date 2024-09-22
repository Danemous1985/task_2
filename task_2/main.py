from google.cloud import bigquery
from flask import Flask, render_template

app = Flask(__name__)

"""
route returns main index.html page
"""
@app.route('/')
def index():
    return render_template('index.html')

# Query 1: Top 10 time slots with the highest trade value
"""
This is Query 1. It will show top 10 time slots with highest trade values like assignment brief ask's. I think the result looks correct?
"""
@app.route('/query1')
def query1():
    client = bigquery.Client(project="task2-436212")
    
    # The query with field names, much like SQL query
    query = """
    SELECT time_ref, SUM(value) AS trade_value
    FROM `task2-436212.quarterly.quarterly_sep_20`
    GROUP BY time_ref
    ORDER BY trade_value DESC
    LIMIT 10
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    return render_template('results.html', results=results)


# Leave comment here for add more queries from assignment

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
