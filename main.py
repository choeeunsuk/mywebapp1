import streamlit as st
import random
import time

# 1. 페이지 기본 설정 (아기자기한 파비콘과 타이틀)
st.set_page_config(
    page_title="💖 뽀짝 MBTI 직업 탐험대!",
    page_icon="🌸",
    layout="centered"
)

# 2. 파스텔 톤 & 귀여운 스타일 CSS 정의
st.markdown("""
<style>
    /* 전체 배경을 연한 파스텔 핑크/크림색 톤으로 설정 */
    .stApp {
        background-color: #FFF5F7;
    }
    
    /* 카드 형태의 컨테이너 디자인 */
    .cute-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 8px 16px rgba(255, 182, 193, 0.3);
        border: 2px solid #FFD1DC;
        margin-bottom: 20px;
    }
    
    /* 메인 타이틀 스타일 */
    .main-title {
        color: #FF6B8B;
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* 서브 타이틀 스타일 */
    .sub-title {
        color: #8860D0;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    
    /* 직업 박스 Highlight */
    .job-box {
        background-color: #FFF0F5;
        border-left: 5px solid #FF6B8B;
        padding: 12px 18px;
        border-radius: 10px;
        margin: 8px 0;
        font-weight: bold;
        color: #4A4A4A;
    }
</style>
""", unsafe_allow_html=True)

# 3. MBTI 데이터베이스 (16가지 유형별 귀여운 정보)
mbti_data = {
    "INTJ": {
        "title": "🧠 용감한 전략가 냥이",
        "jobs": ["📂 데이터 아키텍트", "🤖 AI 연구원", "📈 투자 전략가", "🕹️ 게임 기획자"],
        "desc": "혼자서 완벽한 계획을 세우는 천재! 복잡한 문제를 척척 해결하는 능력이 탁월해요.",
        "cheer": "세상을 뒤흔들 당신의 멋진 플랜을 응원해요! ⚡"
    },
    "INTP": {
        "title": "🔍 호기심 가득한 아인슈타인 햄스터",
        "jobs": ["💻 소프트웨어 개발자", "🧪 물리학자", "🔮 사이버 보안 전문가", "📚 학술 연구원"],
        "desc": "새로운 이론과 아이디어의 천국! '왜 그럴까?'를 탐구할 때 가장 빛나요.",
        "cheer": "오늘도 엉뚱하지만 위대한 질문을 던져보아요! 🌟"
    },
    "ENTJ": {
        "title": "👑 카리스마 넘치는 리더 호랑이",
        "jobs": ["💼 경영 컨설턴트", "🚀 스타트업 대표", "⚖️ 변호사", "🏛️ 정책 기획자"],
        "desc": "목표가 생기면 무섭게 추진하는 대장님! 팀을 이끌어 비전을 현실로 만들어요.",
        "cheer": "당신이 가는 길이 바로 새로운 길이에요! 🦁"
    },
    "ENTP": {
        "title": "💡 아이디어 퐁퐁 토끼",
        "jobs": ["🎤 에이전시 기획자", "🎨 유튜버/크리에이터", "🧩 백엔드/프론트엔드 개발자", "📈 브랜딩 디렉터"],
        "desc": "지루한 건 절대 못 참아! 끊임없이 신선하고 참신한 아이디어를 내놓는 마법사예요.",
        "cheer": "세상을 통쾌하게 놀라게 해줄 아이디어를 기대할게요! 💥"
    },
    "INFJ": {
        "title": "🌙 따뜻한 마음의 예언자 사슴",
        "jobs": ["🩺 심리상담사", "✍️ 소설가/시인", "🏫 인권/교육 활동가", "🎨 아트 디렉터"],
        "desc": "사람들의 마음을 깊게 이해하는 따뜻한 영혼의 소유자! 세상에 온기를 더해줘요.",
        "cheer": "당신의 깊고 다정한 시선이 세상을 바꿔요 🌿"
    },
    "INFP": {
        "title": "🌈 감성 가득 몽상가 곰돌이",
        "jobs": ["📖 일러스트레이터", "🎵 작곡가/작사가", "💬 웹툰 작가", "🌿 환경 운동가"],
        "desc": "풍부한 상상력과 나만의 철학을 가진 예술가 감성! 나만의 가치를 소중히 여겨요.",
        "cheer": "당신만의 예쁜 색깔로 세상을 물들여주세요 🎨"
    },
    "ENFJ": {
        "title": "☀️ 다정한 멘토 강아지",
        "jobs": ["👩‍🏫 선생님/교수", "🤝 HR(인사) 담당자", "📢 PR/홍보 전문가", "💖 사회복지사"],
        "desc": "주변 사람들의 성장을 도울 때 최고의 행복을 느껴요! 긍정 에너지가 뿜뿜!",
        "cheer": "당신의 따뜻한 햇살 같은 미소가 모두를 행복하게 해요 ☀️"
    },
    "ENFP": {
        "title": "🎈 에너자이저 해피 쿼카",
        "jobs": ["🎪 이벤트 기획자", "🎬 영상 감독", "✈️ 여행 에세이 작가", "📢 마케터"],
        "desc": "열정과 호기심이 끝없이 샘솟는 스파크! 주변 사람들에게 즐거움을 선물해요.",
        "cheer": "오늘도 세상이라는 놀이동산에서 신나게 놀아봐요! 🎈"
    },
    "ISTJ": {
        "title": "📋 꼼꼼하고 성실한 펭귄",
        "jobs": ["📊 회계사/세무사", "🏛️ 공무원", "🗄️ Database 관리자", "🔍 품질 관리(QA) 엔지니어"],
        "desc": "약속과 질서를 가장 소중히 여기는 든든한 버팀목! 맡은 일은 100% 완수해요.",
        "cheer": "당신의 한결같은 성실함이 가장 큰 무기랍니다 🐧"
    },
    "ISFJ": {
        "title": "🌷 다정한 수호자 레서판다",
        "jobs": ["🏥 간호사", "📚 사서", "🧸 유치원 교사", "🍰 디저트 파티시에"],
        "desc": "조용히 주변 사람들을 챙겨주는 세심하고 친절한 천사! 보이지 않는 곳에서 빛나요.",
        "cheer": "당신의 작은 배려가 누군가에겐 커다란 힘이 돼요 🌸"
    },
    "ESTJ": {
        "title": "📢 완벽주의 체계왕 강아지",
        "jobs": ["📊 프로젝트 매니저(PM)", "🏦 금융 관리자", "🏢 운영 총괄 디렉터", "👮 경찰/소방관"],
        "desc": "일처리가 신속 정확하고 효율적인 만능 관리자! 규칙과 체계를 명확히 세워요.",
        "cheer": "당신의 착착 맞춰진 리더십은 정말 든든해요! 🛡️"
    },
    "ESFJ": {
        "title": "🍰 친절한 분위기 메이커 다람쥐",
        "jobs": ["✈️ 승무원", "🎉 행사 MC", "🩺 의료 코디네이터", "🤝 고객 만족(CS) 팀장"],
        "desc": "친화력 100%! 어디서나 분위기를 밝게 만들고 사람들을 세심하게 아껴요.",
        "cheer": "당신과 함께라면 어디든 따뜻하고 즐거운 공간이 돼요 🍰"
    },
    "ISTP": {
        "title": "🛠️ 만능 손재주 고양이",
        "jobs": ["🏎️ 카레이서/정비사", "💻 시스템 엔지니어", "📐 건축 설계사", "📸 사진작가"],
        "desc": "상황 판단력이 빠르고 도구를 자유자재로 다루는 능력자! 쿨하고 솔직한 매력이 있어요.",
        "cheer": "당신의 침착하고 날카로운 감각이 멋져요! 🔧"
    },
    "ISFP": {
        "title": "🎨 힐링 아티스트 사막여우",
        "jobs": ["💄 메이크업 아티스트", "🌸 플로리스트", "🐾 수의사 보조/애견 미용사", "🖼️ 그래픽 디자이너"],
        "desc": "현재를 즐길 줄 아는 겸손한 예술가! 따뜻한 온기 감성과 미적 감각을 지녔어요.",
        "cheer": "당신이 만들어내는 소소한 아름다움이 정말 좋아요 🌿"
    },
    "ESTP": {
        "title": "⚡ 모험을 즐기는 수달",
        "jobs": ["🏃 스포츠 트레이너", "💼 스페셜 영업 전문가", "🚑 응급구조사", "📈 주식 트레이더"],
        "desc": "에너지 넘치고 순발력 최고! 백마디 말보다 직접 몸으로 부딪히며 해결해요.",
        "cheer": "망설이지 않고 도전하는 당신의 용기가 짱이에요! 🚀"
    },
    "ESFP": {
        "title": "✨ 흥 부자 슈팅스타 사자",
        "jobs": ["🎭 뮤지컬 배우", "🎤 리포터/아나운서", "👗 패션 스타일리스트", "🎉 레크리에이션 강사"],
        "desc": "오늘을 즐겁게 사는 스타성 만점! 사람들에게 웃음과 에너지를 선사해요.",
        "cheer": "당신이 등장하는 순간 세상의 조명이 켜져요! 💖"
    }
}

