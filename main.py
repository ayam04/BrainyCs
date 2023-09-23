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
    def start():
        hj