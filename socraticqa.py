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
    session_type = st.radio(
    "오늘 연습할 주제를 선택하세요:",
    ("동기부여 강화", "약물에 대한 생각 전환하기") # session 1, session 2
    )
    # session 1 : shoring up motivation -> 후에 여기에 적은 부정적인 결과 응답을 팝업 알림으로 활용도 가능할듯.
    if session_type == "동기부여 강화":
        st.subheader("📌 약물 중단의 동기부여하기")
    
        with st.form("motivation_form"):
            pos = st.text_area("✅ 약물을 사용했을 때의 긍정적인 결과는 무엇인가요?", value=st.session_state.get("pos", ""), key="pos")
            neg = st.text_area("❌ 약물을 사용했을 때의 부정적인 결과는 무엇인가요?", value=st.session_state.get("neg", ""), key="neg")
            st.markdown("---")
        
            goal = st.text_area("🎯 이 프로그램을 통해 만들어 내고 싶은 변화는 무엇인가요?", value=st.session_state.get("goal", ""), key="goal")
            reason = st.text_area("🎯 그 변화가 필요한 가장 중요한 이유는 무엇인가요?", value=st.session_state.get("reason", ""), key="reason")
            change_step = st.text_area("🎯 변화를 위해 계획중인 거쳐야 할 단계들이 있다면 무엇인가요?", value=st.session_state.get("change_step", ""), key="change_step")
            other = st.text_area("🎯 나의 변화를 돕기 위해 다른 사람들이 도와줄 수 있는 일들에는 뭐가 있을까요?", value=st.session_state.get("other", ""), key="other")
            interfere = st.text_area("🎯 나의 변화를 방해할만한 요인들에는 무엇이 있을까요?", value=st.session_state.get("interfere", ""), key="interfere")
        
            submitted = st.form_submit_button("제출하기")
        
            if submitted:
                if all([st.session_state.pos.strip(), st.session_state.neg.strip(), st.session_state.goal.strip(), st.session_state.reason.strip(), st.session_state.change_step.strip(), st.session_state.other.strip(), st.session_state.interfere.strip()]):
                    st.session_state.finished = True
                
                    st.success("🎉 좋아요! 목표 점검은 우리의 의지를 한층 강화해줍니다.")
                    st.markdown("#### 📋 실습 요약")
                    st.markdown(f"- **약물 사용의 긍정적 결과**: {st.session_state.pos}")
                    st.markdown(f"- **약물 사용의 부정적 결과**: {st.session_state.neg}")
                    st.markdown(f"- **내가 이뤄낼 변화**: {st.session_state.goal}")
                    st.markdown(f"- **변화를 이뤄내야 하는 이유**: {st.session_state.reason}")
                    st.markdown(f"- **거쳐야 할 단계들**: {st.session_state.change_step}")
                    st.markdown(f"- **다른 사람들이 나를 도울 수 있는 일들**: {st.session_state.other}")
                    st.markdown(f"- **나의 변화를 방해할만한 요인들**: {st.session_state.interfere}")
                    st.success("동기부여 세션 저장 완료!")

                else:
                    st.warning("⚠️ 모든 항목을 작성해주세요.")



# 🟢 2. 약물에 대한 생각 전환하기 세션
    elif session_type == "약물에 대한 생각 전환하기":
        st.subheader("🧠 약물에 대한 생각 전환하기")
        st.markdown(f"""
                    약물을 사용하고 싶다는 생각이 들 때 대처할 수 있는 생각 전환 방법에는 다음과 같은 것들이 있습니다.
                    - 마지막으로 약물을 사용했을 때의 끝을 생각하고 기억하기
                    - 자신의 생각을 도전적으로 바라보기
                    - 코카인 사용의 부정적인 결과를 떠올리기
                    - 약물을 사용하고 싶다는 생각에 집중하지 않도록 주의를 분산시키기
                    - 생각을 바꾸는 과정에서 생각을 말로 표현하기

                    예를 들어, 💭 *스트레스를 받을 때 약물을 사용해야만 한다*는 생각이 든다면 

                    🛠️ *스트레스 해소를 위해 명상이나 운동을 한다*

                    🛠️ *약물을 사용하면 일시적으로는 기분이 좋아지지만, 결국에는 더 큰 공허함을 느끼게 된다*와 같이 생각 전환을 할 수 있어요.
                    """)
        thought = st.text_area("💭 약물을 사용하고 싶다는 생각이 들었을 때, 구체적으로 어떤 생각이 들었나요?", key="thought")
        coping = st.text_area("🛠️ 이를 어떻게 전환할 수 있을까요?", key="coping")

        if st.button("제출하기", key="submit_button_3"):
            st.success("생각 전환 세션 저장 완료!")
            st.session_state.finished = True


