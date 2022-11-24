from flask import Flask, render_template, request
import smtplib




my_email = "vamsi.krishnathota8055@gmail.com"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password="yapvxkscywaedbsc")
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:New Candidate pls follow up\n\nName {request.form['name']}\n Email:{request.form['email']}\n Contact:"
                    f"{request.form['contact']}\n Message:{request.form['message']}")
        return render_template("index.html")
    else:
        return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)






# @app.route("/post/<int:num>")
# def post(num):
#     url = "https://api.npoint.io/d999c637fb338d977fe0"
#     response = requests.get(url).json()
#     title = ""
#     subtitle = ""
#     body = ""
#     img = ""
#     for blog in response:
#         if blog['id'] == num:
#             title = blog["title"]
#             subtitle = blog["subtitle"]
#             body = blog["body"]
#             img = f"{blog['id']}.avif"
#     return render_template("post.html", title=title, subtitle=subtitle, body=body, img=img)
#
# @app.route("/about/")
# def about():
#     return render_template("about.html")
#
# @app.route("/contact/", methods=['POST', 'GET'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['username']
#         print(name)
#         with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password="yapvxkscywaedbsc")
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=my_email,
#                 msg=f"Subject:New Message\n\nName {request.form['username']}\n Email:{request.form['email']}\n Contact:"
#                     f"{request.form['phone']}\n Message:{request.form['message']}")
#         return render_template("thanks.html")
#     else:
#         return render_template("contact.html")

# @app.route("/form-entry", methods=['POST'])
# def feedback():
#     return render_template("thanks.html")