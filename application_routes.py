from flask import Flask, request, render_template, jsonify
import os
import uuid
from utils.shared import solve_problem_interface, generate_similar_problems_interface, recommend_topics_interface
from langchain.memory import ConversationBufferMemory

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize memory
memory = ConversationBufferMemory()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    """Solve a math problem from text or image"""
    try:
        problem_text = request.form.get('problem_text', '')
        domain = request.form.get('domain', None)

        if not problem_text:
            return jsonify({'error': 'No valid input provided. Please enter a math problem or upload an image.'}), 400

        solution = solve_problem_interface(problem_text, domain)
        memory.save_context({'input': problem_text}, {'output': solution})

        return jsonify({'problem': problem_text, 'solution': solution})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/similar', methods=['POST'])
def similar():
    """Generate similar math problems"""
    try:
        problem_text = request.form.get('problem_text', '')
        domain = request.form.get('domain', None)

        if not problem_text:
            return jsonify({'error': 'No problem text provided.'}), 400

        similar_problems = generate_similar_problems_interface(problem_text, domain)
        memory.save_context({'input': problem_text}, {'output': similar_problems})
        return jsonify({'similar_problems': similar_problems})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend', methods=['POST'])
def recommend():
    """Recommend math topics and provide tutoring based on quiz results"""
    try:
        scores = request.json.get('scores', {})
        level = request.json.get('level', None)  # Get user level

        if not scores:
            return jsonify({'error': 'No scores provided.'}), 400

        if level == 'Terminale':
            # Call the function from math_quiz_unified_interface for Terminale level tutoring
            llm_response = recommend_topics_interface(scores, level)
            return jsonify({'chat': llm_response})

        recommendations = recommend_topics_interface(scores)
        return jsonify({'recommendations': recommendations})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)