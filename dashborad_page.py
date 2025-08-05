import streamlit as st
from data_funtions import *


remove_header_footer = """
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* Hide the orange loading progress bar */
div[data-testid="stDecoration"] {
    display: none !important;
}

/* Remove top padding to avoid white space */
.block-container {
    padding-top: 0rem !important;
}
"""

page_setup = """
/* Set entire app background color */
.stApp {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #f8faff 0%, #ffffff 50%, #f0f4ff 100%);
    color: #1e2331;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Arial, sans-serif;
    overflow-x: hidden;
    width:100%;
}

/* Optional: to set sidebar background and text colors */
[data-testid="stSidebar"] {
    background-color: white !important;
    color: black !important;
}
"""

header_styles = """
    .st-key-dashboard-container {
        padding: 20px;
        max-width: 1600px;
        margin: 0 auto;
        display:flex;
        align-item:center;
        justify-content:center;
    }

    .dashboard-header {
        text-align: center;
        margin-bottom: 30px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(148, 163, 184, 0.2);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);;
    }

    .dashboard-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 10px;
    }

    .dashboard-title span {
        background: linear-gradient(45deg, #3b82f6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .stock-symbol {
        font-size: 1.5rem;
        color: #3b82f6;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .dashboard-subtitle {
        color: #64748b;
        font-size: 1.1rem;
    }    

"""

kpi_styles = """
        .st-key-kpi-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        [class *= "st-key-kpi-card"] {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        }

        [class *= "st-key-kpi-card"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #3b82f6, #06b6d4);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        [class *= "st-key-kpi-card"]:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(59, 130, 246, 0.15);
        }

        [class *= "st-key-kpi-card"]:hover::before {
            opacity: 1;
        }

        .kpi-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .kpi-title {
            font-size: 0.9rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }

        .kpi-icon {
            width: 24px;
            height: 24px;
            opacity: 0.7;
            color: #3b82f6;
        }

        .kpi-value {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 10px;
            color: #1e293b;
            animation: fadeInUp 0.6s ease;
        }

        .kpi-change {
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 5px;
            font-weight: 500;
        }

        .positive { color: #16a34a; }
        .negative { color: #dc2626; }
        .neutral { color: #64748b; }


"""

chart_styles = """
        .st-key-charts-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(400px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }

        [class *= "st-key-chart-card"] {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        }

        [class *= "st-key-chart-card"]:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .chart-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 20px;
            color: #1e293b;
        }

        [class *= "st-key-chart-container"] {
            position: relative;
            min-height:300px;
            height: fit-content;
            overflow: hidden;
            border-radius: 8px;
            background: rgba(248, 250, 252, 0.5);
        }

        /* New stImage div styling - contains all the main styling */
        .stImage {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            transition: all 0.3s ease;
            filter: brightness(1.05) contrast(1.1);
            overflow: hidden;
            position: relative;
        }

        /* stImageChild - wrapper for img */
        .stImage div {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Simplified img styling */
        .stImage div img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
        }

        .st-key-chart-card-1 {
            grid-column: span 2;
        }
        .st-key-chart-card-1 .st-key-chart-container-1 {
            min-height: 400px;
            height: fit-content;
        }
        

"""

styles = f"""
    <style> 
    {remove_header_footer}
    {page_setup} 
    {header_styles}  
    {kpi_styles}
    {chart_styles}
    </style>
"""
@st.cache_data
def load_data(CURRENT_DATA_FILE):
    return pd.read_csv(CURRENT_DATA_FILE)


