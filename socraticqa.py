import streamlit as st
import openai

#openai.api_key = st.secrets["openai"]["api_key"]
openai.api_key = "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"

st.set_page_config(page_title="CBT 챗봇", layout="centered")
st.title("Today's Record")

# 초기화
if "step" not in st.session_state:
    st.session_state.step = -1  # -1: 약물 여부 선택 전
    st.session_state.used_drug = None
    st.session_state.responses = []
    st.session_state.finished = False

# 질문 세트
drug_questions = [ # 오늘 약물을 사용한 경우 # 약물중독자를 위한 CBT 메뉴얼에서 추천하는 질문을 Socratic QA 구조와 적합한 것 중 고름.
    "1. 어떤 감정이나 생각이 들었을 때 약물을 사용했나요?",
    "2. 당시에 '약물 없이 견딜 수 없다'고 느낀 이유는 무엇이었나요?",
    "3. 약물을 사용해야 한다고 느끼게 만든 이전의 구체적인 경험이나 근거가 있었을까요??",
    "4. 이렇게 약물을 사용하는 것이 당신의 삶에 어떤 긍정적/부정적 영향을 미칠 것 같나요?",
    "5. 다시 그 순간으로 돌아간다면, 어떤 다른 선택을 해볼 수 있을까요?"
]

cbt_questions = [ # 약물 중단에 성공한 경우
    "1. 지금 어떤 생각이 가장 많이 떠오르나요?",
    "2. 그 생각이 옳다고 믿는 근거는 무엇인가요?",
    "3. 그 생각을 뒷받침할 수 있는 근거가 있나요?",
    "4. 그런 생각을 계속하면 어떤 결과가 생길까요?",
    "5. 다른 시각에서 본다면 어떤 생각이 가능할까요?"
]

# 1단계: 약물 사용 여부 선택
if st.session_state.step == -1:
    st.session_state.used_drug = st.selectbox("오늘 약물 복용을 했나요?", ("", "예", "아니오"))
    if st.session_state.used_drug in ["예", "아니오"]:
        st.session_state.step = 0
        st.rerun()

# 2단계 이후: 질문 진행
elif 0 <= st.session_state.step < 5:
    questions = drug_questions if st.session_state.used_drug == "예" else cbt_questions
    current_question = questions[st.session_state.step]
    user_input = st.text_area(f"💬 {current_question}", key=f"q_{st.session_state.step}")

    if st.button("답변 제출"):
        if user_input.strip():
            st.session_state.responses.append(user_input.strip())
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("답변을 입력해주세요.")

# 마지막: 응답 요약
elif st.session_state.step >= 5 and not st.session_state.finished:
    st.success("모든 질문에 답변하셨습니다. 아래는 당신의 기록과 인지 왜곡 분석입니다:")
    questions = drug_questions if st.session_state.used_drug == "예" else cbt_questions

    # 응답 묶기
    all_answers = ""
    for i, (q, a) in enumerate(zip(questions, st.session_state.responses), 1):
        all_answers += f"{i}. 질문: {q}\n   답변: {a}\n\n"

    # GPT 분류기 호출 (전체 텍스트로)
    if "classification_summary" not in st.session_state:
        try:
            response = openai.ChatCompletion.create(
                model="ft:gpt-3.5-turbo-1106:personal:distortion:BZis7uu0",
                messages=[
                    {"role": "user", "content": f"다음은 사용자의 CBT 자기기록입니다. 각 응답에 포함된 인지 왜곡 또는 신념 유형을 분석해주세요. 결과는 영어로 표시하세요.:\n\n{all_answers}"}
                ],
                temperature=0.0
            )
            st.session_state.classification_summary = response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            st.session_state.classification_summary = f"❌ 오류 발생: {str(e)}"

    # 출력
    for i, (q, a) in enumerate(zip(questions, st.session_state.responses), 1):
        st.markdown(f"**{q}**")
        st.markdown(f"- 💬 사용자 답변: {a}")
        st.markdown("---")


    # 분석 결과 출력 (영어 원문 그대로)
    st.markdown("### 🧠 오늘의 인지 왜곡/ 신념 분석")
    st.markdown(f"{st.session_state.classification_summary}")

    st.session_state.finished = True

# 다시 시작 옵션
if st.session_state.finished:
    if st.button("처음부터 다시 작성하기"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
