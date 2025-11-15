import string
from flask import Flask, request, render_template
import random


app = Flask(__name__)


def generate_password(length_pass=12, use_upper=True, use_digits=True, use_symbols=True):
    """Генерация безопасного пароля с указанными параметрами"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()_+" if use_symbols else ""

    if not (lower or upper or digits or symbols):
        return "Невозможно сгенерировать пароль с заданными параметрами."

    all_chars = lower + upper + digits + symbols
    password = random.choices(all_chars, k=length_pass)

    if use_upper:
        password[random.randint(0, length_pass - 1)] = random.choice(upper)
    if use_digits:
        password[random.randint(0, length_pass - 1)] = random.choice(digits)
    if use_symbols:
        password[random.randint(0, length_pass - 1)] = random.choice(symbols)

    random.shuffle(password)
    return "".join(password)


def calculate_password_strength(password, use_upper, use_digits, use_symbols):
    """Расчет сложности пароля (0-100)"""
    score = 0
    length = len(password)
    
    # Оценка по длине (максимум 40 баллов)
    if length >= 16:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        score += 10
    
    # Оценка по типам символов (максимум 60 баллов)
    char_types = 1  # всегда есть строчные буквы
    if use_upper:
        char_types += 1
    if use_digits:
        char_types += 1
    if use_symbols:
        char_types += 1
    
    score += (char_types - 1) * 20  # 0, 20, 40, 60 баллов
    
    return min(score, 100)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate", methods=["GET"])
def generate():
    try:
        length = int(request.args.get("length", 12))
        use_upper = "use_upper" in request.args
        use_digits = "use_digits" in request.args
        use_symbols = "use_symbols" in request.args

        password = generate_password(length, use_upper, use_digits, use_symbols)
        strength = calculate_password_strength(password, use_upper, use_digits, use_symbols)
        return render_template("password.html", password=password, strength=strength)

    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
