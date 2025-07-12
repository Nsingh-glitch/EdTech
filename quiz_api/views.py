from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os
import json
from django.http import JsonResponse

def progress(request):
     return render(request, 'accounts/progress.html')

def quiz_view(request):
    return render(request, 'accounts/quiz.html')


def get_ai_response(user_query):
    # Simulating an AI response (Replace this with actual AI integration)
    responses = {
        "hello": "Hello! How can I assist you?",
        "what is AI?": "AI stands for Artificial Intelligence. It enables machines to learn from data and perform tasks.",
        "who created python?": "Python was created by Guido van Rossum in 1991."
    }
    return responses.get(user_query.lower(), "I'm not sure about that. Could you ask in a different way?")





TOGETHER_AI_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_AI_API_KEY="8e3f2af35e5b354247e92348dae585a085382ba234e155357e4d59d26cee4bb5"
# @api_view(['POST'])
@api_view(['GET'])
def chat_gpt(request):
    # data = request.data
    # query = data.get('query', '')
    # user_id = data.get('user_id')
    # quiz_id = data.get('quiz_id')
    # responses = data.get('responses', [])
    
    # if not user_id or not quiz_id or not responses:
    #     return Response({'error': 'user_id, quiz_id, and responses are required'}, status=400)
    # if not query:
    #     return Response({'error': 'Query parameter is required'}, status=400)

    user_id = 123
    quiz_id = 456
    responses = [
        {"question_id": 1, "selected_option": "B", "is_correct": True, "time_taken": 12},
        {"question_id": 2, "selected_option": "C", "is_correct": False, "time_taken": 8},
        {"question_id": 3, "selected_option": "A", "is_correct": True, "time_taken": 15}
    ]



    prompt = f"""
    Analyze the quiz performance of User ID: {user_id} for Quiz ID: {quiz_id}.
    
    Here are the responses:
    {responses}

    Generate a progress report including:
    - Total questions attempted
    - Number of correct and incorrect answers
    - Accuracy percentage
    - Average time per question
    - Strengths and weaknesses
    - Suggestions for improvement

    **Return ONLY a valid JSON object. Do not include explanations, markdown, or text.** 
    return like this :
    "score": 8,
    "total_questions": 10,
    "performance_message": "Good job! Keep practicing!",
    "weak_topics": ["Physics", "Math"]
        


    Format the response in JSON format.
    """






    headers = {
        "Authorization": f"Bearer {TOGETHER_AI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}]
    }


    try:
        response = requests.post(TOGETHER_AI_URL, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            ai_generated_text = response_data['choices'][0]['message']['content']

            try:
                parsed_json = json.loads(ai_generated_text)
                # return Response({'progress_report': parsed_json})
                return Response(parsed_json)
            except json.JSONDecodeError:
                return Response({'error': 'Invalid JSON format from AI', 'raw_response': ai_generated_text}, status=500 )

        else:
            return Response({'error': response_data.get('error', 'Unknown error')}, status=response.status_code)
    

                
                # if response.status_code == 200:
                #     return Response({'response': response_data['choices'][0]['message']['content']})
                # else:
                #     return Response({'error': response_data.get('error', 'Unknown error')}, status=response.status_code)
    except Exception as e:
        return Response({'error': str(e)}, status=500)








def quiz_progress_api(request):
    # Hardcoded sample response
    response_data = {
        "score": 7,  # Hardcoded example score
        "total_questions": 10,
        "weak_topics": ["Physics - Newton’s Laws", "Math - Quadratic Equations"],
        "achievements": ["Smart Learner 📚"],
        "percentage": 70
    }
    return JsonResponse(response_data)