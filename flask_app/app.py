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
        return f"""
         <h1>Ваш сгенерированный пароль:</h1>
        <p style="font-size: 24px; font-weight: bold;">{password}</p>
        <a href="/">Сгенерировать новый пароль</a>
        """

    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
