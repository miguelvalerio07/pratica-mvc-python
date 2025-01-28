from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

# from model.interface import Interface

# def main():
#     Interface()

# if __name__ == '__main__':
#     main()
