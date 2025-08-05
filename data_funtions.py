import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import mplfinance as mpf
def set_stock_data_file(stock_name):
    st.session_state["current_page"] = "dashbord_page"
    st.session_state["current_stock"] = stock_name
    st.session_state["current_stock_file_path"] = f"D:\\project-3\\stock_market_data\\{stock_name}_DATA_SET.csv"


def initilaze():
    if("current_stock" not in st.session_state):
        st.session_state["current_stock"] = None

    if("current_stock_file_path" not in st.session_state):
        st.session_state["current_stock_file_path"] = None

    if("current_page" not in st.session_state):
        st.session_state["current_page"] = "landing_page"
@st.cache_data
def clean_data(dataframe):
    dataframe = dataframe[(~dataframe['ema_10_close'].isna()) & (~dataframe['sma_9_ema'].isna())]
    dataframe = dataframe.reset_index(drop=True)
    dataframe = dataframe.drop_duplicates(subset=["timestamp"])
    dataframe = dataframe.drop(columns="oi")
    return dataframe
@st.cache_data
def eda(dataframe):
    dataframe.insert(1,"Date",pd.to_datetime(dataframe["timestamp"]).dt.date)
    dataframe.insert(2,"Time",pd.to_datetime(dataframe["timestamp"]).dt.time)
    dataframe.insert(2,"Day",pd.to_datetime(dataframe["Date"]).dt.day_name())
    dataframe["returns"] = dataframe["close"].pct_change()
    dataframe["daily_risk"] = dataframe["returns"].abs()
    dataframe['performance'] = dataframe["returns"]*100
    dataframe.dropna(subset=['performance'])
    dataframe=dataframe.dropna(subset = ["returns"])
    dataframe = dataframe.reset_index(drop=True)
    dataframe['prev_sma_9_ema'] = dataframe['sma_9_ema'].shift(1)
    dataframe['prev_ema_10_close'] = dataframe['ema_10_close'].shift(1)
    bullish_cross = (dataframe['sma_9_ema'] > dataframe['ema_10_close']) & (dataframe['prev_sma_9_ema'] <= dataframe['prev_ema_10_close'])
    bearish_cross = (dataframe['sma_9_ema'] < dataframe['ema_10_close']) & (dataframe['prev_sma_9_ema'] >= dataframe['prev_ema_10_close'])
    confirmed_bullish = bullish_cross & (dataframe['close'] > dataframe['ema_10_close'])
    confirmed_bearish = bearish_cross & (dataframe['close'] < dataframe['ema_10_close'])
    dataframe['trend_direction'] = np.where(confirmed_bullish, 'Bullish',
                         np.where(confirmed_bearish, 'Bearish', 'Neutral'))
    dataframe.drop(['prev_sma_9_ema', 'prev_ema_10_close'], axis=1, inplace=True)
    return dataframe
@st.cache_data
def find_current_values(dataframe):
    current_values = dataframe.loc[len(dataframe)-1,["open","close","ema_10_close","sma_9_ema"]]
    return current_values
@st.cache_data
def find_volatility_of_stock(dataframe):
    mean_return  = np.nanmean(dataframe["returns"])
    volatility = np.nanstd(dataframe["returns"])
    annual_volatility = volatility* math.sqrt(252)
    annual_volatility *= 100
    return annual_volatility

def find_sum_volume(dataframe):
    volume_traded = int(np.nansum(dataframe["volume"]))/10000000
    volume_traded = round(volume_traded, 1)
    return str(volume_traded) + "M"

def find_mean_volume(dataframe):
    volume_traded = int(np.nanmean(dataframe["volume"])) / 1000
    volume_traded = round(volume_traded, 1)
    return str(volume_traded) + "K"

def find_median_volume(dataframe):
    volume_traded = int(np.nanmedian(dataframe["volume"])) / 1000
    volume_traded = round(volume_traded, 1)
    return str(volume_traded) + "K"

def find_highest_open_price_date(dataframe):
    highest_open_price = np.nanmax(dataframe["open"])
    highest_open_rows = dataframe.loc[dataframe["open"] == highest_open_price, ["Date", "open"]]
    highest_open_price = highest_open_rows["open"].values[0]
    highest_open_price_date = pd.to_datetime(highest_open_rows["Date"].values[0]).strftime('%b %d, %Y')
    return [highest_open_price, highest_open_price_date]
@st.cache_data
def find_highest_price_stock_data(dataframe):
    highest_price = np.nanmax(dataframe["high"])
    highest_price_row = dataframe.loc[dataframe["high"] == highest_price,["Date","high"]]
    highest_price = highest_price_row["high"].values[0]
    highest_price_date = pd.to_datetime(highest_price_row["Date"].values[0]).strftime('%b %d, %Y')
    return [highest_price,highest_price_date]

