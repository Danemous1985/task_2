from google.cloud import bigquery
from flask import Flask, render_template

app = Flask(__name__)

"""
route returns main index.html page
"""
@app.route('/')
def index():
    return render_template('index.html')

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

"""
query 2 as defined in the assignment brief. Show top 40 countries with the highest total trade deficit value (i.e. import value - export value) of goods from 2013 to 2015 where status is “F”.
"""
@app.route('/query2')
def query2():
    client = bigquery.Client(project="task2-436212")
    
    query = """
    SELECT country_classification.country_label, product_type, 
           SUM(CASE WHEN account = 'Imports' THEN value ELSE -value END) AS trade_deficit_value, 
           status
    FROM `task2-436212.quarterly.quarterly_sep_20` AS quarterly_sep_20
    LEFT JOIN `task2-436212.country.country_classification` AS country_classification 
    ON quarterly_sep_20.country_code = country_classification.country_code
    WHERE time_ref BETWEEN '201301' AND '201512' AND status = 'F'
    GROUP BY country_classification.country_label, product_type, status
    ORDER BY trade_deficit_value DESC
    LIMIT 40
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    return render_template('results2.html', results=results)

"""
This query was really difficult to get right. I'm pretty sure I got it, the results that I'm getting seem to be correct. Can confirm in my demonstration with Tim. Show top 25 services with the highest total trade surplus value (i.e. export value - import value) in the top 10 time slots of Query Result 1 and the top 40 countries of Query Result 2.
"""
@app.route('/query3')
def query3():
    client = bigquery.Client(project="task2-436212")
    
    query = """
    WITH top_time_slots AS (
        SELECT time_ref
        FROM `task2-436212.quarterly.quarterly_sep_20`
        GROUP BY time_ref
        ORDER BY SUM(value) DESC
        LIMIT 10
    ),
    top_countries AS (
        SELECT c.country_code
        FROM `task2-436212.quarterly.quarterly_sep_20` AS q
        JOIN `task2-436212.country.country_classification` AS c
        ON q.country_code = c.country_code
        WHERE q.time_ref BETWEEN '201301' AND '201512'
        AND q.account = 'Imports'
        GROUP BY c.country_code
        ORDER BY SUM(q.value) DESC
        LIMIT 40
    )
    SELECT s.service_label, 
           SUM(CASE WHEN q.account = 'Exports' THEN q.value ELSE -q.value END) AS trade_surplus_value
    FROM `task2-436212.quarterly.quarterly_sep_20` AS q
    JOIN `task2-436212.services.services_classification` AS s
    ON q.code = s.code
    WHERE q.time_ref IN (SELECT time_ref FROM top_time_slots)
    AND q.country_code IN (SELECT country_code FROM top_countries)
    GROUP BY s.service_label
    ORDER BY trade_surplus_value DESC
    LIMIT 25
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    return render_template('results3.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
