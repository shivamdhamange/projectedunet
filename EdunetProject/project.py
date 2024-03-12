# app.py

from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Your existing code for importing, cleaning, and processing data
df = pd.read_csv("EdunetProject/athlete_events (1).csv")
df.drop_duplicates(inplace=True)
df.dropna(subset=['Age', 'Height', 'Weight'], inplace=True)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for processing athlete information
@app.route('/get_info', methods=['POST'])
def get_info():
    athlete_name = request.form['athlete_name']
    athlete_info_name = df[df['Name'] == athlete_name]

    if not athlete_info_name.empty:
        # Generate HTML table
        table_html = athlete_info_name.to_html(index=False, escape=False)

        return jsonify({'success': True, 'info_text': table_html})
    else:
        return jsonify({'success': False, 'message': f"No information found for Athlete with Name '{athlete_name}'."})

if __name__ == '__main__':
    app.run(debug=True)
