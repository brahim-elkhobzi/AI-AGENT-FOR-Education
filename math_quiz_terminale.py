
# Math Quiz Questions for terminale Level
questions_by_topic = {
    "Limites et continuité": [
        {
            "question": "Quelle est la limite de f(x) = (x² - 4)/(x - 2) quand x tend vers 2 ?",
            "options": ["4", "2", "0", "Indéfini"],
            "correct": "4",
            "explanation": "Simplifier : (x² - 4)/(x - 2) = x + 2 pour x ≠ 2, donc lim = 4.",
            "level": "Terminale",
            "topic": "Limites et continuité"
        },
        {
            "question": "La fonction f(x) = 1/x est-elle continue en x = 0 ?",
            "options": ["Non", "Oui", "À droite", "À gauche"],
            "correct": "Non",
            "explanation": "f(x) n’est pas définie en x = 0, donc pas continue.",
            "level": "Terminale",
            "topic": "Limites et continuité"
        },
        {
            "question": "Quelle est la limite de sin(2x)/x quand x tend vers 0 ?",
            "options": ["2", "1", "0", "Indéfini"],
            "correct": "2",
            "explanation": "sin(2x)/x = 2(sin(2x)/(2x)), lim sin(2x)/(2x) = 1, donc lim = 2.",
            "level": "Terminale",
            "topic": "Limites et continuité"
        },
       
    ],
    "Dérivation et étude des fonctions": [
        {
            "question": "Quelle est la dérivée de f(x) = x⁴ + 3x² ?",
            "options": ["4x³ + 6x", "4x³ + 3x", "x³ + 6x", "4x + 6"],
            "correct": "4x³ + 6x",
            "explanation": "f'(x) = 4x³ + 6x par les règles de dérivation.",
            "level": "Terminale",
            "topic": "Dérivation et étude des fonctions"
        },
        {
            "question": "Quel est le point critique de f(x) = x³ - 6x² + 9x ?",
            "options": ["x = 1, 3", "x = 0", "x = 2", "Aucun"],
            "correct": "x = 1, 3",
            "explanation": "f'(x) = 3x² - 12x + 9 = 3(x-1)(x-3), donc x = 1, 3.",
            "level": "Terminale",
            "topic": "Dérivation et étude des fonctions"
        },
        {
            "question": "La fonction f(x) = e^(-x²) a-t-elle un maximum ?",
            "options": ["Oui", "Non", "À l’infini", "Indéfini"],
            "correct": "Oui",
            "explanation": "f'(x) = -2xe^(-x²), f'(0) = 0, f''(0) < 0, donc maximum en x = 0.",
            "level": "Terminale",
            "topic": "Dérivation et étude des fonctions"
        },
        
    ],
    "Suites numériques": [
        {
            "question": "Si u_n = 2/(n + 1), quelle est la limite quand n tend vers l’infini ?",
            "options": ["0", "1", "2", "Indéfini"],
            "correct": "0",
            "explanation": "2/(n + 1) tend vers 0 quand n → ∞.",
            "level": "Terminale",
            "topic": "Suites numériques"
        },
        {
            "question": "La suite u_n = (-1)^n/n converge-t-elle ?",
            "options": ["Oui", "Non", "Vers 1", "Vers -1"],
            "correct": "Oui",
            "explanation": "lim (-1)^n/n = 0, donc converge vers 0.",
            "level": "Terminale",
            "topic": "Suites numériques"
        },
        {
            "question": "Si u_1 = 3 et u_{n+1} = u_n + 2, quelle est l’expression de u_n ?",
            "options": ["3 + 2n", "3 + 2(n-1)", "2n", "3n"],
            "correct": "3 + 2(n-1)",
            "explanation": "Suite arithmétique : u_n = u_1 + (n-1)d = 3 + 2(n-1).",
            "level": "Terminale",
            "topic": "Suites numériques"
        },
       
     ],
    "Fonctions primitives": [
        {
            "question": "Quelle est une primitive de f(x) = 3x² ?",
            "options": ["x³ + C", "3x³ + C", "x² + C", "3x + C"],
            "correct": "x³ + C",
            "explanation": "∫3x² dx = x³ + C.",
            "level": "Terminale",
            "topic": "Fonctions primitives"
        },
        {
            "question": "Quelle est une primitive de f(x) = sin(2x) ?",
            "options": ["-(1/2)cos(2x) + C", "cos(2x) + C", "-(1/2)sin(2x) + C", "sin(2x) + C"],
            "correct": "-(1/2)cos(2x) + C",
            "explanation": "∫sin(2x) dx = -(1/2)cos(2x) + C par substitution.",
            "level": "Terminale",
            "topic": "Fonctions primitives"
        },
        {
            "question": "Quelle est une primitive de f(x) = e^(3x) ?",
            "options": ["(1/3)e^(3x) + C", "e^(3x) + C", "3e^(3x) + C", "e^x + C"],
            "correct": "(1/3)e^(3x) + C",
            "explanation": "∫e^(3x) dx = (1/3)e^(3x) + C par substitution.",
            "level": "Terminale",
            "topic": "Fonctions primitives"
        },
       
    ],
    "Fonctions logarithmiques": [
        {
            "question": "Quel est le domaine de f(x) = ln(2x - 1) ?",
            "options": ["]1/2,∞[", "[1/2,∞[", "]0,∞[", "ℝ"],
            "correct": "]1/2,∞[",
            "explanation": "ln(2x - 1) défini pour 2x - 1 > 0, soit x > 1/2.",
            "level": "Terminale",
            "topic": "Fonctions logarithmiques"
        },
        {
            "question": "Quelle est la dérivée de f(x) = ln(x + 3) ?",
            "options": ["1/(x + 3)", "1/x", "x/(x + 3)", "1/(x + 3)²"],
            "correct": "1/(x + 3)",
            "explanation": "f'(x) = 1/(x + 3) par dérivation de ln(u).",
            "level": "Terminale",
            "topic": "Fonctions logarithmiques"
        },
        {
            "question": "Quelle est la limite de ln(x)/x quand x tend vers ∞ ?",
            "options": ["0", "1", "∞", "-∞"],
            "correct": "0",
            "explanation": "ln(x) croît plus lentement que x, donc lim = 0.",
            "level": "Terminale",
            "topic": "Fonctions logarithmiques"
        },
     
    ],
    "Nombres complexes (Partie 1)": [
        {
            "question": "Quel est le module de z = 1 - i ?",
            "options": ["√2", "1", "2", "√3"],
            "correct": "√2",
            "explanation": "|z| = √(1² + (-1)²) = √2.",
            "level": "Terminale",
            "topic": "Nombres complexes (Partie 1)"
        },
        {
            "question": "Quel est le conjugué de z = 3 + 2i ?",
            "options": ["3 - 2i", "-3 + 2i", "3 + 2i", "-3 - 2i"],
            "correct": "3 - 2i",
            "explanation": "Conjugué : a + bi → a - bi.",
            "level": "Terminale",
            "topic": "Nombres complexes (Partie 1)"
        },
        {
            "question": "Quelle est la partie imaginaire de z = 4 - 5i ?",
            "options": ["-5", "4", "5", "0"],
            "correct": "-5",
            "explanation": "z = 4 - 5i, partie imaginaire = -5.",
            "level": "Terminale",
            "topic": "Nombres complexes (Partie 1)"
        },
       
    ],
    "Fonctions exponentielles": [
        {
            "question": "Quelle est la dérivée de f(x) = e^(-x) ?",
            "options": ["-e^(-x)", "e^(-x)", "e^x", "-e^x"],
            "correct": "-e^(-x)",
            "explanation": "f'(x) = e^(-x) × (-1) = -e^(-x).",
            "level": "Terminale",
            "topic": "Fonctions exponentielles"
        },
        {
            "question": "Quelle est la limite de e^(2x) quand x tend vers -∞ ?",
            "options": ["0", "1", "∞", "-∞"],
            "correct": "0",
            "explanation": "e^(2x) tend vers 0 quand x → -∞.",
            "level": "Terminale",
            "topic": "Fonctions exponentielles"
        },
        {
            "question": "La fonction f(x) = 2e^x est-elle croissante ?",
            "options": ["Oui", "Non", "Parfois", "Jamais"],
            "correct": "Oui",
            "explanation": "f'(x) = 2e^x > 0, donc strictement croissante.",
            "level": "Terminale",
            "topic": "Fonctions exponentielles"
        },
       
    ],
    "Nombres complexes (Partie 2)": [
        {
            "question": "Quelles sont les solutions de z² - 2z + 2 = 0 ?",
            "options": ["z = 1 ± i", "z = 1 ± 2i", "z = ±1", "Aucune"],
            "correct": "z = 1 ± i",
            "explanation": "Δ = 4 - 8 = -4, z = (2 ± √(-4))/2 = 1 ± i.",
            "level": "Terminale",
            "topic": "Nombres complexes (Partie 2)"
        },
        {
            "question": "Quelle est la valeur de i³ ?",
            "options": ["-i", "i", "1", "-1"],
            "correct": "-i",
            "explanation": "i³ = i² × i = (-1) × i = -i.",
            "level": "Terminale",
            "topic": "Nombres complexes (Partie 2)"
        },
        {
            "question": "Quel est l’argument de z = -√3 + i ?",
            "options": ["5π/6", "π/6", "-π/6", "-5π/6"],
            "correct": "5π/6",
            "explanation": "z dans le 2e quadrant, arg = π - π/6 = 5π/6.",
            "level": "Terminale",
            "topic": "Nombres complexes (Partie 2)"
        },
       
    ],
    "Calcul intégral": [
        {
            "question": "Quelle est la valeur de ∫(0 à 2) 2x dx ?",
            "options": ["4", "2", "8", "0"],
            "correct": "4",
            "explanation": "Primitive : x², [x²]_0^2 = 4 - 0 = 4.",
            "level": "Terminale",
            "topic": "Calcul intégral"
        },
        {
            "question": "Quelle est l’intégrale de cos(x) dx ?",
            "options": ["sin(x) + C", "-sin(x) + C", "cos(x) + C", "-cos(x) + C"],
            "correct": "sin(x) + C",
            "explanation": "∫cos(x) dx = sin(x) + C.",
            "level": "Terminale",
            "topic": "Calcul intégral"
        },
        {
            "question": "Quelle est la valeur de ∫(1 à 2) 1/x² dx ?",
            "options": ["1/2", "1", "-1/2", "-1"],
            "correct": "1/2",
            "explanation": "Primitive : -1/x, [-1/x]_1^2 = -1/2 - (-1) = 1/2.",
            "level": "Terminale",
            "topic": "Calcul intégral"
        },
     
    ],
    "Équations différentielles": [
        {
            "question": "Quelle est la solution générale de y' = y ?",
            "options": ["y = Ce^x", "y = Ce^(-x)", "y = Cx", "y = C"],
            "correct": "y = Ce^x",
            "explanation": "Équation y' = ky, solution y = Ce^(kx), ici k = 1.",
            "level": "Terminale",
            "topic": "Équations différentielles"
        },
        {
            "question": "Quelle est la solution particulière de y' - 2y = 0 avec y(0) = 2 ?",
            "options": ["y = 2e^(2x)", "y = 2e^(-2x)", "y = e^(2x)", "y = 2"],
            "correct": "y = 2e^(2x)",
            "explanation": "Solution générale : y = Ce^(2x), y(0) = C = 2.",
            "level": "Terminale",
            "topic": "Équations différentielles"
        },
        {
            "question": "Quel est le type de l’équation y'' - 4y = 0 ?",
            "options": ["Linéaire homogène", "Linéaire non homogène", "Non linéaire", "Séparable"],
            "correct": "Linéaire homogène",
            "explanation": "Équation linéaire avec second membre nul.",
            "level": "Terminale",
            "topic": "Équations différentielles"
        },
       
    ],

    "Géométrie dans l’espace": [
        {
            "question": "Quel est le produit scalaire de u(1,1,0) et v(0,1,1) ?",
            "options": ["1", "2", "0", "3"],
            "correct": "1",
            "explanation": "u·v = 1×0 + 1×1 + 0×1 = 1.",
            "level": "Terminale",
            "topic": "Géométrie dans l’espace"
        },
        {
            "question": "Quel est le produit vectoriel u×v si u(1,0,0) et v(0,0,1) ?",
            "options": ["(0,1,0)", "(0,-1,0)", "(1,0,0)", "(0,0,1)"],
            "correct": "(0,1,0)",
            "explanation": "u×v = (0,0,Obligatory field: The input field is required. (0,1) = (0,1,0) par calcul du déterminant.",
            "correct": "(0,1,0)",
            "explanation": "u×v = (0,1,0) par calcul du déterminant.",
            "level": "Terminale",
            "topic": "Géométrie dans l’espace"
        },
        {
            "question": "Quelle est la distance entre A(1,0,1) et B(0,1,0) ?",
            "options": ["√3", "√2", "2", "1"],
            "correct": "√3",
            "explanation": "d = √((1-0)² + (0-1)² + (1-0)²) = √3.",
            "level": "Terminale",
            "topic": "Géométrie dans l’espace"
        },
       
    ],

    "Dénombrement et probabilités": [
        {
            "question": "Quel est le nombre de combinaisons de 5 objets pris 2 à 2 ?",
            "options": ["10", "5", "20", "25"],
            "correct": "10",
            "explanation": "C(5,2) = 5!/(2!3!) = 10.",
            "level": "Terminale",
            "topic": "Dénombrement et probabilités"
        },
        {
            "question": "Quelle est la probabilité de tirer une carte rouge dans un jeu de 52 cartes ?",
            "options": ["1/2", "1/4", "1/13", "1/26"],
            "correct": "1/2",
            "explanation": "P = 26/52 = 1/2 (26 cartes rouges sur 52).",
            "level": "Terminale",
            "topic": "Dénombrement et probabilités"
        },
        {
            "question": "Quel est le nombre de permutations de 3 objets ?",
            "options": ["6", "3", "9", "12"],
            "correct": "6",
            "explanation": "P(3) = 3! = 6.",
            "level": "Terminale",
            "topic": "Dénombrement et probabilités"
        },
       
    ], 
}