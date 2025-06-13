from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import json
import uuid
import logging
import random
import importlib.util
from utils.math_solver import solve_math_problem, get_similar_problems
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_bcrypt import Bcrypt
import json
import os

import logging
import random
import importlib.util
from utils.domain_prompts import get_domain_prompt
from utils.shared import solve_problem_interface, generate_similar_problems_interface, recommend_topics_interface
from application_routes import app as app_routes
from flask import Flask, request, render_template, jsonify
import os
import uuid
from utils.math_solver import solve_math_problem, get_similar_problems
from langchain.memory import ConversationBufferMemory

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
mail = Mail(app)

# Initialize LangChain memory
memory = ConversationBufferMemory()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('quiz.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Available levels
LEVELS = {
    "1": {"name": "Tronc Commun", "module": "math_quiz_tronc_commun", "threshold": 14, "questions_per_topic": 20},
    "2": {"name": "Premier Bac", "module": "math_quiz_premier_bac", "threshold": 7, "questions_per_topic": 10},
    "3": {"name": "Terminale", "module": "math_quiz_terminale", "threshold": 7, "questions_per_topic": 10}
}


RECOMMENDATIONS = {
    "Tronc Commun": {
        "Ensembles de nombres": "https://www.youtube.com/playlist?list=PLIJfenLlfjW_Rhko9ZHIQvst7FKeEQoNo",
        "Arithmétique dans N": "https://www.youtube.com/watch?v=zlFjeTqldys&list=PLX4JM5un62hA-6CnE9WU-P0y4yyv5NPdW",
        "Calcul vectoriel dans le plan": "https://www.youtube.com/watch?v=N2cM6UevpUQ&list=PLLYc1VjflHSB3B7T-984kmiu5hrc0B-r5",
        "ProjectionLa projection dans le plan": "https://www.youtube.com/watch?v=GsZd1kQgB_Y&list=PLpJ48ZvxMJM31YZn2efxCxpD4G9ZUdS79",
        "Ordre dans ℝ": "https://www.youtube.com/watch?v=PSl_Cu5OeLs&list=PLLYc1VjflHSDFuyJn-SLdTo9yWVK27S__",
        "Droite dans le plan": "https://www.youtube.com/watch?v=d-rUnClmcCY&list=PLVUDmbpupCapf-dGL1hVU0grzGRrGnz1q",
        "Polynômes": "https://www.youtube.com/watch?v=dDKI3jkMjfw&list=PL024XGD7WCIHMAwUrUW5BAmHu-EiuO9nU",
        "Équations et systèmes": "https://www.youtube.com/watch?v=teZikZbqKHk&list=PLLYc1VjflHSD_pdYITsdpu7P9ihItYl-D",
        "Trigonométrie 1 (Règles du calcul trigonométrique)": "https://www.youtube.com/watch?v=tvt9cECTSH4&list=PLuj_W_ckIDLJgccE1Fzt9nbJOIGbX_Ntv",
        "Trigonométrie 2 (Identités et équations trigonométriques)": "https://www.youtube.com/watch?v=iXdSMiuPPb8&list=PLLYc1VjflHSCTNQ9mTqWNAGfm-04JRbE4",
        "Généralités sur les fonctions": "https://www.youtube.com/watch?v=3UATeEoIyuw&list=PLJ99nvBc0N-lczXjMGRoVYcajYYQd5NeT",
        "Transformations": "https://www.youtube.com/watch?v=4hACSwA1cn4&list=PLVUDmbpupCaoE3tQlqACo974XeL2r3eRJ",
        "Produit scalaire": "https://www.youtube.com/watch?v=nmjXcSc3dVg&list=PLX4JM5un62hAy0y2sr5NXisCP5k_mD_v4",
        "Géométrie dans l'espace": "https://www.youtube.com/watch?v=6hjlLk99Vvs&list=PLLYc1VjflHSAGANcAtk9QfFoVdl3yjZXi",
        "Statistiques": "https://www.youtube.com/watch?v=yTtbC1velyk"
    },
    "Premier Bac": {
        "Logique mathématique": "https://www.youtube.com/watch?v=qYniDwFnI1c&list=PLn3XTgvZWCizWCCmr1qGvp2latwJXqJej",
        "Ensembles et applications": "https://www.youtube.com/watch?v=JVyr2ZsfOnk&list=PLhtIEyVuroV0lmh2tmWNQ8M9t9c8n0jrt",
        "Généralités sur les fonctions": "https://www.youtube.com/watch?v=CSLp-wYArlE&list=PLJ99nvBc0N-n-aFiYnm2onm96oaCqRK6K",
        "barycentre dans le plan": "https://www.youtube.com/watch?v=4mX2Dc8LBLI&list=PLX4JM5un62hBhgfG6z8LwrI61qPzVRRjy",
        "produit scalaire dans le plan": "https://www.youtube.com/watch?v=W9i6Jlzuydk&list=PL0Kwtl4gdC_UTo353iFq8gFeMsfX8v58X",
        "Calcul trigonométrique": "https://www.youtube.com/watch?v=9CJrhefj7VM&list=PLX4JM5un62hBGxkd8OkgALTXK1UZqQ_xC",
        "Les suites numériques": "https://www.youtube.com/watch?v=f-okOBwvGWk&list=PLJ99nvBc0N-nFQh3vRcF4DA_9rudFbFBc",
        "Limites d’une fonction": "https://www.youtube.com/watch?v=ZYq6cBBSwa4&list=PLJ99nvBc0N-nVgSVdKzfz2oaf3VBZYI1K",
        "La rotation dans le plan": "https://www.youtube.com/watch?v=huMV-mixKz8",
        "La dérivation": "https://www.youtube.com/watch?v=t6QJ7E5_ubE&list=PLgOzo-YcXOhBhA_CvkvowjY1qDO9Z0dcO",
        "Étude des fonctions": "https://www.youtube.com/watch?v=T02FJWLWvgQ&list=PLX4JM5un62hArVQl15KsMUUrQFUWnpZLa" ,
        "Vecteurs de l’espace": "https://www.youtube.com/watch?v=SCDTHjKyuSo&list=PLUfJOEwIb2c45haqHMQia8ct7D1E4wQ1y",
        "Géométrie dans l’espace": "https://www.youtube.com/watch?v=loNWY2kktnA&list=PLX4JM5un62hC6eL55XJ41E6jZNzcgGkNm",
        "Dénombrement": "https://www.youtube.com/watch?v=yODTn0TfAak&list=PLM8_G-VemRDFm2WkSSopIBJA-IHzj872-",
        "produit scalaire dans l'espace": "https://www.youtube.com/watch?v=QeOoSKyL_dw&list=PL_ZtK1TB2InrsTa3NZQH4i6TIJ3mSz1l0",
        "Arithmétique dans Z": "https://www.youtube.com/watch?v=BVvaflLfjCU&list=PLgOzo-YcXOhA_Sq_c5WVPFdaZOxwtDRhq",
        "produit vectoriel": "https://www.youtube.com/watch?v=2NxriGOFpsA&list=PLhwheJMLOsDBSkxQTXYf0JsjNAZxoe8SG",
    },
    "Terminale": {
        "Limites et continuité": "https://www.youtube.com/watch?v=XcLTzql_v9g&list=PLWDP1k6hCnoQkQ6ILBkiGh20L0-zK8Hz7",
        "Dérivation et étude des fonctions": "https://www.youtube.com/watch?v=T02FJWLWvgQ&list=PLX4JM5un62hArVQl15KsMUUrQFUWnpZLa",
        "Suites numériques": "https://www.youtube.com/watch?v=pA2XEI1Uv_s&list=PLPMCOIL54o6Wf82b8EGrOCdlXstx16WX2",
        "Fonctions primitives": "https://www.youtube.com/watch?v=MLVMYPY_lFE&list=PLJ99nvBc0N-kbh9lCREW0aJ06762fFhyF",
        "Fonctions logarithmiques": "https://www.youtube.com/watch?v=axAZHCBbHPk&list=PLJ99nvBc0N-lD1eLWECLmy-uZ8on-oVc2",
        "Nombres complexes": "https://www.youtube.com/watch?v=lBDkhzI-bIQ&list=PLJ99nvBc0N-m_UqZH_LJK5d6KXS54nf5k",
        "Fonctions exponentielles": "https://www.youtube.com/watch?v=BeiZrSiUS_w&list=PLJ99nvBc0N-mtWhmFWeal3uvLnHbxPow5",
        "Calcul intégral": "https://www.youtube.com/watch?v=zm8Dy4fbtFA&list=PLJ99nvBc0N-kFTiqTRTwYf3jEPqtYYdVz",
        "Équations différentielles": "https://www.youtube.com/watch?v=LX8PxR-ScfM&list=PLdz4lhk1rRmNsBJMBti9DQBNcjP7hdGpZ",
        "Géométrie dans l’espace": "https://www.youtube.com/watch?v=FqTYa6NONwY&list=PLX4JM5un62hBhgv-49WulGlHiYSsBVoKI",
        "Dénombrement et probabilités": "https://www.youtube.com/watch?v=6_Rt-P_Mtec&list=PLPMCOIL54o6UJUJ42QnD1hRQx0ar-kp93"
    }
}

USER_DATA_FILE = "user_data.json"

# Ensure the user data file exists
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)

