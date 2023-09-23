import openai
import os
from colorama import Fore, Style

class Assesment:
    openai.api_key = "API_KEY_HERE"
    openai.organization

    @staticmethod
    def generate_response(messages,temp):
        chat = openai.ChatCompletion.create(
            model= "gpt-3.5-turbo",
            messages=messages,
            n=1,
            stop=None,
            temperature=temp,
        )
        reply = chat.choices[0].message.content
        return {"role": "assistant", "content": reply}

    @staticmethod
    def genqs(age,personality):
        prompt=f""" Randonly Generate questions to ask a candidate to suggest him a career path that appropriate to age and personality type, i.e., {age} and {personality} respectively. Be brief about the questions to ask the candidate and have a very clear and accurate perception about what you are asking the candidate. Use these 7 categories to frame your questions around. 

        1. Leadership
        Leadership questions are common, especially for management jobs. Questions may involve “Describe a time you had to motivate an employee,” for example. Come up with examples of your leadership ahead so that you are prepared for leadership category questions.
 
        2. Negativity
        Behavioral questions about what you didn't like about people or the company are not uncommon. It is a good idea to draft out answers ahead of time so that you don't actually say something negative.
        
        3. Decision Making
        Decision making behavioral questions are very common. You will be asked about both good and bad decisions. Prepare several answers for each, making sure to pick things that aren't too negative.
 
        4. Professional Priorities
        There will be questions about your greatest achievements or questions about what you consider a professional regret, etc. These questions are not only about your work history, but are also designed to gauge what you consider important in your professional life.
 
        5. Problem Solving
        Problem solving behavioral questions are looking at the process you used to make a decision. The end result is not as important as the process used to get to that result. Questions may also include how you organize, since organization is a part of problem solving.
 
        6. Teamwork
        Your ability to work as a team is important for almost any job. Teamwork questions are going to ask you about your history of working with others, how you worked independently, etc.
 
        7. Communication
        Your ability to communicate effectively is important for the role. You may be asked behavioral questions that fall under this category as well.
        
        Just the generate the questions and not anything else as we want to avoid asking unnecessary things to the candidate.

        """
        messages=[
            {"role": "system", "content": prompt},
            {"role":"user", "content": f"""Based on the prompt given to the system RANDOMLY generate 10 interview questions from the 7 unique categories in the format already PROVIDED. Your response MUST BE only the 10 interview questions with labels 1.-10., There should be no other content in your response. DO NOT show the category of the question in the response."""}
        ]
        response = Assesment.generate_response(messages,0.3)
        return response['content']

    @staticmethod
    def start(name,age,questions,personality):
        prompt = f"""You are BrainyCounselor a chabot desinged to provide people with a career path based on the interview that you conduct as a chatbot. You are Reserved, empathetic and a person of a few words. You must take an interview of the candidate and wait for him to reply to the question you have asked, after receiving the reply, only then you can ask another question. 
         
        The interview that you are conducting is just for the general understanding of what career path to suggest the candidate and a roadmap to follow for the same. Maintain a CONVERSATIONAL tone throughout the interview, rather than keeping it only professional. During the interview ONLY ask the candidates questions but NEVER reply when they are asking for clarification regarding a question. ONLY focus on asking questions. DO NOT justify your answers. DO NOT generate and give information not mentioned in the CONTEXT INFORMATION.
         
        RULES FOR THE INTERVIEWER TO FOLLOW :    
            1. NEVER start your responses by having a character identifier. example if you are the interviewer no need to start your response by saying "Interviewer: ...."
            2. NEVER start your responses with "Assistant:", "Interviewer:" or "BrainyCounselor:" under any circumstances.
            3. ONLY ASK questions in the order given to you do not change the order. NEVER come up with your own questions which you might think are relevant under any circumstances. FOLLOW THESE INSTRUCTIONS AS IS!
            4. NEVER skip questions from the list, NEVER break the order of questions and DO NOT take candidate suggestions.
            5. ALWAYS start the interview with message: Hello {name}! How are you doing today?
            6. ALWAYS END the interview when the candidate answers the last question with this response "Thank you for your time, {name}. We will get back to you soon regarding the next steps in the hiring process. Have a great day!". Do not add any other content when ending the interview. NEVER END Interview with anything other than this message provided to you
            7. DO NOT move onto the next question until the current question is PROPERLY answered by the candidate. If the question is not answered tell the candidate their response was not clear.
            8. If the candidate say they do not know the answer(or anything with a similar meaning to "I don't know") to the question being asked, ALWAYS ask that they are sure if this is their answer. If they still do not know the answer after the clarification move onto next question.
            9. NEVER imply that you will answer the candidate's questions.
            10. NEVER alter the question asked, it should always mean the same.
            11. ALWAYS have a smooth transition when moving from one question to the next question.
            12. NEVER thank the candidate for responses, ONLY acknowledge the candidate response within 5 words. When the candidate response is relevant and admirable to the question, ACKNOWLEDGE it with positive affirmation. When the candidate response is irrelevant and/or doesn't make sense(or they don't know) to the question, ACKNOWLEDGE it with some constructive affirmation without negative feedbacks after the verification.
            
        Also as another KEY POINT you can ask for more details or a follow up question if required from the candidate.
        Sample:
            ```
        Assistant: Tell me about your experience ?
        User: I have 2 years of experience
        Assistant: Please elaborate
        User: I have 2 years of experience in Python
            ```
        Both of the questions above will be considered as one question only.
    
        Keep the questions dynamic and drive the interview around Technical, Behavioral, and Situational type questions given to you 
            
        QLIST(List of Questions to ask):
        ```
        {questions}
        ```

        The personality type of the candidate and his age is:
        ```
        {personality} and {age} respectively

        IMPORTANT:
        NEVER justify your answers. NEVER generate and/or give information not mentioned in the CONTEXT. ALWAYS SPECIFY THE QUESTIONS AS FIRST, SECOND, 1, 2, etc. NEVER END THE INTERVIEW UNTIL ALL QUESTIONS ARE ANSWERED.
        """ 