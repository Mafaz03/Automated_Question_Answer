import plotly.express as px
import pandas as pd

def grant_study_time_table(weeks_start, weeks_end, module, descriptions):
    data = {
        'Weeks Start': weeks_start,
        'Weeks End': weeks_end,
        'Modules': module,
        'Description': descriptions
    }

    # Create a dataframe
    df = pd.DataFrame(data)

    # Convert the 'Weeks Start' and 'Weeks End' columns to datetime
    df['Weeks Start'] = pd.to_datetime(df['Weeks Start'])
    df['Weeks End'] = pd.to_datetime(df['Weeks End'])

    # Create the Gantt chart
    fig = px.timeline(df, x_start='Weeks Start', x_end='Weeks End', 
                    y='Modules', text='Description', title="B.Tech AI & DS Study Plan")

    # Update layout for transparency and better styling
    fig.update_traces(marker_color='rgba(0, 123, 255, 0.6)', opacity=0.9)
    fig.update_layout(yaxis_title="Modules", xaxis_title="Timeline", plot_bgcolor='rgba(0,0,0,0)')

    return fig

from datetime import datetime, timedelta

def convert_week_ranges(week_ranges, start_date=None):
    """
    Convert week ranges (e.g., 'Week 1-2:') to start and end dates based on a start date.
    
    Parameters:
    week_ranges (list): List of week range strings (e.g., 'Week 1-2:').
    start_date (datetime): Starting date for the first week (default is today).
    
    Returns:
    tuple: Lists of start and end dates for each week range.
    """
    if start_date is None:
        start_date = datetime.today()

    weeks_start = []
    weeks_end = []

    for week_range in week_ranges:
        week_start, week_end = [int(w) for w in week_range.split(' ')[1].replace(':', '').split('-')]

        week_start_date = start_date + timedelta(weeks=(week_start - 1))
        week_end_date = start_date + timedelta(weeks=week_end)

        weeks_start.append(week_start_date)
        weeks_end.append(week_end_date)

    return weeks_start, weeks_end