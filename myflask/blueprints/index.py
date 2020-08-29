from flask import Blueprint, render_template

index = Blueprint("/", __name__, template_folder="templates")


@index.route('/')
def main():
    return render_template('index.html')