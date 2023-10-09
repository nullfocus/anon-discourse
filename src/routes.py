from flask import render_template, send_from_directory, request
import html
import os
import uuid


def configure_routes(log, app):
    def page(title, content):
        content = str(content)
        content = html.escape(content)
        return f"""
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <pre>{content}</pre>
        </body>
    </html>
    """

    # https://blog.sneawo.com/blog/2017/12/20/no-cache-headers-in-flask/
    @app.after_request
    def set_response_headers(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return page("404 Page Not Found", "Page Not Found"), 404

    @app.errorhandler(Exception)
    def all_exception_handler(error):
        log.debug(error)
        return page("500", error), 500

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    @app.route("/")
    def index():
        channel = request.args.get("c")

        if channel == None or channel.strip() == "":
            log.debug("no channel requested, returning landing page")

            channel = str(uuid.uuid4())

            return render_template("landing.html", channel=channel)
        else:
            log.debug("channel requested: " + channel)

            channel = html.escape(channel)

            return render_template("chat.html", channel=channel)
