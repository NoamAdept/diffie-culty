from flask import Flask, render_template, request, jsonify
import secrets, time

app = Flask(__name__)

def gen_private(p):
    return 2 + secrets.randbelow(p - 3)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["GET"])
def generate():
    p = int(request.args.get("p", 23))
    g = int(request.args.get("g", 5))
    a = gen_private(p)
    A = pow(g, a, p)
    return jsonify({"p": p, "g": g, "A": A, "a": a})  # For demo we send a too (would hide in real CTF)

@app.route("/bruteforce", methods=["POST"])
def bruteforce():
    data = request.get_json()
    p = data["p"]
    g = data["g"]
    A = data["A"]

    start = time.time()
    for candidate in range(2, p - 1):
        if pow(g, candidate, p) == A:
            elapsed = time.time() - start
            return jsonify({"a": candidate, "time": elapsed})
    elapsed = time.time() - start
    return jsonify({"error": "No solution found", "time": elapsed})

if __name__ == "__main__":
    app.run(debug=True)