def refusal_skills_assertiveness(): # topic 3
    st.markdown("## 🚨 거절 연습하기")  
    st.markdown("""
    우리의 궁극적인 목표는 **약물의 사용을 줄이는 것**입니다.
    이를 위해서는 약물에 대한 접근성을 줄이거나 약물의 권유를 효과적으로 거절하는 것이 필요합니다.
    
    **약물 사용 제안을 거절하는 방법**은 다음과 같습니다.            
    - 제안 전에 먼저 거절하세요.
    - 상대방에게 코카인을 제안하지 말라고 요청하세요.
    - 제한을 설정하는 것을 두려워하지 마세요.
    - 거절 시 여지를 남기지마세요. (ex. '오늘은 안 돼' ❌ ->  '저는 더 이상 그럴 생각이 없어요 ✅')
    - 수동적인이거나 공격적인 반응이 아닌, **단호한** 거절을 하세요.
    """)
    with st.form("refusal_form"):
        route = st.text_area("약물에 접근하게 되는 경로와, 접근을 줄이기 위해 취할 수 있는 조치를 적어보세요.", key = "route")
        offer = st.text_area("약물을 제안할 것 같은 사람과, 그들에게 거절의 표시를 어떻게 전할 것인지 적어보세요.", key = "offer")
    
        submitted = st.form_submit_button("제출하기")

    if submitted:
        if route.strip() and offer.strip():
            st.success("🎉 잘하셨어요! 거절 연습 세션이 완료되었습니다.")
            st.markdown("#### 📋 실습 요약")
            st.markdown(f"- **약물 접근 경로 및 조치**: {route}")
            st.markdown(f"- **약물 제안자 및 거절 방법**: {offer}")
            st.session_state.finished = True
        else:
            st.warning("⚠️ 두 항목 모두 작성해주세요.")


def seemingly_irrelevant_decisions(): # topic 4
    st.markdown("## 🧭 의사결정 훈련: 안전한 선택과 위험한 선택 구분하기")
    st.markdown("""
    우리는 하루에도 크고 작은 다양한 결정을 내리게 됩니다.  
    약물 사용에서 회복하는 과정에서는 **작은 결정 하나가 유지 혹은 재발을 가를 수 있습니다.**

    다음의 원칙을 기억하며 결정을 연습해보세요:

    - 가능한 모든 선택지를 고려해보기
    - 각각의 선택지에 대해 모든 긍정적/부정적 결과 생각하기
    - **약물 중독 재발 위험을 최소화하는 안전한 선택** 고르기
    - “내가 해야만 해”, “괜찮을 거야”, “한 번쯤은 괜찮지” 같은 **Red flag 사고🔴**에 주의하기
    """)

    with st.form("decision_form"):
        decision = st.text_area("💭 오늘 당신이 내렸거나 내리게 될 중요한 결정은 무엇인가요?", key="decision")
        safe_alt = st.text_area("🟢 이 상황에서 약물 사용 재발의 가능성을 줄이는 **안전한 선택**은 무엇인가요?", key="safe_alt")
        risky_alt = st.text_area("🔴 약물 사용 재발 위험을 높일 수 있는 **위험한 선택**은 무엇인가요?", key="risky_alt")

        submitted = st.form_submit_button("제출하기")

    if submitted:
        if decision.strip() and safe_alt.strip() and risky_alt.strip():
            st.success("👍 훌륭해요! 당신의 선택을 돌아보며 스스로를 지킬 수 있는 힘이 생기고 있어요.")
            st.markdown("#### 🧾 오늘의 의사결정 요약")
            st.markdown(f"- **결정 상황**: {decision}")
            st.markdown(f"- ✅ 안전한 선택: {safe_alt}")
            st.markdown(f"- ⚠️ 위험한 선택: {risky_alt}")
            st.session_state.finished = True
        else:
            st.warning("⚠️ 모든 항목을 작성해주세요.")


