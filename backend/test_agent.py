from app.services.agent import generate_rebuttal

argument = "Everyone should work remotely forever."

response = generate_rebuttal(argument)

print(response)