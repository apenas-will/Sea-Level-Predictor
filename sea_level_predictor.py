import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_result = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2051, 1)
    y1 = first_result.intercept + first_result.slope * x1 # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
    plt.plot(x1, y1, color='hotpink')

    # Create second line of best fit
    sample = df[df['Year'] >= 2000]
    second_result = linregress(x=sample['Year'], y=sample['CSIRO Adjusted Sea Level'])
    x2 = np.arange(sample['Year'].min(), 2051, 1)
    y2 = second_result.intercept + second_result.slope * x2 # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
    plt.plot(x2, y2, color='crimson')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()