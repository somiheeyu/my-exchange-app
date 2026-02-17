import streamlit as st
import yfinance as yf
from datetime import datetime
import pytz
import time

# 1. 페이지 설정
st.set_page_config(page_title="Exchange Monitor", layout="wide")

# 2. 스타일 설정 (시계 크기를 100px로 대폭 확대)
st.markdown("""
    <style>
    .main { background-color: #121212; }
    .stApp { background-color: #121212; }
    /* 환율 숫자 스타일 */
    .price-text { font-size: 180px !important; font-weight: bold; color: #f1c40f; text-align: center; line-height: 1.1; margin-top: -30px; }
    /* 제목 스타일 */
    .title-text { font-size: 45px; color: #bdc3c7; text-align: center; padding-top: 20px; font-weight: bold; }
    /* 시계 스타일 - 크기를 100px로 키우고 형광색 계열로 변경하여 가시성 확보 */
    .clock-text { font-size: 80px !important; color: #00FF41; text-align: center; font-weight: bold; font-family: 'Courier New', monospace; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. 화면 구역 설정
title_placeholder = st.empty()
price_placeholder = st.empty()
clock_placeholder = st.empty()

while True:
    try:
        # 환율 데이터 수집
        ticker = yf.Ticker("USDKRW=X")
        current_price = ticker.fast_info['last_price']
        
        # 시간 설정
        kor_tz = pytz.timezone('Asia/Seoul')
        usa_tz = pytz.timezone('US/Eastern')
        now_kor = datetime.now(kor_tz).strftime("%H:%M:%S")
        now_usa = datetime.now(usa_tz).strftime("%H:%M:%S")

        # 화면 업데이트
        title_placeholder.markdown('<p class="title-text">USD / KRW Realtime</p>', unsafe_allow_html=True)
        price_placeholder.markdown(f'<p class="price-text">{current_price:,.2f}</p>', unsafe_allow_html=True)
        # 서울과 플로리다 시간을 더 크게 표시
        clock_placeholder.markdown(f'<p class="clock-text">SEOUL {now_kor}<br>FLORIDA {now_usa}</p>', unsafe_allow_html=True)
        
    except Exception as e:
        pass
    
    time.sleep(5)
