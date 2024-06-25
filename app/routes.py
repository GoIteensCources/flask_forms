from flask import render_template, redirect, url_for, request
from app import app
from app.forms import SubcriptionForm, RegistrationForm


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dosearch/", methods=["GET", "POST"])
def search():
    field_s = request.args.get("s")

    if request.method == "POST":
        field_s = request.form.get("s")

    return f"method: <b>{request.method}</b> Це сторінка пошуку. Виконується пошук по <i>{field_s}</i>"


@app.route("/email/subscription/", methods=["GET", "POST"])
def subscription():
    form = SubcriptionForm()
    # if request.method == "POST":
    if form.validate_on_submit():
        return {"name": form.name.data,
                "email": form.email.data}

    return render_template("subscription.html", form=form)


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == "GET":
        return render_template("registration.html", form=form)

    if form.validate_on_submit():
        return {"VALID": True,
                "name": form.name.data,
                "email": form.email.data,
                "rem": form.remember.data,
                "password": form.password.data,
                "age": form.age.data
                }
    else:
        return f"{form.errors}"

