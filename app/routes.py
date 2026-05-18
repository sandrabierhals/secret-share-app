from flask import Blueprint, render_template, request, url_for
from services import create_secret, get_secret

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        secret_text = request.form["secret"]
        expires_in = int(request.form["expires_in"])
        one_time = "one_time" in request.form

        secret_id = create_secret(secret_text, expires_in, one_time)

        secret_link = url_for(
            "main.view_secret",
            secret_id=secret_id,
            _external=True
        )

        return render_template(
            "secret-created.html",
            secret_link=secret_link
        )

    return render_template("index.html")


@main.route("/secret/<secret_id>")
def view_secret(secret_id):
    secret_text, error = get_secret(secret_id)

    if error == "not_found":
        return render_template("secret-not-found.html"), 404

    if error == "expired":
        return render_template("secret-expired.html"), 410

    if error == "already_read":
        return render_template("secret-already-read.html"), 410

    return render_template(
        "view-secret.html",
        secret=secret_text
    )
    

@main.route("/health")
def health():
    return {"status": "ok"}, 200