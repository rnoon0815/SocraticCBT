import streamlit as st
from openai import OpenAI
import datetime

st.set_page_config(page_title="CBT 챗봇", layout="centered")

def coping_with_craving(): # topic 1 - 약물을 사용한 경우 무조건 실행
    st.markdown("## 🚨 갈망 대처 실습")  
    st.markdown("""
    약물을 복용하고 싶은 욕구는 **흔하고 자연스러운 증상**이며, 약물 복용 중단의 실패를 의미하는 게 아닙니다. 
    충동은 파도와 같습니다.  일정 수준까지 강해지다가 점차 약해지기 시작합니다.
    약물을 사용하지 않으면 충동은 약해지고 결국 사라지며, 충동은 그에 굴복할 때만 강해집니다.
    궁극적으로 약물 사용을 하고 싶은 욕구에서 탈출하기 위해서는 충동을 유발하는 신호 혹은 상황을 피하거나 없애는 방법을 선택할 수 있습니다.
    
    **충동을 대처하는 방법**은 다음과 같습니다.
    - 몇 분 동안 다른 일에 집중하기.
    - 나를 지지해주는 사람과 충동에 대해 이야기하기.
    - 충동을 가만히 느끼며 이해하기 또는 충동을 견디기.
    - 약물을 사용했을 때의 부정적인 결과를 떠올리기.
    - 스스로에게 충동을 이겨내는 방법을 설명하기.
                
    이는 실패의 신호가 아닌, 회복 과정의 일부입니다.
    아래 실습을 통해 당신의 갈망(trigger)을 인식하고, 스스로 효과적으로 대처하는 방법을 정리해봅시다.
    """)
    # 정리하러 가기 버튼 누르면 세션 상태에 저장
    if "show_craving_form" not in st.session_state:
        st.session_state.show_craving_form = False

    if not st.session_state.show_craving_form:
        if st.button("정리하러 가기"):
            st.session_state.show_craving_form = True
            st.experimental_rerun()

    if st.session_state.show_craving_form:
        with st.form("craving_form"):
            craving_event = st.markdown("1️⃣ 최근 약물을 사용하고 싶었던 때와 장소는 언제였나요?")
            selected_date = st.date_input("📅 날짜를 선택하세요", value=datetime.date.today(), key="selected_date")
            selected_time = st.time_input("⏰ 시간을 선택하세요", value=datetime.datetime.now().time(), key="selected_time")
            selected_place = st.text_area("📍 장소를 입력해주세요", key="selected_place")        
            craving_trigger = st.text_area("2️⃣ 그 때 어떤 일이 있었고, 어떤 생각과 기분이 들었나요?", key="craving_trigger")
            craving_intensity = st.slider("3️⃣ 약물을 사용하고 싶은 충동은 어느 정도로 강했나요? 숫자를 선택해주세요", min_value=1, max_value=100, value=50, key="craving_intensity")
            craving_length = st.text_input("4️⃣ 그 충동은 얼마나 지속됐나요?", key="craving_length")
            coping_options = [
                "몇 분 동안 다른 일에 집중하기",
                "지지해주는 사람과 이야기하기",
                "충동이 자연스러운 것임을 인정하며 지금 상태를 견디기",
                "약물 사용의 부정적 결과 떠올리기",
                "스스로에게 이겨낼 방법 설명하기",
                "기타 (직접 입력)"
            ]
            selected_coping = st.selectbox("5️⃣ 다음에는 어떤 대처 방법을 사용해볼까요?", options=coping_options, key="coping_strategy")
            # coping_custom 값이 있을 경우 selected_coping에 반영
            
            coping_summary = st.text_area("위 방법을 구체적으로 어떻게 사용할 것인가요?", key="coping_summary")

            submitted = st.form_submit_button("갈망 대처 실습 제출")
            
            if submitted:


                if all([
                    len(selected_place.strip()) > 0,
                    len(craving_trigger.strip()) > 0,
                    len(str(craving_intensity).strip()) > 0,
                    len(craving_length.strip()) > 0,
                    len(coping_summary.strip()) > 0
                ]):

                    st.success("🎉 훌륭해요! 갈망에 대한 인식과 대처 전략은 회복의 핵심입니다.")
                    st.markdown("#### 📋 실습 요약")
                    st.markdown(f"- **날짜 및 시간**: {selected_date.strftime('%Y-%m-%d')} {selected_time.strftime('%H:%M:%S')}")
                    st.markdown(f"- **장소**: {selected_place}")
                    st.markdown(f"- **갈망 유발 요인**: {craving_trigger}")
                    st.markdown(f"- **충동 강도**: {craving_intensity} / 100")
                    st.markdown(f"- **충동 지속 시간**: {craving_length}")
                    st.markdown(f"- **다음에 사용할 대처 전략**: {selected_coping}")
                    st.session_state.finished = True
                else:
                    st.warning("⚠️ 모든 항목을 작성해주세요.")