# 4. 앱 헤더 화면
st.markdown('<div class="main-title">💖 뽀짝 MBTI 맞춤 직업 탐험 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 MBTI를 선택하면, 딱 어울리는 깜찍한 직업을 추천해드려요!</div>', unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트박스
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_mbti = st.selectbox(
        "✨ 당신의 MBTI는 무엇인가요?",
        list(mbti_data.keys()),
        index=0
    )
    
    # 귀여운 분석 버튼
    analyze_btn = st.button("✨ 직업 탐험 시작하기 ✨", use_container_width=True)

# 6. 결과 출력 로직
if analyze_btn:
    # 귀여운 로딩 애니메이션 효과
    with st.spinner("🎀 귀여운 직업 요정이 당신의 성격을 분석 중이에요..."):
        time.sleep(0.7)
    
    st.balloons() # 풍선 팡팡 이펙트!
    
    data = mbti_data[selected_mbti]
    
    # 카드 형태로 결과 표시
    st.markdown(f"""
    <div class="cute-card">
        <h2 style="color: #FF6B8B; text-align: center; margin-bottom: 5px;">[{selected_mbti}] {data['title']}</h2>
        <p style="text-align: center; font-size: 1.05rem; color: #555; margin-bottom: 20px;">{data['desc']}</p>
        <hr style="border: 1px dashed #FFD1DC;">
        <h4 style="color: #8860D0; margin-top: 15px;">✨ 당신에게 딱 맞을 추천 직업 List</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # 추천 직업 리스트 출력
    for job in data['jobs']:
        st.markdown(f'<div class="job-box">{job}</div>', unsafe_allow_html=True)
        
    # 응원 메시지 박스
    st.info(f"💌 **요정의 한마디:** {data['cheer']}")

# 7. 푸터 (하단 안내)
st.markdown("---")
st.caption("💕 내 꿈을 향해 달리는 당신을 항상 응원합니다! | Streamlit으로 제작됨")
