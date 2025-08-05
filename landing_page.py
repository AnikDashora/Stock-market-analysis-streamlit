import streamlit as st
from data_funtions import set_stock_data_file

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
}

/* Optional: to set sidebar background and text colors */
[data-testid="stSidebar"] {
    background-color: white !important;
    color: black !important;
}
"""

# main page styling
parent_div_styles = """
.st-key-parent-flex-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 48px;
  max-width: 1400px;
  margin: 20px auto 0 auto;
  min-height: 100vh;
  padding: 0 20px;
}

@media (max-width: 1100px) {
  .st-key-parent-flex-row {
    flex-direction: column;
    gap: 60px;
    align-items: center;
  }
  .st-key-features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
"""

left_section_styles = """
.st-key-left-section {
  flex: 1 1 55%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 42px;
  min-width: 0;
  justify-content: flex-start;
}
"""

badge_styles = """
.analytics-badge {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 32px;
  background: linear-gradient(135deg, #e7eafc 0%, #e8f0ff 60%, #f0f7ff 100%);
  color: #2151e1;
  border: 2px solid rgba(177, 202, 246, 0.6);
  border-radius: 999px;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 20px;
  box-shadow: 0 4px 20px rgba(33, 81, 225, 0.12);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  animation: badgeAnimation 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s both;
  z-index: 1;
}

.analytics-badge:hover {
  transform: translateY(-4px) scale(1.05);
  box-shadow: 0 12px 35px rgba(33, 81, 225, 0.22);
}
"""

animations = """
@keyframes badgeAnimation {
  0% { 
    opacity: 0; 
    transform: translateX(-60px) scale(0.8);
  }
  100% { 
    opacity: 1; 
    transform: translateX(0) scale(1);
  }
}

@keyframes titleAnimation {
  0% { 
    opacity: 0; 
    transform: translateX(-40px) translateY(20px) scale(0.95);
    z-index: -1;
  }
  100% { 
    opacity: 1; 
    transform: translateX(0) translateY(0) scale(1);
    z-index: 1;
  }
}

@keyframes featureCardAnimation {
  0% { 
    opacity: 0; 
    transform: scale(0.8);
  }
  100% { 
    opacity: 1; 
    transform: scale(1);
  }
}

@keyframes stockCardAnimation {
  0% { 
    opacity: 0; 
    transform: translateX(60px) scale(0.8);
  }
  100% { 
    opacity: 1; 
    transform: translateX(0) scale(1);
  }
}

@keyframes gradientShift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes wave {
  0%, 100% { transform: scaleY(1); }
  25% { transform: scaleY(0.4); }
  50% { transform: scaleY(0.9); }
  75% { transform: scaleY(0.6); }
}
"""

title_and_subtitle_styles = """
.hero-title {
  font-size: 3.5rem;
  font-weight: 900;
  line-height: 1.05;
  margin-bottom: 12px;
  color: #1c2536;
  letter-spacing: -0.02em;
  animation: titleAnimation 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.4s both;
  z-index: 1;
}

.hero-title .gradient-text {
  background: linear-gradient(135deg, #2151e1 0%, #4694fe 50%, #6366f1 100%);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  background-size: 200% 200%;
  animation: gradientShift 3s ease-in-out infinite;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #4a5568;
  margin-bottom: 32px;
  line-height: 1.6;
  max-width: 520px;
  font-weight: 400;
  animation: titleAnimation 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.6s both;
  z-index: 1;
}
"""

feature_card_styles = """
.st-key-features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-top: 12px;
  margin-bottom: 16px;
  width: 100%;
}

.feature-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  padding: 20px 18px;
  border-radius: 16px;
  border: 1px solid rgba(212, 219, 231, 0.6);
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
  animation: featureCardAnimation 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

.feature-card:nth-child(1) { animation-delay: 0.8s; }
.feature-card:nth-child(2) { animation-delay: 0.9s; }
.feature-card:nth-child(3) { animation-delay: 1.0s; }
.feature-card:nth-child(4) { animation-delay: 1.1s; }
.feature-card:nth-child(5) { animation-delay: 1.2s; }
.feature-card:nth-child(6) { animation-delay: 1.3s; }

.feature-card:hover {
  transform: translateY(-6px) scale(1.02);
  box-shadow: 0 16px 45px rgba(33, 81, 225, 0.18);
  border-color: rgba(33, 81, 225, 0.3);
}

.icon-wrapper {
  background: linear-gradient(135deg, #e9f2fc 0%, #f0f8ff 100%);
  color: #2151e1;
  border-radius: 12px;
  padding: 12px;
  min-width: 38px;
  min-height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.feature-card:hover .icon-wrapper {
  transform: scale(1.15);
}

.feature-title {
  font-size: 16px;
  font-weight: 700;
  color: #1e2331;
  margin-bottom: 2px;
}

.feature-desc {
  font-size: 13px;
  color: #6b7280;
  font-weight: 500;
}
"""

right_section_style = """
.st-key-right-stock-cards {
  flex: 1 1 45%;
  position: relative;
  min-width: 320px;
  height: 800px;
  display: flex;
  align-items: center;
}
"""

stock_cards_styles = """
.st-key-visual-stack {
  width: auto;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 30px;
  z-index: 2;
  padding: 20px;
  box-sizing: border-box;
  margin-left: auto;
}

.stock-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  border: 2px solid rgba(229, 231, 235, 0.8);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(72, 91, 164, 0.12), 0 4px 12px rgba(19, 23, 49, 0.06);
  padding: 20px 16px;
  width: 220px;
  flex: 1;
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  position: relative;
  overflow: hidden;
  margin: 0;
  min-height: 140px;
  animation: stockCardAnimation 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

.stock-card:nth-child(1) { animation-delay: 0.8s; }
.stock-card:nth-child(2) { animation-delay: 0.9s; }
.stock-card:nth-child(3) { animation-delay: 1.0s; }
.stock-card:nth-child(4) { animation-delay: 1.1s; }

.stock-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  transition: left 0.6s ease;
}

.stock-card:hover::before {
  left: 100%;
}

.stock-card:hover {
  transform: translateY(-8px) scale(1.03);
  box-shadow: 0 20px 60px rgba(29, 49, 110, 0.22), 0 12px 25px rgba(19, 23, 49, 0.1);
  border-color: rgba(33, 81, 225, 0.4);
}

.card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 16px;
}

.card-stock-main {
  display: flex;
  flex-direction: column;
}

.card-symbol {
  font-size: 1.1rem;
  font-weight: 800;
  color: #1941bc;
  margin-bottom: 2px;
}

.card-meta {
  font-size: 0.8rem;
  color: #8991a1;
  font-weight: 500;
}

.card-price {
  text-align: right;
  font-size: 1.2rem;
  font-weight: 700;
  color: #1e2331;
  margin-bottom: 4px;
}

.card-changes {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.9rem;
  font-weight: 600;
  justify-content: flex-end;
}

.card-bars {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 50px;
  margin-top: 16px;
  overflow: hidden;
}

.card-bar {
  border-radius: 4px 4px 0 0;
  transition: all 0.3s ease;
  animation: wave 3.5s ease-in-out infinite;
  transform-origin: bottom;
  opacity: 0.5;
}

.card-bar-green {
  background: linear-gradient(180deg, #22c55e 0%, rgba(34, 197, 94, 0.4) 100%);
}

.card-bar-red {
  background: linear-gradient(180deg, #ef4444 0%, rgba(239, 68, 68, 0.4) 100%);
}

.card-bar:nth-child(1) { animation-delay: 0s; }
.card-bar:nth-child(2) { animation-delay: 0.4s; }
.card-bar:nth-child(3) { animation-delay: 0.8s; }
.card-bar:nth-child(4) { animation-delay: 1.2s; }
.card-bar:nth-child(5) { animation-delay: 1.6s; }
.card-bar:nth-child(6) { animation-delay: 2.0s; }
.card-bar:nth-child(7) { animation-delay: 2.4s; }
.card-bar:nth-child(8) { animation-delay: 2.8s; }

.stock-card:hover .card-bar {
  animation-duration: 2.5s;
}

@media (max-width: 1100px) {
  .st-key-right-stock-cards {
    min-width: 100%;
    height: auto;
  }
  .st-key-visual-stack {
    position: relative;
    right: auto;
    top: auto;
    transform: none;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    height: auto;
  }
  .stock-card {
    min-width: 220px;
    width: 220px;
    height: 140px;
    flex: 1 1 300px;
    margin: 0;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.8rem;
  }
  .st-key-parent-flex-row {
    padding: 0 16px;
    gap: 40px;
  }
  .st-key-features-grid {
    grid-template-columns: 1fr;
  }
  .st-key-visual-stack {
    flex-direction: column;
    align-items: center;
  }
}
"""

stock_select_parent_box_styles = """
    .st-key-stock-select-parent-box{
        padding:20px 40px;
        display:flex;
        flex-wrap:wrap;
        justify-content:center;
        margin:40px 0 0 auto;
    }
"""

stock_select_box_styles = """
    .st-key-stock-select-box {
        width:100%;
        max-width: 1000px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 32px;
        box-shadow: 0 6px 30px rgba(60, 80, 170, 0.12), 0 2px 8px rgba(20,40,80,0.10);
        padding:20px 40px;
        border-radius:20px;
    }
    .stock-box-heading {
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

    .stock-box-heading h2 {
        font-size: 2rem;
        font-weight: 600;
        color: #1e2331;
        margin: 0;
    }

    .stock-box-heading p {
        color: #6b7280;
        font-size: 1rem;
        margin: 0;
    }
"""

stock_text_input_section_styles = """
    .st-key-stock-text-input-section-1,
    .st-key-stock-text-input-section-2,
    .st-key-stock-text-input-section-3{
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    .stock-text-input-heading {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .stock-text-input-heading svg {
        width: 20px;
        height: 20px;
        color: #2151e1;
    }

    .stock-text-input-heading h3 {
        font-size: 1.125rem;
        font-weight: 500;
        color: #1e2331;
        margin: 0;
    }

    .st-key-search-form{
        display: flex;
        gap: 12px;
    }

    .st-key-search_input{
        flex: 1;
    }
    div[data-baseweb="input"]{
        border:none;
        height: 48px;
        width:100%;
        border-radius: 21px;
    }

    input[type="text"] {
        width: 100% !important;
        height: 48px;
        padding: 0 16px;
        border: 2px solid rgba(229, 231, 235);
        border-radius: 20px;
        font-size: 1rem;
        background: rgba(255, 255, 255);
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(33, 81, 225, 0.08);
        color: #111827;
    }

    input[type="text"]:focus {
        border-color: #2151e1;
        box-shadow: 0 6px 24px rgba(33, 81, 225, 0.2);
        background: rgba(255, 255, 255);
    }

    input[type="text"]::placeholder {
        color: #9ca3af;
        font-weight: 500;
    }
    button[kind="secondary"]{
        width:100%;
    }
    .st-key-search-form button[kind="secondary"]{
        height: 48px;
        padding: 0 24px;
        background: linear-gradient(135deg, #2151e1 0%, #4694fe 50%, #6366f1 100%);
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(33, 81, 225, 0.25);
        white-space: nowrap;
    }
    
"""

stock_option_button_style = """
    [class *= "st-key-stock-grid-"] button[kind="secondary"]    {
        padding: 16px;
        border-radius: 8px;
        border: 2px solid rgba(229, 231, 235, 0.8);
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        transition: all 0.2s ease;
        text-align: center;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    [class *= "st-key-stock-grid-"] button[kind="secondary"]:hover {
        transform: translateY(-1px) scale(1.02);
        border-color: rgba(33, 81, 225, 0.5);
        background: linear-gradient(135deg, #2151e1 0%, #4694fe 50%, #6366f1 100%);
        box-shadow: 0 8px 20px rgba(33, 81, 225, 0.4);
        color:white;
    }
"""

styles = f"""
<style>
{remove_header_footer}
{page_setup}
{parent_div_styles}
{left_section_styles}
{badge_styles}
{title_and_subtitle_styles}
{feature_card_styles}
{right_section_style}
{stock_cards_styles}
{animations}
{stock_select_parent_box_styles}
{stock_select_box_styles}
{stock_text_input_section_styles}
{stock_option_button_style}
</style>
"""


def landingpage():
    st.set_page_config(
        page_title="Stock Market Analysis",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(styles, unsafe_allow_html=True)
    with st.container(key = "parent-flex-row"):
        left_section,right_section = st.columns(2)
        with left_section:
            with st.container(key = "left-section"):
                st.markdown("""
                <div class="analytics-badge">
                    <svg width="30" height="25" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle;">
                        <path d="M16 7h6v6"></path>
                        <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                    </svg>
                    <span>DATA-Powered Analytics</span>
                </div>
                """,unsafe_allow_html=True)
                st.markdown("""
                    <div>
                        <div class="hero-title">
                            Smart Stock<br>
                            <span class="gradient-text">Market Analysis</span>
                        </div>
                        <div class="hero-subtitle">
                            Harness the power of advanced algorithms and real-time data to make informed investment decisions with confidence and precision.
                        </div>
                    </div>
                """,unsafe_allow_html=True)
                
                with st.container(key = "features-grid"):
                    st.markdown("""
                        <div class="feature-card">
                            <div class="icon-wrapper">
                                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                                    <path d="M18 17V9"></path>
                                    <path d="M13 17V5"></path>
                                    <path d="M8 17v-3"></path>
                                </svg>
                            </div>
                            <div>
                                <div class="feature-title">Real-time Data</div>
                                <div class="feature-desc">Live market feeds</div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="feature-card">
                            <div class="icon-wrapper">
                                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                                    <path d="M18 17V9"></path>
                                    <path d="M13 17V5"></path>
                                    <path d="M8 17v-3"></path>
                                </svg>
                            </div>
                            <div>
                                <div class="feature-title">Real-time Data</div>
                                <div class="feature-desc">Live market feeds</div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="feature-card">
                            <div class="icon-wrapper">
                                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                                    <path d="M18 17V9"></path>
                                    <path d="M13 17V5"></path>
                                    <path d="M8 17v-3"></path>
                                </svg>
                            </div>
                            <div>
                                <div class="feature-title">Real-time Data</div>
                                <div class="feature-desc">Live market feeds</div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="feature-card">
                            <div class="icon-wrapper">
                                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                                    <path d="M18 17V9"></path>
                                    <path d="M13 17V5"></path>
                                    <path d="M8 17v-3"></path>
                                </svg>
                            </div>
                            <div>
                                <div class="feature-title">Real-time Data</div>
                                <div class="feature-desc">Live market feeds</div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="feature-card">
                            <div class="icon-wrapper">
                                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                                    <path d="M18 17V9"></path>
                                    <path d="M13 17V5"></path>
                                    <path d="M8 17v-3"></path>
                                </svg>
                            </div>
                            <div>
                                <div class="feature-title">Real-time Data</div>
                                <div class="feature-desc">Live market feeds</div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                    <div class="feature-card">
                        <div class="icon-wrapper">
                            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M3 3v16a2 2 0 0 0 2 2h16"></path>
                                <path d="M18 17V9"></path>
                                <path d="M13 17V5"></path>
                                <path d="M8 17v-3"></path>
                            </svg>
                        </div>
                        <div>
                            <div class="feature-title">Real-time Data</div>
                            <div class="feature-desc">Live market feeds</div>
                        </div>
                    </div>
                """,unsafe_allow_html=True)
        with right_section:
            with st.container(key = "right-stock-cards"):
                with st.container(key = "visual-stack"):
                    st.markdown("""
                        <div class="stock-card">
                            <div class="card-head">
                                <div class="card-stock-main">
                                    <div class="card-symbol">AAPL</div>
                                    <div class="card-meta">Vol: 2.5M</div>
                                </div>
                                <div>
                                    <div class="card-price">$175.23</div>
                                    <div class="card-changes" style="color:#18b153;">
                                        <svg width="25" height="25" fill="none" stroke="#18b153" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M16 7h6v6"></path>
                                            <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                                        </svg>
                                        +2.34%
                                    </div>
                                </div>
                            </div>
                            <div class="card-bars">
                                <div class="card-bar card-bar-green" style="width:8px;height:15px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:28px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:35px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:22px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:18px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:32px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:25px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:12px;"></div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="stock-card">
                            <div class="card-head">
                                <div class="card-stock-main">
                                    <div class="card-symbol">AAPL</div>
                                    <div class="card-meta">Vol: 2.5M</div>
                                </div>
                                <div>
                                    <div class="card-price">$175.23</div>
                                    <div class="card-changes" style="color:#18b153;">
                                        <svg width="25" height="25" fill="none" stroke="#18b153" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M16 7h6v6"></path>
                                            <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                                        </svg>
                                        +2.34%
                                    </div>
                                </div>
                            </div>
                            <div class="card-bars">
                                <div class="card-bar card-bar-green" style="width:8px;height:15px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:28px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:35px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:22px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:18px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:32px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:25px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:12px;"></div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="stock-card">
                            <div class="card-head">
                                <div class="card-stock-main">
                                    <div class="card-symbol">AAPL</div>
                                    <div class="card-meta">Vol: 2.5M</div>
                                </div>
                                <div>
                                    <div class="card-price">$175.23</div>
                                    <div class="card-changes" style="color:#18b153;">
                                        <svg width="25" height="25" fill="none" stroke="#18b153" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M16 7h6v6"></path>
                                            <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                                        </svg>
                                        +2.34%
                                    </div>
                                </div>
                            </div>
                            <div class="card-bars">
                                <div class="card-bar card-bar-green" style="width:8px;height:15px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:28px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:35px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:22px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:18px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:32px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:25px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:12px;"></div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
                    st.markdown("""
                        <div class="stock-card">
                            <div class="card-head">
                                <div class="card-stock-main">
                                    <div class="card-symbol">AAPL</div>
                                    <div class="card-meta">Vol: 2.5M</div>
                                </div>
                                <div>
                                    <div class="card-price">$175.23</div>
                                    <div class="card-changes" style="color:#18b153;">
                                        <svg width="25" height="25" fill="none" stroke="#18b153" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M16 7h6v6"></path>
                                            <path d="m22 7-8.5 8.5-5-5L2 17"></path>
                                        </svg>
                                        +2.34%
                                    </div>
                                </div>
                            </div>
                            <div class="card-bars">
                                <div class="card-bar card-bar-green" style="width:8px;height:15px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:28px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:35px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:22px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:18px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:32px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:25px;"></div>
                                <div class="card-bar card-bar-green" style="width:8px;height:12px;"></div>
                            </div>
                        </div>
                    """,unsafe_allow_html=True)
    
    with st.container(key = "stock-select-parent-box"):
        with st.container(key = "stock-select-box"):
            st.markdown("""
                <div class="stock-box-heading">
                    <h2>Select Stock to Analyze</h2>
                    <p>Choose from popular stocks or enter your own custom symbol</p>
                </div>
            """,unsafe_allow_html=True)

            # with st.container(key = "stock-text-input-section-1"):
                # st.markdown("""
                #     <div class="stock-text-input-heading">
                #         <svg  width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                #             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m21 21-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                #         </svg>
                #         <h3>Search Stock Symbol</h3>
                #     </div>
                # """,unsafe_allow_html=True)
                # with st.container(key = "search-form"):
                #     search_bar_col,search_button_col = st.columns([4,1])
                #     with search_bar_col:
                #         st.text_input(
                #             label="search",
                #             placeholder="Search",
                #             key="search_input",
                #             label_visibility="collapsed"
                #         )
                #     with search_button_col:
                #         st.button(
                #             label="select",
                #             key = "search-btn",
                #             type="secondary",
                #             use_container_width=True
                #         )

            with st.container(key = "stock-text-input-section-2"):
                st.markdown("""
                    <div class="stock-text-input-heading">
                        <svg  width="16" height="16" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                        </svg>
                        <h3>Popular Stocks</h3>
                    </div>
                """,unsafe_allow_html=True)
                with st.container(key = "stock-grid-1"):
                    popular_stock = ["RELIANCE","HDFCBANK","TCS","ICICIBANK"]
                    popular_stock_button = st.columns(4)
                    with popular_stock_button[0]:
                        st.button(
                            label = f"{popular_stock[0]}",
                            type="secondary",
                            key = "stock-card-1",
                            on_click=set_stock_data_file,
                            args=(popular_stock[0],)
                        )
                    with popular_stock_button[1]:
                        st.button(
                            label = f"{popular_stock[1]}",
                            type="secondary",
                            key = "stock-card-2",
                            on_click=set_stock_data_file,
                            args=(popular_stock[1],)
                        )
                    with popular_stock_button[2]:
                        st.button(
                            label = f"{popular_stock[2]}",
                            type="secondary",
                            key = "stock-card-3",
                            on_click=set_stock_data_file,
                            args=(popular_stock[2],)
                        )
                    with popular_stock_button[3]:
                        st.button(
                            label = f"{popular_stock[3]}",
                            type="secondary",
                            key = "stock-card-4",
                            on_click=set_stock_data_file,
                            args=(popular_stock[3],)
                        )

            with st.container(key = "stock-text-input-section-3"):
                st.markdown("""
                    <div class="stock-text-input-heading">
                        <svg  width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                        </svg>
                        <h3>More Options</h3>
                    </div>
                """,unsafe_allow_html=True)
                with st.container(key = "stock-grid-2"):
                    more_option_stock = ["INFY","SBIN","LICI","HINDUNILVR"]
                    more_option_stock_button = st.columns(4)
                    with more_option_stock_button[0]:
                        st.button(
                            label = f"{more_option_stock[0]}",
                            type="secondary",
                            key = "stock-card-5",
                            on_click=set_stock_data_file,
                            args=(more_option_stock[0],)
                        )
                    with more_option_stock_button[1]:
                        st.button(
                            label = f"{more_option_stock[1]}",
                            type="secondary",
                            key = "stock-card-6",
                            on_click=set_stock_data_file,
                            args=(more_option_stock[1],)
                        )
                    with more_option_stock_button[2]:
                        st.button(
                            label = f"{more_option_stock[2]}",
                            type="secondary",
                            key = "stock-card-7",
                            on_click=set_stock_data_file,
                            args=(more_option_stock[2],)
                        )
                    with more_option_stock_button[3]:
                        st.button(
                            label = f"{more_option_stock[3]}",
                            type="secondary",
                            key = "stock-card-8",
                            on_click=set_stock_data_file,
                            args=(more_option_stock[3],)
                        )                