def shoring_up_motivation(): # topic 2 - shoring up motivation and commitment to stop : 의지 박약 시
    pass


def refusal_skills_assertiveness(): # topic 3
    pass

def seemingly_irrelevant_decisions(): # topic 4
    pass

def all_purpose_coping_plan(): # topic 5
    pass

def problemsolving(): # topic 6
    pass

def case_management(): # topic 7
    pass

def HIV_risk_reduction(): # topic 8
    pass

distortion_to_intervention = { # 인지 왜곡과 연습할 skill training (topic) 연결
    "mind reading": refusal_skills_assertiveness,
    "fortune-telling": shoring_up_motivation,
    "all-or-nothing thinking": problemsolving,
    "should statements": refusal_skills_assertiveness,
    "labeling": case_management,
    "emotional reasoning": all_purpose_coping_plan,
    "personalization": seemingly_irrelevant_decisions,
    "magnification": problemsolving,
    "overgeneralization": shoring_up_motivation,
    "mental filter": all_purpose_coping_plan
}

skill_name_map = {
    refusal_skills_assertiveness: "거절 기술 및 자기주장 훈련",
    shoring_up_motivation: "동기 강화 훈련",
    problemsolving: "문제 해결 훈련",
    seemingly_irrelevant_decisions: "관련 없는 결정 분석 훈련",
    all_purpose_coping_plan: "범용 대처 계획 훈련",
    case_management: "사례 관리 훈련",
    HIV_risk_reduction: "위험 감소 훈련"
}
skill_name_to_func = {v: k for k, v in skill_name_map.items()}

# OpenAI 클라이언트 생성
api_key = st.secrets["openai_api_key"]
client = OpenAI(api_key=api_key)

st.title("🧠 CBT 자기기록 - Today's Record")

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = -1
    st.session_state.used_drug = None
    st.session_state.responses = []
    st.session_state.finished = False

# 질문 리스트
drug_questions = [
    "1. 어떤 감정이나 생각이 들었을 때 약물을 사용했나요?",
    "2. 당시에 '약물 없이 견딜 수 없다'고 느낀 이유는 무엇이었나요?",
    "3. 약물을 사용해야 한다고 느끼게 만든 이전의 구체적인 경험이나 근거가 있었을까요?",
    "4. 이렇게 약물을 사용하는 것이 당신의 삶에 어떤 긍정적/부정적 영향을 미칠 것 같나요?",
    "5. 다시 그 순간으로 돌아간다면, 어떤 다른 선택을 해볼 수 있을까요?"
]

cbt_questions = [
    "1. 지금 어떤 생각이 가장 많이 떠오르나요?",
    "2. 그 생각이 옳다고 믿는 근거는 무엇인가요?",
    "3. 그 생각을 뒷받침할 수 있는 근거가 있나요?",
    "4. 그런 생각을 계속하면 어떤 결과가 생길까요?",
    "5. 다른 시각에서 본다면 어떤 생각이 가능할까요?"
]

