from flask import Flask, request, jsonify
from config import config
import logging
import yagmail


mail = Flask(__name__)


logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level']
)

username = config['user']
password = config['password']
yag = yagmail.SMTP(username)

yagmail.register(username, password)


def send_mail(request):
    reciverData = request.args.get('reciver')
    subjectData = request.args.get('subject')
    contentsData = request.args.get('contents')
    logging.info(f"{reciverData} {subjectData} {contentsData}")
    return yag.send(to=reciverData,
                    subject=subjectData,
                    contents=contentsData)


@mail.route('/', methods=['GET'])
def get_name():
    return jsonify({"developer": "Enes Turan"},
                   {"version": "1.0.0"}), 200


@mail.route('/send', methods=['POST'])
def sender():
    if request.method == 'POST':
        logging.info(f"{request.data}")

    try:
        send_mail(request)
        return jsonify({"message": "Mail sent successfully"},
                       {"status": "success"}), 200

    except Exception as e:
        logging.error(f"{e}")
        return jsonify({"message": "Mail not sent"}), 500


if __name__ == "__main__":
    mail.run(debug=True, host="localhost", port=5000)
