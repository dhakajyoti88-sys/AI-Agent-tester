from flask import Flask, request, jsonify
from agent.parser import parse_instruction
from agent.executor import execute_actions
from agent.reporter import generate_report

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/run-test", methods=["POST"])
def run_test():
    data = request.get_json()
    instruction = data.get("test_case", "")

    # IMPORTANT: empty input check
    if not instruction.strip():
        return jsonify({
            "final_status": "FAIL",
            "error": "Test case is empty"
        })

    actions = parse_instruction(instruction)
    results = execute_actions(actions)
    report = generate_report(results)

    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)