# Step -1: 약물 사용 여부 선택
if st.session_state.step == -1:
    st.session_state.used_drug = st.selectbox("오늘 약물 복용을 했나요?", ("", "예", "아니오"))
    if st.session_state.used_drug in ["예", "아니오"]:
        st.session_state.step = 0
        st.experimental_rerun()

# Step 0~4: 질문 응답
elif 0 <= st.session_state.step < 5:
    questions = drug_questions if st.session_state.used_drug == "예" else cbt_questions
    current_question = questions[st.session_state.step]
    user_input = st.text_area(f"💬 {current_question}", key=f"q_{st.session_state.step}")

    if st.button("답변 제출"):
        if user_input.strip():
            st.session_state.responses.append(user_input.strip())
            st.session_state.step += 1
            st.experimental_rerun()
        else:
            st.warning("⚠️ 답변을 입력해주세요.")

# Step 5: GPT로 인지 왜곡 분석
elif st.session_state.step == 5 and not st.session_state.finished:
    if st.session_state.used_drug == "예":
        st.session_state.step = 6
        st.experimental_rerun()
    else:
        questions = cbt_questions
        all_answers = ""
        for i, (q, a) in enumerate(zip(questions, st.session_state.responses), 1):
            all_answers += f"{i}. 질문: {q}\n   답변: {a}\n\n"
            st.markdown(f"**{q}**")
            st.markdown(f"- 💬 사용자 답변: {a}")
            st.markdown("---")

        if "classification_summary" not in st.session_state:
            try:
                response = client.chat.completions.create(
                    model="ft:gpt-3.5-turbo-1106:personal:distortion:BZis7uu0",
                    messages = [{"role": "system", "content": "You are a CBT chatbot. You understand and analyze user input in Korean. Please always respond in English."},{"role": "user", "content": f"Below is the user's CBT self-record. Please analyze each response and identify the cognitive distortions or belief types present. Respond only in English, listing only the distortions found from the following possible types: mind reading, fortune-telling, all-or-nothing thinking, should statements, labeling, emotional reasoning, personalization, magnification, overgeneralization, and mental filter.:\n\n{all_answers}"}],
                    temperature=0.0,
                )
                st.session_state.classification_summary = response.choices[0].message.content.strip()
            except Exception as e:
                st.session_state.classification_summary = f"❌ 오류 발생: {str(e)}"

        st.markdown("### 🧠 오늘의 인지 왜곡/신념 분석")
        st.markdown(f"{st.session_state.classification_summary}")

        matched_distortions = [d for d in distortion_to_intervention.keys() if d.lower() in st.session_state.classification_summary.lower()]

        if matched_distortions:
            st.success(f"✨ 감지된 주요 인지 왜곡: {', '.join(matched_distortions)}")
            st.markdown("👇 아래에서 실습할 인지 왜곡을 선택하세요:")
            selected_distortion = st.selectbox("인지 왜곡 선택", options=matched_distortions)
            if st.button("선택한 실습 시작하기"):
                intervention_func = distortion_to_intervention[selected_distortion]
                intervention_func()

                    # Step 6로 이동시키고 finished는 여기서 안 건드림
            if st.button("다음 단계로 진행하기"):
                st.session_state.step = 6
                st.experimental_rerun()

        else:
            st.info("특정한 인지 왜곡이 감지되지 않았습니다. 필요에 따라 연습할 스킬을 수동으로 선택할 수 있습니다.")
            # 모든 스킬 리스트트
            all_skills = list(skill_name_map.values())
            selected_skill_name = st.selectbox("연습할 스킬 선택", options=all_skills)
            if st.button("선택한 실습 시작하기 (수동)"):
                intervention_func = skill_name_to_func[selected_skill_name]
                st.markdown(f"▶ 선택한 연습 스킬: **{selected_skill_name}**")
                intervention_func()

# Step 6: 대처 실습
elif st.session_state.step == 6 and not st.session_state.finished:
    coping_with_craving()  # 혹은 약물 사용 여부에 따라 다르게 할 수도 있음

# 종료 후 초기화 버튼
if st.session_state.finished:
    if st.button("처음으로 돌아가기"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