def find_lowest_price_stock_data(dataframe):
    lowest_price = np.nanmax(dataframe["low"])
    lowest_price_row = dataframe.loc[dataframe["low"] == lowest_price,["Date","low"]]
    lowest_price = lowest_price_row["low"].values[0]
    lowest_price_date = pd.to_datetime(lowest_price_row["Date"].values[0]).strftime('%b %d, %Y')
    return [lowest_price,lowest_price_date]


def find_annual_risk(dataframe):
    avg_risk = dataframe["returns"].std()*100
    annual_risk = avg_risk*np.sqrt(252)
    annual_risk = round(annual_risk,3)
    return annual_risk

def find_min_risk(dataframe):
    min_risk_row = dataframe.loc[dataframe['daily_risk'] > 0, 'daily_risk'].idxmin()
    min_risk_value = (dataframe.loc[min_risk_row, 'daily_risk'])*100
    min_risk_value = round(min_risk_value,3)
    min_risk_date = dataframe.loc[min_risk_row,"Date"].strftime('%b %d, %Y')
    return [min_risk_value,min_risk_date]

def find_max_risk(dataframe):
    max_risk_row = dataframe["daily_risk"].idxmax()
    max_risk_value = (dataframe.loc[max_risk_row,"daily_risk"])*100
    max_risk_value = round(max_risk_value,3)
    max_risk_date = dataframe.loc[max_risk_row,"Date"].strftime('%b %d, %Y')
    return [max_risk_value,max_risk_date]
@st.cache_data
def trand_analysis(dataframe):
    
    last_direction = dataframe.loc[len(dataframe)-1,"trend_direction"]
    return last_direction
@st.cache_data
def gap_analysis(dataframe, threshold=0):
    """
    Perform gap analysis on a DataFrame with 'open' and 'close' price columns.
    Returns a list of tuples: (gap_value, gap_classification)
    
    Parameters:
    - df: pandas DataFrame with 'open' and 'close' columns
    - threshold: numeric, minimum gap size to consider (default 0 means any gap)
    
    Returns:
    - List of tuples: [(gap_value, 'Gap Up'|'Gap Down'|'No Gap'), ...]
    """
    # Make sure columns exist
    if 'open' not in dataframe.columns or 'close' not in dataframe.columns:
        raise ValueError("DataFrame must contain 'open' and 'close' columns")
    
    # Step 1: Previous closing price
    df = dataframe.copy()
    df['prev_close'] = df['close'].shift(1)
    
    # Step 2: Gap value = open - previous close
    df['gap'] = df['open'] - df['prev_close']
    
    # Step 3: Function to classify gaps
    def classify_gap(row):
        if pd.isnull(row['prev_close']):
            return "No Gap"
        if row['gap'] > threshold:
            return "Gap Up"
        elif row['gap'] < -threshold:
            return "Gap Down"
        else:
            return "No Gap"
    
    # Step 4: Apply classification
    df['gap_type'] = df.apply(classify_gap, axis=1)
    
    # Step 5: Prepare list of tuples (gap_value, gap_type)
    gap_list = list(zip(df['gap'].fillna(0), df['gap_type']))
    
    return gap_list[-1]
