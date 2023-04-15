from flask import Flask, request , jsonify
import os
import openai

openai.api_key = "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"
init_temperature = 0.7 

order_ai_new1_default = "위의 문장을, 영어로 번역해줘 "
order_ai_new2_default = "위의 문장을, 일본어로 번역해줘 "

order_ai_middle_default =  "\n , 이에 대하여, " 

order_ai_new1 = order_ai_new1_default
order_ai_new2 = order_ai_new2_default
order_ai_middle = order_ai_middle_default

guide_pointer = '여기에서 들여쓰기=표식=의미없음='

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    message2 = ''
    message3 = ''
    message4 = ''
    message5 = ''
    message6 = ''
    message7 = ''
    message8 = ''
    message9 = ''
    message10 = ''
    
    if request.method == 'POST':
        button = request.form.get('button')
        message = request.form.get('message')
        message2 = request.form.get('message2')
        message3 = request.form.get('message3')
        message4 = request.form.get('message4')

        message5 = request.form.get('message5')
        message6 = request.form.get('message6')
        message7 = request.form.get('message7')
        message8 = request.form.get('message8')
        message9 = request.form.get('message9')
        message10 = request.form.get('message10')

#====================== 버튼 == 가이드 라인 ==============
#=========================================================   
         
        if button == '5': # 프롬프트1 실행  
            
#========================> 프롬프트실행1 == order_ai_new1  ==============
# =========================================================   
            
            guide_pointer = '여기에서 들여쓰기'

            messages = []
            u_yonsei_univ = message
            
            if message2 == '' : 
                 message2 = order_ai_new1_default
            
            order_ai_new1 = message2

            u_yonsei_univ =  u_yonsei_univ + order_ai_middle + order_ai_new1 

            messages.append({"role": "user", "content": f"{u_yonsei_univ}"})
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature= init_temperature,
                top_p=1,
                messages=messages
              )

            assistant_content = completion.choices[0].message['content'].strip()
            messages.append({"role": "assistant", "content": f"{assistant_content}"})

#            message3 = u_yonsei_univ + "\n ====> 실행결과 ====> \n\n" + assistant_content 
            message4 = assistant_content 

# =========================================================   
        elif button == '9':
#======================  버튼 =>>>> 프롬프트실행2 ==============
# =========================================================   

            messages = []
            u_yonsei_univ = message

            if message3 == '' : 
                 message3 = order_ai_new2_default

            order_ai_new2 = message3

            guide_pointer = '여기에서 들여쓰기'  
          
            u_yonsei_univ =  u_yonsei_univ + order_ai_middle + order_ai_new2 

            messages.append({"role": "user", "content": f"{u_yonsei_univ}"})
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature= init_temperature,
                top_p=1,
                messages=messages
              )

            assistant_content = completion.choices[0].message['content'].strip()
            messages.append({"role": "assistant", "content": f"{assistant_content}"})

#            message3 = u_yonsei_univ + "\n ====> 실행결과 ====> \n\n" + assistant_content 
            message4 = assistant_content



# =========================================================   

# ================================
# ================================
# ================================

        elif button == '2':
            message5 = message5 + '\n\n' + message   # 결과물 저장 = 첫번째 


# ================================
# ================================
# ================================

        elif button == '10':
            message5 = message5 + '\n\n' + message4   # 결과물 저장2

#================ 이거는 무의미한 것  같아 = 나중에 삭제 요망 ===
#================ 이거는 무의미한 것  같아 = 나중에 삭제 요망 ===
#================ 이거는 무의미한 것  같아 = 나중에 삭제 요망 ===
#================ 이거는 무의미한 것  같아 = 나중에 삭제 요망 ===

        elif button == '11':
            message4 = message4 +'\n\n'+ message3 # 문단입력창2의 내용을 가져옴
        elif button == '12':
            message3 = ''   

            
