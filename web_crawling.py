import pandas as pd

class SimpleChatBot:
    # 챗봇 객체를 초기화하는 메서드
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    # CSV 파일로부터 질문과 답변 데이터를 불러오는 메서드
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers
        
    ###레벤슈타인 거리 계산하기###
    def calc_distance(self, a, b):
        if a == b: return 0 # 같으면 0을 반환
        a_len = len(a) # a 길이
        b_len = len(b) # b 길이
        if a == "": return b_len
        if b == "": return a_len
    
        matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
        for i in range(a_len+1): # 0으로 초기화
            matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
            
    # 0일 때 초깃값을 설정
        for i in range(a_len+1):
            matrix[i][0] = i
        for j in range(b_len+1):
            matrix[0][j] = j
            
    # 표 채우기 --- (※2)
        for i in range(1, a_len+1):
            ac = a[i-1]

        for j in range(1, b_len+1):
            bc = b[j-1] 
            
            cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
            ])
            
        return matrix[a_len][b_len]
    
    # 입력된 질문에 대한 답변을 찾는 함수
    def find_best_answer(self, input_sentence):
        a = input_sentence
        b = self.questions
        # 가장 레벤슈타인 거리가 짧은 질문을 찾음
        best_match_question = min(self.calc_distance(a, b))
        # 가장 유사한 질문에 해당하는 답변을 반환
        return self.answers[best_match_question]    

# 데이터 파일의 경로를 지정합니다.
filepath = open(r"c:\Users\배민욱\Desktop\HYOSIM SW\AI개발실무\final\ChatbotData.csv", 'r')

# 챗봇 객체를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)