def all_purpose_coping_plan(): # topic 5
    st.markdown("## ⚠️ 위험 상황 대응 훈련")
    st.markdown("""
    여러분이 최선을 다하더라도 언제든 예기치 못한 상황은 발생할 수 있습니다.
    이는 여러분의 잘못이 아니며, 긍정적인 사건이든 부정적인 사건이든 약물 사용 재발의 고위험 상황으로 이어질 수 있습니다.
    이번 시간에는 이러한 위기 상황이 발생할 경우 참고하고 사용할 수 있는 비상 대응 계획을 세워보세요.

    다음의 원칙을 기억하며 계획을 세워보세요.
    - 예기치 못한 상황이 닥치는 것은 자연스러운 삶의 한 부분이며, 항상 피할 수는 없습니다.
    - 다만, 가장 중요한 것은 그 상황이 약물 사용의 재발로 이어지지 않아야 한다는 것입니다.
    """)

    with st.form("decision_form"):
        st.markdown("💭 당신이 약물 사용의 위험 상황에 처했을 때, 어떻게 행동할 것인지 선언문을 적어봅시다.")
        q1 = st.text_area("1️⃣ 나는 그 상황을 피하거나 바꿀 것이다. 내가 그 때 갈 수 있는 안전한 곳은:", key="q1")
        q2 = st.slider("2️⃣ 나는 약물을 사용할지 여부를 15분 후에 결정할 것이다. 내 갈망은 보통 ___ 분 후에 사라진다는 것을 안다. 그리고 과거에 갈망을 성공적으로 이겨낸 경험이 있다.", min_value=1, max_value=15, value=7, key="q2")
        q3 = st.text_area("3️⃣ 나는 내가 좋아하는 행동을 하며 약물에 대한 주의를 분산시킬 것이다. 그 행동은:", key="q3")
        q4 = st.text_area("4️⃣ 나는 나의 비상연락망에 전화를 할 것이다. 전화번호는:", key="q4")
        q5= st.text_area("5️⃣ 나는 내가 지금까지 이뤘던 금단 성공을 기억할 것이다. 내가 그동안 버텼던 기간과 행동은:", key="q5")
        q6 = st.text_area("6️⃣ 나는 긍정적인 사고로의 전환을 기억하며 약물을 사용하고 싶다는 지금의 생각을 바꿔버릴 것이다. 전환한 생각은:", key="q6")
        
        submitted = st.form_submit_button("제출하기")

    if submitted:
        if all([q1.strip(), q3.strip(), q4.strip(), q5.strip(), q6.strip()]):
            st.success("👍 훌륭해요! 이 선언문을 계속해서 읽어봅시다.")
            st.markdown("#### 🧾 선언문 요약")
            st.markdown(f"1️⃣ **내가 약물 사용을 피하거나 상황을 바꿀 장소**: {q1}")
            st.markdown(f"2️⃣ **내가 참으면 되는 잠깐의 시간**: {q2}분")
            st.markdown(f"3️⃣ **주의를 돌릴 수 있는 활동**: {q3}")
            st.markdown(f"4️⃣ **비상연락망 전화번호**: {q4}")
            st.markdown(f"5️⃣ **내가 그동안 버텼던 성공의 기억들**: {q5}")
            st.markdown(f"6️⃣ **생각의 전환**: {q6}")
            st.session_state.finished = True
        else:
            st.warning("⚠️ 모든 항목을 작성해주세요.")