@st.cache_data
def OHLC_moving_average_graph(dataframe):
    fig, ax = plt.subplots(figsize=(12, 6))
    df_grup = dataframe.groupby("Date")[["open","high","low","close","volume","ema_10_close","sma_9_ema"]].mean()
    ax.plot(df_grup.index, df_grup['close'], label='Close Price', color='black', linewidth=2)
    ax.plot(df_grup.index, df_grup['ema_10_close'], label='EMA 10', color='blue', linestyle='dotted', linewidth=2)
    if 'sma_9_ema' in dataframe.columns:
        ax.plot(df_grup.index, df_grup['sma_9_ema'], label='SMA 9 EMA', color='cyan', linestyle='dashed', linewidth=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.xticks(rotation=45)
    fig.tight_layout()
    ax.grid(True, linestyle=':', linewidth=0.75)
    ax.legend(frameon=True, fontsize='medium')
    return fig
@st.cache_data
def volume_analysis_graph(dataframe):

    df = dataframe.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    daily_vol = (
        df.groupby('Date', as_index=False)['volume']
        .mean()
        .sort_values('Date')
        .reset_index(drop=True)
    )
    colors = ['green']
    for i in range(1, len(daily_vol)):
        if daily_vol.loc[i, 'volume'] > daily_vol.loc[i-1, 'volume']:
            colors.append('green')
        else:
            colors.append('red')

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(daily_vol['Date'], daily_vol['volume'], color=colors, width=0.8)
    ax.set_xlabel('Date')
    ax.set_ylabel('Average Volume')
    fig.autofmt_xdate(rotation=45)
    
    return fig

@st.cache_data
def corelation_analysis(dataframe):
    num_df = dataframe.select_dtypes(include='number')
    num_df = num_df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(num_df, ax=ax, cmap='coolwarm', annot=True, fmt='.2f')
    plt.tight_layout()
    return fig
@st.cache_data
def trend_analysis_graph(dataframe):
    counts = dataframe["trend_direction"].value_counts()
    percentages = counts / counts.sum() * 100

    # Define mapping for labels and colors
    label_color_map = {
        "Bullish": "green",
        "Bearish": "red",
        "Neutral": "lightskyblue"  # Light blue
    }
    labels = [f"{lbl}: {percentages[lbl]:.1f}%" for lbl in counts.index]
    colors = [label_color_map.get(lbl, 'grey') for lbl in counts.index]

    # Plot pie chart with a hole (donut)
    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts = ax.pie(counts,
                           labels=labels,
                           colors=colors,
                           startangle=90,
                           wedgeprops=dict(width=0.3))
    return fig

def volume_distribution_by_range(dataframe,bins = 10):
    df = dataframe.copy()
    # Create price bins (intervals)
    min_price = df["close"].min()
    max_price = df["close"].max()
    bin_edges = np.linspace(min_price, max_price, bins + 1)
    df['price_bin'] = pd.cut(df["close"], bins=bin_edges, include_lowest=True)

    # Sum volumes within each bin
    summary_df = df.groupby('price_bin', observed=True)["volume"].sum().reset_index()

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(summary_df['price_bin'].astype(str), summary_df["volume"], color='steelblue')
    ax.set_xlabel('Price Range')
    ax.set_ylabel('Total Volume')
    plt.xticks(rotation=45, ha='right')
    
    # Set x-tick labels bold
    for tick in ax.get_xticklabels():
        tick.set_fontweight('bold')

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'{int(height)}',
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # vertical offset in points
            textcoords='offset points',
            ha='center', va='bottom',
            fontsize=10, fontweight='bold'
        )

    plt.tight_layout()
    return fig
@st.cache_data
def daily_performance_analysis(dataframe,max_bars = 30):
    df = dataframe.tail(max_bars).copy()
    
    # Color bars
    bar_colors = ['green' if x >= 0 else 'red' for x in df['performance']]
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    
    sns.barplot(x=df["Date"], y='performance', data=df, palette=bar_colors, ax=ax)

    # Label (example: every 5th bar + last bar)
    # for i, row in df.reset_index(drop=True).iterrows():
    #     if i % 5 == 0 or i == len(df) - 1:
    #         ax.text(i, row['performance'] + (0.01 * df['performance'].max()),
    #                 f"{row['performance']:.2f}",
    #                 color='black', ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.set_xlabel('Date')
    ax.set_ylabel('Daily Return (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

@st.cache_data
def overall_price_trend(df):

    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    sortData = df.sort_values(by="timestamp").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        x=sortData["timestamp"],
        y=sortData["close"],
        label="Closing Price",
        ax=ax
    )
    ax.set_xlabel("Time")
    ax.set_ylabel("Closing Price (INR)")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

@st.cache_data
def boxplot_close_price(dataframe):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(y=dataframe["close"], ax=ax)
    ax.set_xlabel("Closing Price")
    return fig

@st.cache_data
def skewness_of_close(dataframe):
    fig, ax = plt.subplots(figsize=(12, 6))
    # KDE for close price
    sns.kdeplot(dataframe['close'], fill=True, color='cornflowerblue', label='Close Price', ax=ax)
    close_skew = dataframe['close'].skew()
    ax.text(0.05, 0.85, f"Close Price Skewness: {close_skew:.2f}", transform=ax.transAxes,
            fontsize=12, fontweight='bold', bbox=dict(boxstyle='round', fc='w', ec='k'))


    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    plt.tight_layout()
    return fig
@st.cache_data
def skewness_of_volume(dataframe):
    fig, ax = plt.subplots(figsize=(12, 6))

    # KDE for volume
    sns.kdeplot(dataframe['volume'], fill=True, color='orange', label='Volume', ax=ax)
    volume_skew = dataframe['volume'].skew()
    ax.text(0.05, 0.75, f"Volume Skewness: {volume_skew:.2f}", transform=ax.transAxes,
            fontsize=12, fontweight='bold', bbox=dict(boxstyle='round', fc='w', ec='k'))

    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    plt.tight_layout()
    return fig