from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__)


@app.route('/')
def trx():
    return render_template('flask.html')

@app.route('/data', methods=["GET","POST"])
def data():
    if request.method == "POST":
        address = request.form.get("ev")
        htmlfile = urlopen(f"https://blockchain.info/rawaddr/{address}/?format=json")
        htmltext = htmlfile.read().decode('utf-8')
        load = json.loads(htmltext)
        tnx = load["n_tx"]
        final = [{"Wallet Address":load["address"], "Total Transction":load["n_tx"], "Total Recived":str(load["total_received"]/100000000) + " BTC", "Total Sent":str(load["total_sent"]/100000000)+ " BTC", "Final Balnace":str(load["final_balance"]/100000000)+ " BTC"}]
        output = final
        return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
