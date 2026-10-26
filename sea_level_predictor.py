import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
  # 1. Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # 2. Create scatter plot
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.scatter(
      df['Year'],
      df['CSIRO Adjusted Sea Level'],
      color='blue',
      alpha=0.7,
      label='Original Data',
  )

  # 3. Create first line of best fit (using all data from 1880 to the most recent year)
  slope_all, intercept_all, r_value, p_value, std_err = linregress(
      df['Year'], df['CSIRO Adjusted Sea Level']
  )

  # Generate array of years from the start year through 2050 for the prediction line
  years_extended = pd.Series([i for i in range(df['Year'].min(), 2051)])
  ax.plot(
      years_extended,
      slope_all * years_extended + intercept_all,
      color='red',
      label='Best Fit (1880-2050)',
  )

  # 4. Create second line of best fit (using data from year 2000 through the most recent year)
  df_recent = df[df['Year'] >= 2000]
  slope_recent, intercept_recent, r_val_rec, p_val_rec, std_err_rec = (
      linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
  )

  # Generate array of years from 2000 through 2050 for the recent prediction line
  years_recent_extended = pd.Series([i for i in range(2000, 2051)])
  ax.plot(
      years_recent_extended,
      slope_recent * years_recent_extended + intercept_recent,
      color='green',
      label='Best Fit (2000-2050)',
  )

  # 5. Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')
  ax.legend()

  # Save plot and return the Axes object for testing
  fig.savefig('sea_level_plot.png')
  return ax