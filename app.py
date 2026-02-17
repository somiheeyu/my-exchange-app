import streamlit as st
import yfinance as yf
from datetime import datetime
import pytz
import time

# 1. 페이지 설정 (브라우저 탭 이름 및 레이아웃)
st.set_page_config(page_title="Global Exchange Monitor", layout="wide")

# 2. 스타일 설정 (글자 크기 및 배경색)
st.markdown("""
    <style>
    .main { background-color: #121212; }
    .stApp { background-color: #121212; }
    .price-text { font-size: 150px !important; font-weight: bold; color: #f1c40f; text-align: center; line-height: 1.2; }
    .title-text { font-size: 40px; color: #bdc3c7; text-align: center; padding-top: 30px; }
    .clock-text { font-size: 35px; color: #ecf0f1; text-align: center; font-weight: bold; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# 3. 화면에 표시될 구역 설정
title_placeholder = st.empty()
price_placeholder = st.empty()
clock_placeholder = st.empty()

# 4. 실시간 업데이트 로직
# st.empty()를 사용하여 화면 전체를 새로고침하지 않고 숫자만 쏙 바꿉니다.
while True:
    try:
        # 환율 데이터 가져오기
        ticker = yf.Ticker("USDKRW=X")
        current_price = ticker.fast_info['last_price']
        
        # 시간 설정 (서울, 플로리다)
        kor_tz = pytz.timezone('Asia/Seoul')
        usa_tz = pytz.timezone('US/Eastern')
        now_kor = datetime.now(kor_tz).strftime("%H:%M:%S")
        now_usa = datetime.now(usa_tz).strftime("%H:%M:%S")

        # 화면 업데이트
        title_placeholder.markdown('<p class="title-text">USD / KRW Realtime</p>', unsafe_allow_html=True)
        price_placeholder.markdown(f'<p class="price-text">{current_price:,.2f}</p>', unsafe_allow_html=True)
        clock_placeholder.markdown(f'<p class="clock-text">서울 : {now_kor}  |  플로리다 : {now_usa}</p>', unsafe_allow_html=True)
        
    except Exception as e:
        # 오류 발생 시 화면에 표시하지 않고 조용히 재시도
        pass
    
    # 5초 쉬었다가 다시 실행 (서버 부하 방지)
    time.sleep(5)
