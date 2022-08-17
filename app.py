from flask import Flask, request, Response, render_template
import wakeonlan

app = Flask(__name__)


@app.route('/')
def howtouse():
    return render_template("index.html")


@app.route('/send_magick', methods=['GET'])
def send_magick():
    mac_address = request.args['mac_address']
    ip_address = request.args['ip_address']
    # broadcast_address = request.args.get('broadcast', '192.168.0.255')
    port = request.args.get('port', default=9, type=int)

    wakeonlan.send_magic_packet(
        mac_address,
        ip_address=ip_address,
        port=port
    )
    return Response('magick packet have sent successfully', status=201)


@app.errorhandler(400)
def error_handler(error):
    return 'Some parameter have not received', error.code


if __name__ == '__main__':
    app.run(debug=True)
