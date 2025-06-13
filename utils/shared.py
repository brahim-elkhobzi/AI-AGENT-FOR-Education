from utils.math_solver import solve_math_problem, get_similar_problems
from utils.domain_prompts import get_domain_prompt
from langchain.memory import ConversationBufferMemory

# Initialize memory
memory = ConversationBufferMemory()

def solve_problem_interface(problem_text, domain):
    """Solve a math problem based on the domain."""
    solution = solve_math_problem(problem_text, domain)
    memory.save_context({'input': problem_text}, {'output': solution})
    return solution

def generate_similar_problems_interface(problem_text, domain):
    """Generate similar math problems based on the domain."""
    similar_problems = get_similar_problems(problem_text, domain)
    memory.save_context({'input': problem_text}, {'output': similar_problems})
    return similar_problems

def recommend_topics_interface(scores, level=None):
    """Recommend topics based on scores and user level."""
    return get_domain_prompt(scores, level)
