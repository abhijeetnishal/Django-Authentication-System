from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def signup(request):
    # try-except for error handling
    try:
        # Check for request method
        if request.method == 'POST':
            # Check if the request has a JSON payload
            if request.content_type == 'application/json':
                # Parse JSON data from the request body
                data = json.loads(request.body)

                # Extract user details from JSON data
                username, email, password = data.get('username'), data.get('email'), data.get('password')

                # Input validation
                if not username or len(username) == 0:
                    return JsonResponse({"error": "Enter a valid username"}, status=400)
                elif not email or len(email) == 0:
                    return JsonResponse({"error": "Enter a valid email"}, status=400)
                elif not password or len(password) == 0:
                    return JsonResponse({"error": "Enter a valid password"}, status=400)

                # Check if user already exists or not
                if User.objects.filter(email=email).first():
                    return JsonResponse({"error": "User already exists"}, status=400)

                else:
                    # Hash the password
                    hashed_password = make_password(password)

                    # Save user to the database
                    user = User(username=username, email=email, password=hashed_password)
                    user.save()

                    return JsonResponse({"message": f"User saved to DB"}, status=201)
            else:
                return JsonResponse({"error": "Request must be in JSON format"}, status=400)

        else:
            return JsonResponse({"error": "Invalid HTTP request method"}, status=500)
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)


@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            if request.content_type == 'application/json':
                # Parse JSON data from the request body
                data = json.loads(request.body)

                # Extract email and password from data
                email, password = data['email'], data['password']

                # Validate Input
                if (not email or len(email) == 0) or (not password or len(password) == 0):
                    return JsonResponse({"error": "Enter required details"}, status=400)
                else:
                    # Retrieve user based on username or email
                    userExists = User.objects.filter(email=email).first() 

                    # Check user registered or not
                    if userExists == None:
                        return JsonResponse({"error": "User not registered"}, status=404)
                    else:
                        # Check if the provided password matches the stored hashed password
                        if not check_password(password, userExists.password):
                            return JsonResponse({"error": "Incorrect password"}, status=401)
                        else:
                            return JsonResponse({"message": "User logged in"}, status=200)

            else:
                return JsonResponse({"error" : "Request must be in JSON format"}, status=400)
        else:
            return JsonResponse({"error": "Invalid HTTP request method"}, status= 500)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)