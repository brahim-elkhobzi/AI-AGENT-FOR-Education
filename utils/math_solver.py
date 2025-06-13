from groq import Groq
import os
import logging
from dotenv import load_dotenv
from .domain_prompts import get_domain_prompt
from langchain.memory import ConversationBufferMemory
import json
from flask import session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
GROQ_API_KEY = GROQ_API_KEY = "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"

# Initialize Groq client
client = None
try:
    from groq import Client
    client = Client(api_key="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")
except ImportError:
    client = None
    logger.error("Failed to import Groq client. Please install the Groq library.")

# Initialize LangChain memory
memory = ConversationBufferMemory()

def save_conversation_to_file(problem_text, solution):
    """Save conversation history to conversation_data.json dynamically."""
    file_path = "c:\\Users\\brahi\\OneDrive\\Desktop\\AI-Agent\\conversation_data.json"
    username = session.get("username", "unknown")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            conversation_data = json.load(f)
        
        if username not in conversation_data:
            conversation_data[username] = {"name": username, "level": "Unknown", "conversation_history": []}
        
        # Update user level dynamically
        user_level = session.get("level", "Unknown")
        conversation_data[username]["level"] = user_level
        
        conversation_data[username]["conversation_history"].append({"problem": problem_text, "solution": solution})
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(conversation_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Failed to save conversation: {str(e)}")

# Update solve_math_problem to save conversation history dynamically
def solve_math_problem(problem_text, domain=None):
    """Solve a math problem using Groq API"""
    if not problem_text:
        logger.error("Problem text is empty. Cannot solve math problem.")
        return "Error: Problem text is required to solve the problem."

    if client is None:
        logger.error("Groq client not initialized. Please check your API key.")
        return "Error: Groq client not initialized. Please check your API key."

    try:
        # Auto-detect domain if not specified
        if domain is None:
            domain = detect_math_domain(problem_text)

        # Get domain-specific prompt
        system_prompt = get_domain_prompt(domain)

        # Format the problem
        formatted_problem = f"Solve this mathematics problem step-by-step:\n\n{problem_text}"

        # Call Groq API with Claude model
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": formatted_problem}
            ],
            temperature=0.2,
            max_tokens=4000
        )

        solution = completion.choices[0].message.content
        logger.info(f"Generated solution for {domain} problem") 

        # Save conversation history using LangChain memory
        memory.save_context(
            {"input": formatted_problem},
            {"output": solution}
        )

        # Save conversation to file dynamically
        save_conversation_to_file(problem_text, solution)

        return solution

    except Exception as e:
        logger.error(f"Error solving math problem: {str(e)}")
        return f"Error solving math problem: {str(e)}"

def detect_math_domain(problem_text):
    """Simple heuristic to detect math domain based on keywords"""
    problem_text = problem_text.lower()
    
    if any(kw in problem_text for kw in ["derivative", "integral", "differentiate", "integrate", "limit"]):
        return "calculus"
    elif any(kw in problem_text for kw in ["matrix", "vector", "linear", "determinant", "eigenvalue", "eigenvector", "span"]):
        return "linear_algebra"
    elif any(kw in problem_text for kw in ["probability", "distribution", "random", "variance", "standard deviation", "mean", "median", "hypothesis"]):
        return "statistics"
    elif any(kw in problem_text for kw in ["differential equation", "ode", "pde", "solve for y", "d/dx", "∂/∂t"]):
        return "differential_equations"
    else:
        return "general"

def get_similar_problems(problem_text, domain, n=3):
    """Generate similar math problems using Groq API"""
    if client is None:
        return ["Error: Groq client not initialized. Please check your API key."]
    try:
        if not domain:
            return ["Error: Domain must be explicitly provided."]

        system_prompt = get_domain_prompt(domain)

        user_prompt = (
            f"Given the following math problem, generate {n} similar but distinct problems "
            f"of the same type and difficulty. Only output the problems, numbered:\n\n"
            f"Original problem:\n{problem_text}"
        )
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        response = completion.choices[0].message.content
        # Extract the problems as a list
        problems = [line.strip() for line in response.split('\n') if line.strip() and (line.strip()[0].isdigit() or line.strip().startswith('-'))]
        return problems if problems else [response]
    except Exception as e:
        logger.error(f"Error generating similar problems: {str(e)}")
        return [f"Error generating similar problems: {str(e)}"]

def generate_course_content(level, starting_point, include_progress=False):
    """
    Génère un cours de mathématiques structuré et détaillé, adapté au système éducatif marocain.

    Args:
        level (str): Niveau scolaire ('Tronc Commun', 'Premier Bac', 'Terminale').
        starting_point (str): Thème du cours (ex: 'Dénombrement et probabilités').
        include_progress (bool): Optionnel. Inclure des repères de progression pour suivi.

    Returns:
        str: Contenu du cours au format Markdown, structuré pédagogiquement.
    """

    valid_levels = ["Tronc Commun", "Premier Bac", "Terminale"]
    if level not in valid_levels:
        return f"Erreur : Niveau invalide. Choisissez parmi {valid_levels}."

    if not starting_point.strip():
        return "Erreur : Le thème du cours doit être une chaîne non vide."

    system_prompt = f"""
Tu es un professeur de mathématiques expérimenté, spécialisé dans l'enseignement au lycée marocain.  
Ton objectif est d'expliquer le thème **'{starting_point}'** de manière claire et progressive pour un élève de niveau **'{level}'**.  

### **Directives :**  
1. **Introduction simple**  
   - Expliquer *pourquoi* ce thème est important en mathématiques ou dans la vie quotidienne.  
   - Donner un exemple concret pour motiver l’élève.  

2. **Prérequis nécessaires**  
   - Lister brièvement les notions que l’élève doit déjà connaître.  
   - Si besoin, rappeler rapidement ces bases.  

3. **Explications étape par étape**  
   - Découper le cours en petites parties (**sous-titres clairs**).  
   - Pour chaque partie :  
     - Définition simple  
     - Exemple détaillé  
     - Exercice d’application (facile → moyen)  
   - Éviter le jargon trop technique.  

4. **À la fin du cours**  
   - Un **résumé** sous forme de liste ou de schéma.  
   - 2-3 exercices pour s’entraîner (avec corrigés si possible).  

### **Style d’écriture :**  
- Phrases courtes et précises.  
- Beaucoup d’exemples numériques.  
- Utiliser des analogies pour faciliter la compréhension.  
- Markdown simple (titres, listes, encadrés).  
"""

    user_prompt = f"""
Je veux un cours sur **{starting_point}** pour un élève de **{level}** au lycée.

Le cours doit être :
✅ **Facile à suivre** (explications pas à pas).
✅ **Avec des exemples concrets** (calculs, situations réelles).
✅ **Avec des exercices** pour vérifier la compréhension.

Format souhaité :
1. **Introduction** (À quoi ça sert ?)
2. **Notions de base** (Rappels si besoin)
3. **Leçons principales** (Définitions + Exemples)  
4. **Résumé & Exercices**  
"""

    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.6,
        max_tokens=4000
    )

    course_content = completion.choices[0].message.content
    return course_content
