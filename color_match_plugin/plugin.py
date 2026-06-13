from flask import Blueprint, render_template, current_app
import os

story_bp = Blueprint(
    "story",
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "static"),
    static_url_path="/story_static"
)

@story_bp.route("/")
def main():
    base_exists = "base.html" in current_app.jinja_loader.list_templates()
    return render_template("story.html", base_exists=base_exists)
