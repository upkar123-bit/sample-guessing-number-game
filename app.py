from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Global variable to store the number to guess
number_to_guess = random.randint(1, 100)

@app.route('/')
def home():
    return "🎯 Welcome to the Guessing Number Game! Send your guess to /guess"

@app.route('/guess', methods=['POST'])
def guess_number():
    global number_to_guess
    data = request.get_json()
    
    if not data or 'number' not in data:
        return jsonify({'error': 'Please provide a number in JSON, e.g., {"number": 42}'}), 400
    
    try:
        guess = int(data['number'])
    except ValueError:
        return jsonify({'error': 'Number must be an integer'}), 400
    
    if guess < number_to_guess:
        return jsonify({'result': 'Too low!'})
    elif guess > number_to_guess:
        return jsonify({'result': 'Too high!'})
    else:
        # Reset the game after correct guess
        number_to_guess = random.randint(1, 100)
        return jsonify({'result': 'Correct! New number generated, keep playing!'})


if __name__ == '__main__':
    # Run Flask development server (0.0.0.0 so Docker exposes it)
    app.run(host='0.0.0.0', port=5000, debug=True)