def problemsolving(): # topic 6
    st.markdown("## ⚠️ 문제 해결 훈련")
    st.markdown("""
    많은 사람들은 문제가 발생했을 때 이를 올바르게 인식하지 못하고 충동적으로 행동할 가능성이 높습니다.
    특히, 치료를 마치고 퇴원을 하면 이전에는 약물에 가려져 보이지 않았던 현실의 문제들에 직면하게 될 수 있습니다.
    이 때, 일시적인 해결책으로 충동적인 약물 사용을 하지 않도록 **올바른 문제 해결법**을 연습해봅시다.
                
    1️⃣ "어떤 문제가 있나요?” 
        - 문제가 존재한다는 것을 인식합니다. 우리는 몸, 생각과 감정, 행동, 다른 사람에 대한 반응, 그리고 다른 사람들이 우리에게 반응하는 방식에서 단서를 얻습니다.
   
    2️⃣ “문제가 무엇인가요?” 
        - 문제를 식별합니다. 문제를 가능한 한 정확히 설명합니다.
                
    3️⃣ 문제를 관리가 가능한 부분으로 나누세요.
                
    4️⃣ “무엇을 할 수 있을까요?” 
        - 문제를 해결하기 위한 다양한 접근 방법을 고려합니다. 브레인스토밍을 통해 가능한 한 많은 해결책을 생각해 봅니다. 상황을 바꾸기 위해 행동을 취하거나, 상황에 대한 생각을 바꾸는 것을 고려합니다.
                
    5️⃣ “만약 . . .라면 어떻게 될까요?” 
        - 가장 유망한 접근 방법을 선택합니다. 각 가능성 있는 접근 방법의 긍정적 및 부정적 측면을 모두 고려하고, 문제를 해결할 가능성이 가장 높은 것을 선택합니다.
                
    6️⃣ “어떻게 되었나요?” 
        - 선택한 접근 방식의 효과를 평가하세요. 접근 방식을 충분히 시도한 후, 효과가 있는 것 같은지 평가합니다. 그렇지 않다면 계획을 강화하기 위해 할 수 있는 일을 고려하거나, 포기하고 다른 가능한 접근 방식 중 하나를 시도해 보세요.
    """)
    with st.form("problemsolving_form"):
        st.markdown("## ⚠️ 위의 설명을 읽어보고 답변을 적어보세요.")
        problem = st.text_input("💭 아직 명확한 해결책이 없는 문제가 무엇인가요?", key="problem")
        brainstorming = st.text_input("💭 그에 대한 해결책을 브레인스토밍 해봅시다.")
        numbering = st.text_input("💭 위에 적은 해결책들을 선호하는 순서대로 정리해봅시다.", key = 'numbering')

        submitted = st.form_submit_button("제출하기")    
        if submitted:
            if all([problem.strip(), brainstorming.strip(), numbering.strip()]):
                st.success("👍 좋습니다! 이렇게 건강한 방법으로 문제를 해결해보아요.")
                st.markdown("#### 🧾 문제 상황 및 해결책책 요약")
                st.markdown(f"1️⃣ **내가 처한 문제 상황**: {problem}")
                st.markdown(f"2️⃣ **이를 해결할 수 있는 방법**: {numbering}")
                st.session_state.finished = True
            else:
                st.warning("⚠️ 모든 항목을 작성해주세요.")
    