#================ 이거는 무의미한 것  같아 = 나중에 삭제 요망 ===






        elif button == '13': # 모두 클리어 
            message = ''       
            message2 = ''       
            message3 = ''       
            message4 = ''       
        elif button == '14': # 맨위에 덧붙임 
            message = message + '\n\n' + message4 
        elif button == '15': # 맨위로 
            message = message4 
        elif button == '16': # 클리어 
            message4 = ''       
        else:
            pass
    return '''
        <style>
            body {{
                background-color: #333333;
            }}
            textarea {{
                background-color: black;
                color: white;
                font-size: 18px;
            }}

            button {{
                background-color: dimgray;
                color: white;
                font-size: 14px;
                cursor: pointer; /* 마우스 커서 모양 변경 */
            }}

            button:hover {{
                background-color: #006400; /* 마우스 오버 시 변경될 색상 */
            }}

        </style>
        <form method="post">
            <p>
                <p><textarea name="message" rows="10" cols="100"  placeholder="여기에, 영어를 포함한 모든 언어로 쓰여진 문장, 영어 공부하기, 언어 공부하기, 자기소개서 쓰기, 레포트 쓰기, 보고서 쓰기, 사업계획서 쓰기, 소설 쓰기, 시나리오 쓰기, 시 쓰기 ...외, 머리속에 떠오르는 내용을, 세련되고 알기 쉽게 적어주세요. 챗GPT 인공지능에게 명령을 내릴 아래의 프롬프트1,프롬프트2 명령어는(프롬프트1 기본값은 , 영어로 번역해줘) (프롬프트2 기본값은 , 영어로 번역해줘) 입니다. " >{0}</textarea>
                <button type="submit" name="button" value="2">    &nbsp;  &nbsp; &nbsp; &nbsp; 저장1 &nbsp; &nbsp;  &nbsp;  &nbsp;   </button>>
                </p>
            </p>
            <p>
                <p><textarea name="message2" rows="2" cols="100"  placeholder="여기에, 위의 내용을 바탕으로, 챗GPT에게 요청할 내용(프롬프트1)을 적어 넣으세요.(기본값은 , 영어로 번역해줘 , 입니다) "  >{1}</textarea>
                <button type="submit" name="button" value="5">    프롬프트1 실행    </button>>
                </p>
            </p>
            <p>
                <p><textarea name="message3" rows="2" cols="100" placeholder="여기에, 맨위의 내용을 바탕으로, 챗GPT에게 요청할 내용(프롬프트2)을 적어 넣으세요.(기본값은 , 일본어로 번역해줘 , 입니다) " >{2}</textarea>
                  <button type="submit" name="button" value="9">     프롬프트2 실행    </button>
                </p>
            </p>
            <p>
                <p><textarea name="message4" rows="6" cols="100" placeholder="여기에, 챗GPT에 의해 생성된 결과물이 표시 됩니다." >{3}</textarea>
                  <button type="submit" name="button" value="10">    &nbsp;  &nbsp; &nbsp; &nbsp;  저장2 &nbsp; &nbsp;  &nbsp;  &nbsp;   </button>
                
                </p>
                <p><button type="submit" name="button" value="13"> &nbsp; &nbsp;  &nbsp; &nbsp; 모두 클리어 &nbsp; &nbsp;  &nbsp; &nbsp; </button>
                  <button type="submit" name="button" value="14">  &nbsp;  &nbsp; &nbsp; 맨위로 덧붙임 &nbsp; &nbsp;  &nbsp; </button>
                  <button type="submit" name="button" value="15">  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;  맨위로  &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  </button>
                  <button type="submit" name="button" value="16">  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;   클리어  &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  </button></p>
            </p>
            
            <p style="color:white; font-size:20px;">위의 저장1 저장2 버튼을 누르면, 아래에 계속 누적되어, 내용이 저장이 됩니다. </p>
            

            <p>
                <p><textarea name="message5" rows="52" cols="100"  placeholder="여기에, 결과물이 차례대로 저장 됩니다." >{4}</textarea>
                  <button type="submit" name="button" value="20"> &nbsp; &nbsp;  &nbsp; &nbsp; 저장 &nbsp; &nbsp;  &nbsp; &nbsp;  </button>
                </p>
            </p>

            
        </form>
    '''.format(message, message2, message3, message4, message5, message6, message7, message8, message9, message10  )

if __name__ == '__main__':
    app.run()
