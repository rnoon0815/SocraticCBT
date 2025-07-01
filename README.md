**2025년 1학기 URP (소프트웨어학부연구학점제) 용 코드**

URP 주제 : 청소년 약물중독자를 위한 Socratic QA 기반의 CBT 치료 프로그램 (웹으로 제공)

환경 : python + GPT 3.5 turbo finetuning & streamlit 으로 배포

CBT의 구성요소 중 Functional analysis와 skill training을 기반으로 구현
- functional anlaysis : 6개의 정형화된 고정 질의응답. 폼 형태로 제공.
- 이 응답을 모아 Fine tuned GPT (인지왜곡분류기)의 input으로 활용. -> 인지왜곡유형 분류
- 위의 output(인지왜곡 유형)을 효과적으로 해소할 수 있는 skill training topic으로 연결.
- 해당 topic의 session들은 CBT manual의 학습지를 기반으로 폼이 구성되어 있음. 사용자가 해당 학습지를 수행하며 skill training 연습.

인지왜곡분류기
- 허깅페이스의 CBT benchmark dataset 이용.
- 기본 모델은 GPT 3.5 turbo
- 해당 dataset의 level 2 (distortion) data를 이용함.


  (프롬프트, 데이터 가공 등 이어서 쓰기)
