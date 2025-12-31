import streamlit as st
import pandas as pd
import plotly.express as px

# --- 설정 및 제목 ---
st.set_page_config(page_title="LG화학 전략 진입 상황실", layout="wide")

# 전략적 슬로건 (모든 부서 인지용)
st.markdown("""
    <div style="background-color:#800000;padding:15px;border-radius:10px">
    <h2 style="color:white;text-align:center;margin:0;">🚩 전략 목표: LG화학 신규 진입 및 Vendor 등록 완수</h2>
    <p style="color:white;text-align:center;margin:5px;">"이번 프로젝트의 완벽한 수행은 향후 LG화학 전 사업장 SCR 촉매 교체 물량 선점의 시작입니다."</p>
    </div>
    """, unsafe_allow_html=True)

st.title("") # 간격 조절
st.error("📅 견적 및 서류 제출 마감: 2026년 1월 16일 (오후 5시 한도)")

# 1. 전략적 중요성 분석 (영업팀/전사 공유)
col_strat, col_spec = st.columns([1, 1])

with col_strat:
    st.subheader("💡 프로젝트의 전략적 가치")
    st.write("1. **First-Step:** 대영씨엔이 최초 LG화학 대형 프로젝트 진입")
    st.write("2. **Future Value:** NCC2공장 성공 시, 여수/대산 전체 사업장 확대 기회")
    st.write("3. **Brand Image:** 에틸렌 분해로(NCC) 레퍼런스 확보 시 해외 시장 경쟁력 확보")

with col_spec:
    st.subheader("🎯 핵심 성공 요인 (Critical Success Factors)")
    st.write("- **기술력 증명:** 크롬/중금속 내독성 4년 보증 (연구소)")
    st.write("- **실적 완벽 대응:** NCC 2회 이상 연속 공급 실적 증명 (영업)")
    st.write("- **신뢰도 구축:** 신용평가서 및 회사소개서 최신화 제출 (영업/구매)")

st.divider()

# 2. 부서별 관리 탭
tabs = st.tabs(["💰 영업/전략", "📐 설계/엔지니어링", "🔬 연구/기술", "✅ 품질/생산"])

with tabs[0]: # 영업/전략 탭
    st.subheader("💼 LG화학 파트너십 구축 전략")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**[영업 핵심 과제]**")
        st.checkbox("이승호 책임(설비구매팀) 밀착 대응", value=True)
        st.checkbox("LG화학 전용 벤더 등록 서류(신용/소개서) 준비", value=False)
        st.checkbox("타사(경쟁사) 동향 파악 및 차별화 전략 수립", value=False)
    with c2:
        st.write("**[미래 로드맵]**")
        roadmap = pd.DataFrame({
            "단계": ["'26 상반기", "'27 보수", "'28 이후"],
            "목표": ["NCC2 수주", "성공적 교체", "LG화학 전사 확대"],
            "상태": ["진행중", "대기", "잠재기회"]
        })
        st.table(roadmap)

with tabs[1]: # 설계팀
    st.subheader("📐 설계 안정성: "수직형(Vertical) HRSG" 완벽 대응")
    st.info("LG화학의 까다로운 설비 구조 내에서 최적의 기계적 안정성(Support/Sealing)을 증명해야 합니다.")
    st.write("- **YEO 도면 분석:** Sealing Detail 최적화하여 Leakage 제로 달성")
    st.write("- **Monorail 검토:** 보수 시 교체 용이성 강조 (고객사 관리 포인트)")

with tabs[2]: # 연구소
    st.subheader("🔬 기술 격차 확인: 중금속 내독성 4년 보증")
    st.warning("단순 효율이 아니라 '독성 물질(Cr)에 대한 방어력'이 수주를 결정짓는 핵심입니다.")
    chart_data = pd.DataFrame({
        "시간(년)": [1, 2, 3, 4],
        "경쟁사 예측": [98, 90, 82, 75],
        "대영 최적화 안": [99, 97, 95, 93]
    })
    st.plotly_chart(px.line(chart_data, x="시간(년)", y=["경쟁사 예측", "대영 최적화 안"], title="내독성 유지 시뮬레이션"), use_container_width=True)

with tabs[3]: # 품질/구매
    st.subheader("💎 품질 신뢰성 및 구매 경쟁력")
    st.write("- **품질:** LG화학의 높은 검사 기준을 상회하는 QA/QC 리포트 준비")
    st.write("- **구매:** 원재료 수급 안정성 확보를 통한 단가 경쟁력 및 납기 보장")

st.caption("※ 본 대시보드는 LG화학 최초 진입을 위한 전사적 협업 툴입니다.")
