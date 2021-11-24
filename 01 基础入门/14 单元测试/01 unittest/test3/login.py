from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "hello world"


@app.route("/login", methods=["POST"])
def login():
    """登录"""
    name = request.form.get("name")
    password = request.form.get("password")

    if not all([name, password]):
        return jsonify(code=65535, message="参数不完整")

    if name == "admin" and password == "123456":
        return jsonify(code=0, message="OK")
    else:
        return jsonify(code=65535, message="用户名或密码错误")


if __name__ == '__main__':
    app.run(debug=True)
