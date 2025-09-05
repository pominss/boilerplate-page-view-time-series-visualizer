import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date")

# Clean data
maior = df["value"].quantile(0.975)
menor = df["value"].quantile(0.025)
df = df[(df["value"] >= menor) & (df["value"] <= maior)]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["value"])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index)
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    # Draw bar plot
    fig = df_grouped.plot(kind = "bar", figsize = (12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title = "Months", labels = ["January","February","March","April","May","June", "July","August","September","October","November","December"])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.index = pd.to_datetime(df_box.index)
    df_box.reset_index(inplace = True)
    df_box["year"] = [d.year for d in df_box["date"]]
    df_box["month"] = [d.strftime("%b") for d in df_box["date"]]


    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize = (12, 6))

    plt.subplot(1, 2, 1)
    sns.boxplot(x = "year", y = "value", data = df_box)
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")

    plt.subplot(1, 2, 2)
    sns.boxplot(x = "month", y = "value", order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], data = df_box)
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    plt.title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