def dashboard():
    st.markdown(styles,unsafe_allow_html=True)
    st.set_page_config(
        page_title="Stock Market Analysis",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    DATA_NAME = st.session_state["current_stock"]
    DATA_SET_FILE = st.session_state["current_stock_file_path"]
    raw_data = load_data(DATA_SET_FILE)
    data = clean_data(raw_data)
    data = eda(data)

    with st.container(key = "dashboard-container"):

        st.markdown(f"""
            <div class="dashboard-header">
                <h1 class="dashboard-title">Stock Analysis <span> Dashboard </span></h1>
                <div class="stock-symbol">{DATA_NAME}</div>
            </div>
        """,unsafe_allow_html=True)

    with st.container(key = "kpi-grid"):
        current_values = find_current_values(data)
        with st.container(key = "kpi-card-1"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">Current Price</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
                        <path d="M2 17l10 5 10-5"></path>
                        <path d="M2 12l10 5 10-5"></path>
                    </svg>
                </div>
                <div class="kpi-value">₹{current_values[1]}</div>
                <div class="kpi-change positive">
                    <span>↗</span> +$2.45 (1.36%)
                </div>
            """,unsafe_allow_html=True)

        with st.container(key = "kpi-card-2"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">Daily Volume</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                        <path d="M18 17V9"></path>
                        <path d="M13 17V5"></path>
                        <path d="M8 17v-3"></path>
                    </svg>
                </div>
                <div class="kpi-value">{find_mean_volume(data)}</div>
                <div class="kpi-change positive">
                    <span>↗</span> +12.5% vs avg volume
                </div>
            """,unsafe_allow_html=True)

        with st.container(key = "kpi-card-3"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">All Time High</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M16 7h6v6"></path>
                        <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                    </svg>
                </div>
                <div class="kpi-value">₹{find_highest_price_stock_data(data)[0]}</div>
                <div class="kpi-change negative">
                </div>
            """,unsafe_allow_html=True)
        
        with st.container(key = "kpi-card-4"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">Day Range</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"></path>
                    </svg>
                </div>
                <div class="kpi-value">₹{current_values[0]} - ₹{current_values[1]}</div>
                <div class="kpi-change neutral">
                    <span>→</span> 1.89% range
                </div>
            """,unsafe_allow_html=True)

        with st.container(key = "kpi-card-5"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">EMA 10</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                        <line x1="9" y1="9" x2="9.01" y2="9"></line>
                        <line x1="15" y1="9" x2="15.01" y2="9"></line>
                    </svg>
                </div>
                <div class="kpi-value">₹{round(current_values[2],3)}</div>
                <div class="kpi-change positive">
                    <span>↗</span> Above EMA
                </div>
            """,unsafe_allow_html=True)

        with st.container(key = "kpi-card-6"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">SMA 9 EMA</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 9V5a3 3 0 0 0-6 0v4"></path>
                        <rect x="2" y="9" width="20" height="11" rx="2" ry="2"></rect>
                    </svg>
                </div>
                <div class="kpi-value">₹{round(current_values[3],3)}</div>
                <div class="kpi-change positive">
                    <span>↗</span> Bullish
                </div>
            """,unsafe_allow_html=True)
        
        with st.container(key = "kpi-card-7"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">Volatility</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 1v6l4-4M8 5l4 4 4-4"></path>
                        <path d="M12 23v-6l4 4M8 19l4-4 4 4"></path>
                    </svg>
                </div>
                <div class="kpi-value">{round(find_volatility_of_stock(data),3)}%</div>
                <div class="kpi-change neutral">
                    <span>→</span> Medium volatility
                </div>
            """,unsafe_allow_html=True)

        with st.container(key = "kpi-card-8"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">Trend Signal</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
                    </svg>
                </div>
                <div class="kpi-value">{trand_analysis(data)}</div>
                <div class="kpi-change positive">
                    <span>→</span> Strong signal
                </div>
            """,unsafe_allow_html=True)
        gap_values = gap_analysis(data)
        signal = ""
        if(gap_values[1] == "Gap Up"):
            signal = "positive"
        elif(gap_values[1] == "Gap Down"):
            signal = "negative"
        with st.container(key = "kpi-card-9"):
            st.markdown(f"""
                <div class="kpi-header">
                    <span class="kpi-title">Gap Analysis</span>
                    <svg class="kpi-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="3"></circle>
                        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1 1.51V6a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                    </svg>
                </div>
                <div class="kpi-value">{round(gap_values[0],3)}</div>
                <div class="kpi-change {signal}">
                    <span>↗</span> {gap_values[1]}
                </div>
            """,unsafe_allow_html=True)
        
    with st.container(key = "charts-grid"):

        with st.container(key = "chart-card-1"):
            st.markdown("""<h3 class="chart-title">OHLC Price Chart with Moving Averages</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-1"):
                st.pyplot(OHLC_moving_average_graph(data))
        
        with st.container(key = "chart-card-2"):
            st.markdown("""<h3 class="chart-title">Volume Analysis</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-2"):
                st.pyplot(volume_analysis_graph(data))

        

        with st.container(key = "chart-card-4"):
            st.markdown("""<h3 class="chart-title">Trading Signal Distribution</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-4"):
                st.pyplot(trend_analysis_graph(data))
        
        with st.container(key = "chart-card-5"):
            st.markdown("""<h3 class="chart-title">Overall Price Trend</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-5"):
                st.pyplot(overall_price_trend(data))

        with st.container(key = "chart-card-6"):
            st.markdown("""<h3 class="chart-title">Volume Distribution by Range</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-6"):
                st.pyplot(volume_distribution_by_range(data))

        with st.container(key = "chart-card-7"):
            st.markdown("""<h3 class="chart-title">Boxplot of Daily Closing Prices</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-7"):
                st.pyplot(boxplot_close_price(data))
        
        with st.container(key = "chart-card-8"):
            st.markdown("""<h3 class="chart-title">KDE of Close Price and Volume with Skewness</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-8"):
                st.pyplot(skewness_of_close(data))

        with st.container(key = "chart-card-3"):
            st.markdown("""<h3 class="chart-title">KDE of Volume with Skewness</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-3"):
                st.pyplot(skewness_of_volume(data))

        with st.container(key = "chart-card-9"):
            st.markdown("""<h3 class="chart-title">Corelation Analysis</h3>""",unsafe_allow_html=True)
            with st.container(key = "chart-container-9"):
                st.pyplot(corelation_analysis(data))

        