def case_management(): # topic 7
    st.markdown("## 📋 사례 관리 훈련")
    st.markdown("""
    약물 중단을 오래 유지하기 위해서는 약물 자체만이 아니라, 사회심리적인 문제도 해결이 되어야 합니다.
    이를 위해서는 여러분이 속해 있는 사회 안에서 의지할 수 있는 시스템 혹은 사람을 확인하고 그들을 활용할 수 있어야 합니다.         
    
    확인하길 권장하는 정보에는 다음과 같은 것들이 있습니다.
    - 각 기관이 어떤 서비스를 제공하는지
    - 누구를 대상으로 서비스를 제공하는지 (청소년, 성인, 특정 질환자 등)
    - 서비스를 받기 위한 자격 조건
    - 다른 대안 기관은 어디 있는지
    """)

    with st.form("plan_form"):
        contact_plan = st.text_input("1️⃣ 나의 목표는 무엇인가요?", key="contact_plan")
        contact_person = st.text_input("2️⃣ 누구에게 연락할 건가요? (이름, 전화번호, 주소 등)", key="contact_person")
        contact_situation = st.text_input("3️⃣ 어떤 상황에 연락할 건가요?", key="contact_situation")
        requested_services = st.text_area("4️⃣ 어떤 서비스를 요청할 건가요?", key="requested_services")
        outcome = st.text_area("📋결과", key="outcome")
        submitted = st.form_submit_button("제출하기")

    if submitted:
        if all([contact_plan.strip(), contact_person.strip(), contact_situation.strip(),requested_services.strip(),outcome.strip()]):
            st.success("👍 훌륭해요! 좋은 계획입니다.")
            st.markdown("### 📋 나의 목표 실행 계획")
            st.table({
                    "항목": ["나의 목표", "연락 대상", "연락할 상황", "요청 서비스", "결과"],
                    "내용": [
                        contact_plan,
                        contact_person,
                        contact_situation,
                        requested_services,
                        outcome 
                    ]
                })
            st.session_state.finished = True
        else:
            st.warning("⚠️ 모든 항목을 작성해주세요.")

def HIV_risk_reduction(): # topic 8
    st.markdown("## 🛡️ HIV 감염 위험 감소를 위한 변화 계획 세우기")

    with st.form("change_plan_form"):
        changes = st.text_area("1️⃣ HIV 감염 위험 감소를 위해 내가 바꾸고 싶은 행동은 무엇인가요?", key="changes")
        reasons = st.text_area("2️⃣ 내가 이렇게 변해야만 하는 가장 중요한 이유는 무엇인가요?", key="reasons")
        steps = st.text_area("3️⃣ 변화를 위해 계획한 구체적인 행동은 무엇인가요?", key="steps")
        helper = st.text_area("4️⃣ 다른 사람들이 이 계획을 도와줄 수 있는 방법은 뭐가 있을까요?", key="helper")
        obstacles = st.text_area("5️⃣ 이 계획을 방해할만한 장애물이 있다면 무엇일까요?", key="obstacles")

        submitted = st.form_submit_button("제출하기")

        if submitted:
            if all([
                changes.strip(), reasons.strip(), steps.strip(),
                obstacles.strip(), helper.strip()]):
                st.success("🎯 계획이 잘 정리되었습니다! 실천으로 이어가 보세요.")
                st.markdown("### 📋 변화 계획 요약")
                st.markdown(f"- **바꾸고 싶은 행동:** {changes}")
                st.markdown(f"- **변화 이유:** {reasons}")
                st.markdown(f"- **다른 사람들이 도와줄 수 있는 방법:** {helper}")
                st.markdown(f"- **예상되는 장애물:** {obstacles}")
                st.session_state.finished = True
            else:
                st.warning("⚠️ 모든 항목을 작성해주세요.")

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

            if st.button("선택한 실습 시작하기"):
                st.session_state.selected_skill = selected_skill_name
                st.session_state.page = "run_skill"
                st.experimental_rerun()
            # 'run_skill' 페이지에서 선택된 스킬 실행
            if st.session_state.get("page") == "run_skill":
                selected_skill = st.session_state.get("selected_skill")
                if selected_skill:
                    st.markdown(f"▶ 선택한 연습 스킬: **{selected_skill}**")
                    intervention_func = distortion_to_intervention.get(selected_skill) or skill_name_to_func.get(selected_skill)
                    if intervention_func:
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
