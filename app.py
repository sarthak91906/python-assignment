"""
Global State/Province Demographic Analyzer
A Flask web application that analyzes demographic data of U.S. states
using pandas for data processing and Chart.js for visualization.
"""

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    """
    Main route that processes demographic data and renders the template.
    Creates a DataFrame with U.S. state data, calculates population density,
    and identifies the state with highest density.
    """
    
    # Create dataset of 10 real U.S. states with demographic data
    data = {
        'State': [
            'California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
            'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan'
        ],
        'Area': [
            423967, 695662, 170312, 141297, 119280,
            149995, 116098, 153910, 137309, 250487
        ],
        'Population': [
            39538223, 29145505, 21538187, 20201249, 13002700,
            12812508, 11799448, 10711908, 10439388, 10077331
        ]
    }
    
    # Load data into pandas DataFrame
    df = pd.DataFrame(data)
    
    # Calculate population density (people per sq km)
    df['Population_Density'] = df['Population'] / df['Area']
    
    # Sort by population density (highest first) for better visualization
    df_sorted = df.sort_values('Population_Density', ascending=False)
    
    # Identify state with highest population density
    highest_density_state = df_sorted.iloc[0]
    highest_density_name = highest_density_state['State']
    highest_density_value = round(highest_density_state['Population_Density'], 2)
    
    # Prepare data for Chart.js
    # Convert DataFrame to dictionary format for JSON serialization
    chart_data = {
        'labels': df['State'].tolist(),
        'areas': df['Area'].tolist(),
        'populations': df['Population'].tolist(),
        'densities': [round(density, 2) for density in df['Population_Density'].tolist()]
    }
    
    # Prepare table data with formatted numbers
    table_data = []
    for _, row in df_sorted.iterrows():
        table_data.append({
            'state': row['State'],
            'area': f"{row['Area']:,}",  # Format with commas
            'population': f"{row['Population']:,}",  # Format with commas
            'density': round(row['Population_Density'], 2)
        })
    
    # Render template with all required data
    return render_template('index.html',
                         table_data=table_data,
                         highest_density_name=highest_density_name,
                         highest_density_value=highest_density_value,
                         chart_data=chart_data)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True, host='127.0.0.1', port=5000)