# Load users
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Save users
def save_users(users):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

# Load scores
def load_scores():
    if os.path.exists("scores_math_quiz.json"):
        with open("scores_math_quiz.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Save scores
def save_scores(scores):
    with open("scores_math_quiz.json", "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4, ensure_ascii=False)

def load_user_data():
    """Load data for all users."""
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_user_data(data):
    """Save data for all users with UTF-8 encoding."""
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Recommend starting point
def recommend_starting_point(level_name, scores_by_topic, threshold):
    min_score_value = float('inf')
    weakest_topic = None

    # Identify the weakest topic based on scores
    for topic, data in scores_by_topic.items():
        if data["total"] == 0:
            continue
        if data["score"] < threshold and data["score"] < min_score_value:
            min_score_value = data["score"]
            weakest_topic = topic

    # Fetch YouTube link for the weakest topic
    if weakest_topic:
        youtube_link = RECOMMENDATIONS.get(level_name, {}).get(weakest_topic)
        if youtube_link:
            return weakest_topic, youtube_link
        else:
            return weakest_topic, f"Aucun lien trouvé pour le sujet faible: {weakest_topic}"
    else:
        return None, "Félicitations ! Vous avez réussi tous les modules ou aucun test n’a été complété."

@app.route("/")
def home():
    if 'username' in session:
        return redirect(url_for('select_level'))
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'username' in session:
        return redirect(url_for('select_level'))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        if username in users and bcrypt.check_password_hash(users[username]["password"], password):
            session['username'] = username
            session['student_id'] = users[username]["student_id"]
            logger.info(f"User {username} logged in")
            flash("Connexion réussie !", "success")
            return redirect(url_for('select_level'))
        else:
            logger.warning(f"Failed login for {username}")
            flash("Identifiant ou mot de passe incorrect.", "error")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if 'username' in session:
        return redirect(url_for('select_level'))

    if request.method == "POST":
        email = request.form.get('email')
        confirmation_code = request.form.get('confirmationCode')

        if 'confirmation_code' not in session:
            # Generate and send confirmation code
            code = str(random.randint(100000, 999999))
            session['confirmation_code'] = code
            session['email'] = email

            msg = Message('Votre code de confirmation',
                          sender='your_email@example.com',
                          recipients=[email])
            msg.body = f'Votre code de confirmation est : {code}'
            mail.send(msg)
            flash('Un code de confirmation a été envoyé à votre adresse e-mail.', 'success')
            return redirect(url_for('register'))

        # Verify confirmation code
        if confirmation_code != session.get('confirmation_code'):
            flash('Code de confirmation incorrect.', 'error')
            return redirect(url_for('register'))

        # Proceed with registration logic
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        if username in users:
            logger.warning(f"Registration failed: {username} exists")
            flash("Nom d'utilisateur déjà pris.", "error")
            return redirect(url_for("register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        users[username] = {
            "password": hashed_password,
            "student_id": str(uuid.uuid4())
        }
        save_users(users)
        logger.info(f"User {username} registered successfully")
        flash("Inscription réussie !", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout")
def logout():
    username = session.get('username', 'unknown')
    session.clear()
    logger.info(f"User {username} logged out")
    flash("Vous êtes déconnecté.", "success")
    return redirect(url_for('login'))

@app.route("/select_level", methods=["GET", "POST"])
def select_level():
    if 'username' not in session:
        logger.warning("select_level: No user logged in")
        flash("Veuillez vous connecter.", "error")
        return redirect(url_for('login'))
    if request.method == "POST":
        level = request.form.get("level")
        if level in LEVELS:
            session['level'] = level
            session['scores_by_topic'] = {}
            session['current_topic_index'] = 0
            session['current_question_index'] = 0
            session['questions_by_topic'] = {}
            session['topics'] = []
            logger.info(f"User {session['username']} selected level {LEVELS[level]['name']}")
            flash(f"Quiz pour {LEVELS[level]['name']} démarré !", "success")
            return redirect(url_for('quiz'))
        else:
            logger.warning(f"Invalid level: {level}")
            flash("Niveau invalide.", "error")
    return render_template("select_level.html", levels=LEVELS)

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if 'username' not in session or 'level' not in session:
        logger.warning("quiz: No user or level")
        flash("Veuillez vous connecter et choisir un niveau.", "error")
        return redirect(url_for('login'))
    
    level = session['level']
    student_id = session['student_id']
    
    # Load questions if not set
    if not session.get('questions_by_topic'):
        try:
            scores_by_topic, questions_by_topic = load_questions(level, student_id)
            if not questions_by_topic or all(len(q) == 0 for q in questions_by_topic.values()):
                logger.error(f"No questions for {LEVELS[level]['name']}")
                flash(f"Aucune question disponible pour {LEVELS[level]['name']}. Vérifiez {LEVELS[level]['module']}.py.", "error")
                return redirect(url_for('select_level'))
            session['scores_by_topic'] = scores_by_topic
            session['questions_by_topic'] = questions_by_topic
            session['topics'] = list(questions_by_topic.keys())
            logger.info(f"Loaded {sum(len(q) for q in questions_by_topic.values())} questions for {LEVELS[level]['name']}")
        except Exception as e:
            logger.error(f"Error loading questions for {LEVELS[level]['name']}: {str(e)}")
            flash(f"Erreur : {str(e)}", "error")
            return redirect(url_for('select_level'))
    
    topics = session['topics']
    current_topic_index = session.get('current_topic_index', 0)
    
    if not topics or current_topic_index >= len(topics):
        logger.info(f"Quiz completed for {session['username']}")
        return redirect(url_for('results'))
    
    current_topic = topics[current_topic_index]
    questions = session['questions_by_topic'][current_topic]
    current_question_index = session.get('current_question_index', 0)

    if not questions or current_question_index >= len(questions):
        logger.info(f"Completed topic {current_topic}")
        session['current_topic_index'] = current_topic_index + 1
        session['current_question_index'] = 0
        return redirect(url_for('quiz'))
    
    question_data = questions[current_question_index]
    options = question_data['options'].copy()
    random.shuffle(options)
    
    if request.method == "POST":
        selected_option = request.form.get("answer")
        correct_answer = question_data['correct']
        scores_by_topic = session['scores_by_topic']
        
        if selected_option == correct_answer:
            scores_by_topic[current_topic]['score'] += 1
            flash("Correct !", "success")
            logger.debug(f"Correct answer for {current_topic}, Q{current_question_index + 1}")
        else:
            flash(f"Incorrect. Réponse : {correct_answer}. Explication : {question_data['explanation']}", "error")
            logger.debug(f"Incorrect answer for {current_topic}, Q{current_question_index + 1}")
        
        scores_by_topic[current_topic]['total'] += 1
        session['scores_by_topic'] = scores_by_topic
        session['current_question_index'] = current_question_index + 1
        
        # Save scores
        try:
            scores = load_scores()
            if student_id not in scores:
                scores[student_id] = {}
            if LEVELS[level]['name'] not in scores[student_id]:
                scores[student_id][LEVELS[level]['name']] = {}
            scores[student_id][LEVELS[level]['name']].update(scores_by_topic)
            save_scores(scores)
            logger.info(f"Scores saved for {session['username']}")
        except Exception as e:
            logger.error(f"Error saving scores: {str(e)}")
            flash("Erreur lors de l’enregistrement des scores.", "error")
        
        return redirect(url_for('quiz'))
    
    logger.debug(f"Displaying {current_topic}, Q{current_question_index + 1}: {question_data['question']}")
    return render_template(
        "quiz.html",
        question=question_data['question'],
        options=options,
        topic=current_topic,
        question_number=current_question_index + 1,
        total_questions=len(questions)
    )

@app.route("/chat", methods=["GET", "POST"])
def chat():
    username = session.get("username")
    if not username:
        return jsonify({"error": "User not logged in"}), 401

    user_data = load_user_data()
    user_info = user_data.get(username, {})

    # Extract user details
    user_name = user_info.get("name", "Unknown")
    user_level = user_info.get("level", "Unknown")
    user_starting_point = user_info.get("starting_point", "Unknown")

    if request.method == "POST":
        problem_text = request.form.get("problem_text", "")
        domain = request.form.get("domain", None)

        if not problem_text:
            flash("Please enter a math problem to solve.", "error")
            return render_template("chat.html", chat_context=chat_context)

        solution = solve_problem_interface(problem_text, domain)

        # Save conversation history for the user
        user_data = load_user_data()
        if username not in user_data:
            user_data[username] = {"history": []}
        user_data[username]["history"].append({"problem": problem_text, "solution": solution})
        save_user_data(user_data)

        return render_template("chat.html", problem=problem_text, solution=solution, chat_context=chat_context)

    # Pass user details to the chat context
    chat_context = {
        'name': user_name,
        'level': user_level,
        'starting_point': user_starting_point,
        'history': memory.load_memory_variables({})
    }

    return render_template("chat.html", chat_context=chat_context)

@app.route("/results")
def results():
    """Display quiz results and save user profile."""
    if 'username' not in session or 'level' not in session:
        logger.warning("results: No user or level")
        flash("Veuillez vous connecter et choisir un niveau.", "error")
        return redirect(url_for('login'))

    username = session['username']
    level = session['level']
    level_name = LEVELS[level]['name']
    scores_by_topic = session.get('scores_by_topic', {})
    threshold = LEVELS[level]['threshold']

    weakest_topic, recommendation = recommend_starting_point(level_name, scores_by_topic, threshold)
    logger.info(f"Results for {username}, weakest: {weakest_topic}")

    # Load user data
    user_data = load_user_data()
    if username not in user_data:
        user_data[username] = {}

    # Save user profile
    user_data[username]['name'] = username
    user_data[username]['level'] = level_name
    user_data[username]['scores'] = scores_by_topic
    user_data[username]['recommendation'] = recommendation
    user_data[username]['starting_point'] = weakest_topic
    save_user_data(user_data)

    flash("Quiz completed! View your profile for details.", "success")
    return redirect(url_for("profile"))

def load_questions(level, student_id):
    """Load questions for the selected level."""
    module_name = LEVELS[level]['module']
    try:
        # Check if file exists
        if not os.path.exists(f"{module_name}.py"):
            logger.error(f"File {module_name}.py not found")
            raise FileNotFoundError(f"File {module_name}.py not found")
        
        logger.debug(f"Attempting to import {module_name}.py")
        spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
        if spec is None:
            logger.error(f"Failed to create spec for {module_name}.py")
            raise ImportError(f"Cannot create spec for {module_name}.py")
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        questions_by_topic = getattr(module, 'questions_by_topic', None) or {}
        if not questions_by_topic:
            logger.warning(f"questions_by_topic not found or empty in {module_name}.py")
            questions_by_topic = {"default": []}
        
        logger.debug(f"questions_by_topic keys: {list(questions_by_topic.keys())}")
        scores_by_topic = {}
        questions_by_topic_out = {}
        
        if not questions_by_topic:
            logger.error(f"questions_by_topic is empty in {module_name}.py")
            raise ValueError(f"questions_by_topic is empty in {module_name}")
        
        for topic in questions_by_topic:
            available_questions = questions_by_topic[topic].copy()
            logger.debug(f"Topic {topic}: {len(available_questions)} questions")
            if not available_questions:
                logger.warning(f"No questions for {topic} in {LEVELS[level]['name']}")
                scores_by_topic[topic] = {"score": 0, "total": 0}
                questions_by_topic_out[topic] = []
                continue
            random.shuffle(available_questions)
            questions_to_ask = min(LEVELS[level]['questions_per_topic'], len(available_questions))
            selected_questions = available_questions[:questions_to_ask]
            scores_by_topic[topic] = {"score": 0, "total": 0}
            questions_by_topic_out[topic] = selected_questions
            logger.debug(f"Loaded {len(selected_questions)} questions for {topic}")
        
        if not any(questions_by_topic_out.values()):
            logger.error(f"No valid questions loaded for {LEVELS[level]['name']}")
            raise ValueError(f"No valid questions for {LEVELS[level]['name']}")
        
        return scores_by_topic, questions_by_topic_out
    except Exception as e:
        logger.error(f"Failed to load questions for {LEVELS[level]['name']}: {str(e)}")
        raise

def access_app_routes():
    """Access routes defined in application_routes.py"""
    from application_routes import app
    return app

def access_math_solver():
    """Access functions from math_solver.py"""
    from utils.math_solver import solve_math_problem, get_similar_problems
    return solve_math_problem, get_similar_problems

def access_templates():
    """Access templates for rendering"""
    import os
    templates_dir = os.path.join(os.getcwd(), 'templates')
    return templates_dir

def access_static_files():
    """Access static files like CSS and JS"""
    import os
    static_dir = os.path.join(os.getcwd(), 'static')
    return static_dir

def access_utils():
    """Access utility files like domain_prompts.py"""
    from utils.domain_prompts import get_prompts
    return get_prompts

@app.route('/start_app', methods=['POST'])
def start_app_route():
    """Handle requests to start the application"""
    try:
        # Logic to start the application
        return jsonify({'message': 'Application is already running.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/link_files', methods=['GET'])
def link_files():
    """Link all files in the project"""
    try:
        files = {
            'templates': access_templates(),
            'static': access_static_files(),
            'utils': {
                'domain_prompts': get_domain_prompt(),
                'math_solver': {
                    'solve': solve_problem_interface,
                    'similar': generate_similar_problems_interface
                }
            },
            'routes': app_routes.url_map
        }
        return jsonify({'linked_files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    """Solve a math problem from text or image"""
    try:
        # Check if image was uploaded
        if 'problem_image' in request.files and request.files['problem_image'].filename != '':
            # Process image input
            image_file = request.files['problem_image']
            
            # Create a unique filename
            filename = str(uuid.uuid4()) + os.path.splitext(image_file.filename)[1]
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            
            # Save the image
            image_file.save(image_path)
            
            # Extract text from image
            # problem_text = extract_text_from_image(image_path)
            
            # Clean up the image file
            os.remove(image_path)
            
        else:
            # Process text input
            problem_text = request.form.get('problem_text', '')
        
        # Get domain if specified
        domain = request.form.get('domain', None)
        
        # Solve the problem
        if not problem_text:
            return jsonify({
                'error': 'No valid input provided. Please enter a math problem or upload an image.'
            }), 400
            
        solution = solve_math_problem(problem_text, domain)
        
        return jsonify({
            'problem': problem_text,
            'solution': solution
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/similar', methods=['POST'])
def similar():
    """Generate similar math problems"""
    try:
        problem_text = request.form.get('problem_text', '')
        domain = request.form.get('domain', None)
        if not problem_text:
            return jsonify({'error': 'No problem text provided.'}), 400
        similar_problems = get_similar_problems(problem_text, domain)
        return jsonify({'similar_problems': similar_problems})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/profile')
def profile():
    if 'username' not in session:
        flash("Veuillez vous connecter.", "error")
        return redirect(url_for('login'))

    username = session['username']
    user_data = load_user_data()

    if username not in user_data:
        flash("Profil utilisateur introuvable.", "error")
        return redirect(url_for('home'))

    return render_template('profil.html', user_data=user_data[username])

@app.route('/generate_course', methods=['POST'])
def generate_course():
    """Generate a course based on the user's starting point and level."""
    try:
        username = session.get('username')
        if not username:
            return jsonify({'error': 'User not logged in'}), 401

        user_data = load_user_data()
        user_info = user_data.get(username, {})

        # Extract user details
        user_starting_point = user_info.get('starting_point', 'Unknown')
        user_level = user_info.get('level', 'Unknown')

        # Generate course content using the new function
        from utils.math_solver import generate_course_content
        course_content = generate_course_content(user_level, user_starting_point)

        return jsonify({
            'starting_point': user_starting_point,
            'level': user_level,
            'content': course_content
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-cours.html', methods=['GET'])
def generate_cours_page():
    return render_template('generate-cours.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)