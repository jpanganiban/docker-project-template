from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("pages/index.html")


if __name__ == "__main__":
    import config

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )
