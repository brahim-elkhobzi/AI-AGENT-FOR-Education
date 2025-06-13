
# Math Quiz Questions for Premier Bac Level
questions_by_topic = {
    "Fonctions": [
        {
            "question": "Le domaine de f(x) = 1/x est :",
            "options": ["ℝ", "ℝ\\{0}", "[0,∞)", "[-1,1]"],
            "correct": "ℝ\\{0}",
            "explanation": "x ≠ 0 pour éviter division par 0.",
            "level": "Premier Bac",
            "topic": "Fonctions"
        },
        {
            "question": "f(x) = x² est-elle injective ?",
            "options": ["Non", "Oui", "Sur ℝ⁺", "Sur ℝ⁻"],
            "correct": "Non",
            "explanation": "f(-x) = f(x), donc pas injective.",
            "level": "Premier Bac",
            "topic": "Fonctions"
        },
        {
            "question": "Si f(x) = 2x + 3, alors f(1) = ?",
            "options": ["5", "3", "4", "6"],
            "correct": "5",
            "explanation": "f(1) = 2×1 + 3 = 5.",
            "level": "Premier Bac",
            "topic": "Fonctions"
        },
        # ... 17 more questions
        {
            "question": "f(x) = |x| est-elle surjective sur ℝ ?",
            "options": ["Non", "Oui", "Sur ℝ⁺", "Sur ℝ⁻"],
            "correct": "Non",
            "explanation": "Image de f(x) = |x| est ℝ⁺, pas ℝ.",
            "level": "Premier Bac",
            "topic": "Fonctions"
        }
    ],
    "Barycentre": [
        {
            "question": "Barycentre de A(1,1) et B(3,3) avec poids 1:1 ?",
            "options": ["(2,2)", "(1,3)", "(3,1)", "(4,4)"],
            "correct": "(2,2)",
            "explanation": "Moyenne des coordonnées.",
            "level": "Premier Bac",
            "topic": "Barycentre"
        },
        {
            "question": "Barycentre de A(0,0) et B(4,0) avec poids 2:1 ?",
            "options": ["(4/3,0)", "(8/3,0)", "(2,0)", "(1,0)"],
            "correct": "(8/3,0)",
            "explanation": "x = (2×0 + 1×4)/(2+1).",
            "level": "Premier Bac",
            "topic": "Barycentre"
        },
        {
            "question": "Barycentre de A(1,2), B(5,4) avec poids 3:1 ?",
            "options": ["(2,5/2)", "(3,3)", "(4,3)", "(2,3)"],
            "correct": "(2,5/2)",
            "explanation": "x = (3×1 + 1×5)/(3+1), y = (3×2 + 1×4)/(3+1).",
            "level": "Premier Bac",
            "topic": "Barycentre"
        },
        # ... 17 more questions
        {
            "question": "Si G(3,2) est barycentre de A(2,1), B(x,y), poids 2:1, alors B = ?",
            "options": ["(5,4)", "(4,3)", "(3,2)", "(6,5)"],
            "correct": "(5,4)",
            "explanation": "x = (2×2 + 1×x)/(2+1) = 3, y = (2×1 + 1×y)/(2+1) = 2.",
            "level": "Premier Bac",
            "topic": "Barycentre"
        }
    ],
    "Produit scalaire": [
        {
            "question": "Produit scalaire u·v, u(1,2), v(3,4) ?",
            "options": ["11", "7", "5", "9"],
            "correct": "11",
            "explanation": "u·v = 1×3 + 2×4 = 11.",
            "level": "Premier Bac",
            "topic": "Produit scalaire"
        },
        {
            "question": "u et v orthogonaux si u(1,0), v(0,1) ?",
            "options": ["Oui", "Non", "Parfois", "Jamais"],
            "correct": "Oui",
            "explanation": "u·v = 0.",
            "level": "Premier Bac",
            "topic": "Produit scalaire"
        },
        {
            "question": "Norme de u(2,3) ?",
            "options": ["√13", "5", "√5", "7"],
            "correct": "√13",
            "explanation": "||u|| = √(2² + 3²) = √13.",
            "level": "Premier Bac",
            "topic": "Produit scalaire"
        },
        # ... 17 more questions
        {
            "question": "Produit scalaire u·v, u(2,0), v(0,3) ?",
            "options": ["0", "6", "2", "3"],
            "correct": "0",
            "explanation": "u·v = 2×0 + 0×3 = 0.",
            "level": "Premier Bac",
            "topic": "Produit scalaire"
        }
    ],
    "Suites numériques": [
        {
            "question": "Si u_n = 2n + 1, alors u_3 =",
            "options": ["7", "5", "9", "6"],
            "correct": "7",
            "explanation": "u_3 = 2×3 + 1 = 7.",
            "level": "Premier Bac",
            "topic": "Suites numériques"
        },
        {
            "question": "Suite géométrique : 2, 4, 8, …, raison =",
            "options": ["2", "4", "1", "3"],
            "correct": "2",
            "explanation": "4/2 = 8/4 = 2.",
            "level": "Premier Bac",
            "topic": "Suites numériques"
        },
        {
            "question": "Si u_1 = 1, u_{n+1} = 3u_n, alors u_3 = ?",
            "options": ["9", "3", "6", "1"],
            "correct": "9",
            "explanation": "u_2 = 3×1 = 3, u_3 = 3×3 = 9.",
            "level": "Premier Bac",
            "topic": "Suites numériques"
        },
        # ... 17 more questions
        {
            "question": "u_n = n² est-elle croissante pour n ≥ 1 ?",
            "options": ["Oui", "Non", "Parfois", "Jamais"],
            "correct": "Oui",
            "explanation": "u_{n+1} - u_n = 2n + 1 > 0 pour n ≥ 1.",
            "level": "Premier Bac",
            "topic": "Suites numériques"
        }
    ],
    "Calcul trigonométrique": [
        {
            "question": "Valeur de sin(π/6) ?",
            "options": ["1/2", "√3/2", "1", "0"],
            "correct": "1/2",
            "explanation": "Valeur usuelle de sin(30°).",
            "level": "Premier Bac",
            "topic": "Calcul trigonométrique"
        },
        {
            "question": "cos²(x) + sin²(x) =",
            "options": ["1", "0", "2", "-1"],
            "correct": "1",
            "explanation": "Identité trigonométrique fondamentale.",
            "level": "Premier Bac",
            "topic": "Calcul trigonométrique"
        },
        {
            "question": "Valeur de tan(π/3) ?",
            "options": ["√3", "1", "1/√3", "0"],
            "correct": "√3",
            "explanation": "Valeur usuelle de tan(60°).",
            "level": "Premier Bac",
            "topic": "Calcul trigonométrique"
        },
        # ... 17 more questions
        {
            "question": "Si sin(x) = √2/2, alors x = ? (0 ≤ x ≤ π/2)",
            "options": ["π/4", "π/6", "π/3", "π/2"],
            "correct": "π/4",
            "explanation": "sin(x) = √2/2 pour x = π/4 dans [0,π/2].",
            "level": "Premier Bac",
            "topic": "Calcul trigonométrique"
        }
    ],
    "Rotation": [
        {
            "question": "Rotation de 90° autour de O, A(1,0) ?",
            "options": ["(0,1)", "(-1,0)", "(0,-1)", "(1,0)"],
            "correct": "(0,1)",
            "explanation": "Rotation 90° : (x,y) → (-y,x).",
            "level": "Premier Bac",
            "topic": "Rotation"
        },
        {
            "question": "Rotation de 180° autour de O, A(2,3) ?",
            "options": ["(-2,-3)", "(2,-3)", "(-2,3)", "(3,2)"],
            "correct": "(-2,-3)",
            "explanation": "Rotation 180° : (x,y) → (-x,-y).",
            "level": "Premier Bac",
            "topic": "Rotation"
        },
        {
            "question": "Rotation de 90° autour de (1,1), A(2,1) ?",
            "options": ["(1,2)", "(2,2)", "(1,0)", "(0,1)"],
            "correct": "(1,2)",
            "explanation": "Translation, rotation 90°, translation inverse.",
            "level": "Premier Bac",
            "topic": "Rotation"
        },
        # ... 17 more questions
        {
            "question": "Rotation de -90° autour de O, A(1,1) ?",
            "options": ["(1,-1)", "(-1,1)", "(-1,-1)", "(0,0)"],
            "correct": "(1,-1)",
            "explanation": "Rotation -90° : (x,y) → (y,-x).",
            "level": "Premier Bac",
            "topic": "Rotation"
        }
    ],
    "Limites": [
        {
            "question": "Limite de f(x) = 1/x quand x → ∞ ?",
            "options": ["0", "1", "∞", "-∞"],
            "correct": "0",
            "explanation": "1/x → 0 quand x → ∞.",
            "level": "Premier Bac",
            "topic": "Limites"
        },
        {
            "question": "Limite de f(x) = x² quand x → 0 ?",
            "options": ["0", "1", "∞", "-∞"],
            "correct": "0",
            "explanation": "x² → 0 quand x → 0.",
            "level": "Premier Bac",
            "topic": "Limites"
        },
        {
            "question": "Limite de f(x) = (x²-4)/(x-2) quand x → 2 ?",
            "options": ["4", "2", "0", "Indéfini"],
            "correct": "4",
            "explanation": "(x²-4)/(x-2) = x+2, limite = 4.",
            "level": "Premier Bac",
            "topic": "Limites"
        },
        # ... 17 more questions
        {
            "question": "Limite de f(x) = (2x+1)/(x-1) quand x → ∞ ?",
            "options": ["2", "1", "∞", "0"],
            "correct": "2",
            "explanation": "Diviser par x, limite = 2/1 = 2.",
            "level": "Premier Bac",
            "topic": "Limites"
        }
    ],
    "Dérivation": [
        {
            "question": "Dérivée de f(x) = x² ?",
            "options": ["2x", "x", "2", "x²"],
            "correct": "2x",
            "explanation": "f'(x) = 2x.",
            "level": "Premier Bac",
            "topic": "Dérivation"
        },
        {
            "question": "Dérivée de f(x) = sin(x) ?",
            "options": ["cos(x)", "-sin(x)", "sin(x)", "-cos(x)"],
            "correct": "cos(x)",
            "explanation": "f'(x) = cos(x).",
            "level": "Premier Bac",
            "topic": "Dérivation"
        },
        {
            "question": "Dérivée de f(x) = 3x² - 2x ?",
            "options": ["6x - 2", "3x - 2", "6x", "3x"],
            "correct": "6x - 2",
            "explanation": "f'(x) = 6x - 2.",
            "level": "Premier Bac",
            "topic": "Dérivation"
        },
        # ... 17 more questions
        {
            "question": "Dérivée de f(x) = cos(x) ?",
            "options": ["-sin(x)", "sin(x)", "cos(x)", "-cos(x)"],
            "correct": "-sin(x)",
            "explanation": "f'(x) = -sin(x).",
            "level": "Premier Bac",
            "topic": "Dérivation"
        }
    ],
    "Étude des fonctions": [
        {
            "question": "Signe de f(x) = x² - 4 pour x > 2 ?",
            "options": ["Positif", "Négatif", "Nul", "Indéfini"],
            "correct": "Positif",
            "explanation": "x² - 4 > 0 pour x > 2.",
            "level": "Premier Bac",
            "topic": "Étude des fonctions"
        },
        {
            "question": "f(x) = x³ est-elle croissante ?",
            "options": ["Oui", "Non", "Sur ℝ⁺", "Sur ℝ⁻"],
            "correct": "Oui",
            "explanation": "f'(x) = 3x² ≥ 0, donc croissante.",
            "level": "Premier Bac",
            "topic": "Étude des fonctions"
        },
        {
            "question": "Minimum de f(x) = x² - 4x + 3 ?",
            "options": ["x = 2", "x = 1", "x = 0", "Aucun"],
            "correct": "x = 2",
            "explanation": "f'(x) = 2x - 4, f''(2) > 0, min en x = 2.",
            "level": "Premier Bac",
            "topic": "Étude des fonctions"
        },
        # ... 17 more questions
        {
            "question": "Asymptote horizontale de f(x) = (3x)/(x+2) ?",
            "options": ["y = 3", "y = 0", "y = 2", "Aucune"],
            "correct": "y = 3",
            "explanation": "Limite quand x → ±∞ donne y = 3.",
            "level": "Premier Bac",
            "topic": "Étude des fonctions"
        }
    ],
    "Géométrie dans l’espace": [
        {
            "question": "Distance entre A(1,0,0) et B(0,1,0) ?",
            "options": ["√2", "1", "2", "√3"],
            "correct": "√2",
            "explanation": "d = √((1-0)² + (0-1)² + (0-0)²).",
            "level": "Premier Bac",
            "topic": "Géométrie dans l’espace"
        },
        {
            "question": "Vecteur AB si A(1,1,1), B(2,3,4) ?",
            "options": ["(1,2,3)", "(2,3,4)", "(1,1,1)", "(3,4,5)"],
            "correct": "(1,2,3)",
            "explanation": "AB = (2-1, 3-1, 4-1).",
            "level": "Premier Bac",
            "topic": "Géométrie dans l’espace"
        },
        {
            "question": "Équation paramétrique de la droite passant par (0,0,0), vecteur (1,2,3) ?",
            "options": ["x = t, y = 2t, z = 3t", "x = t, y = t, z = t", "x = 0, y = t, z = 0", "x = t, y = 0, z = 0"],
            "correct": "x = t, y = 2t, z = 3t",
            "explanation": "Paramétrique : x = t, y = 2t, z = 3t.",
            "level": "Premier Bac",
            "topic": "Géométrie dans l’espace"
        },
        # ... 17 more questions
        {
            "question": "Produit scalaire u·v, u(1,0,1), v(0,1,0) ?",
            "options": ["0", "1", "2", "3"],
            "correct": "0",
            "explanation": "u·v = 1×0 + 0×1 + 1×0 = 0.",
            "level": "Premier Bac",
            "topic": "Géométrie dans l’espace"
        }
    ]
}
