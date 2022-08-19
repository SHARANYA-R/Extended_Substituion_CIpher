import json
import random
from flask import Flask, request
from ExtendedSubCipher import ExtendedSubCipher  
from config import config  

app = Flask(__name__)

sub_cipher = ExtendedSubCipher(config["seed"]+'.'+str(config["no_of_tables"]))  
current_index = 0
@app.route('/', methods=['GET'])
def index():
    plain_text = request.args.get('text')
    # print(plain_text)
    if len(plain_text)+sub_cipher.starting_table_index > config["no_of_tables"]:
        sub_cipher.reset_starting_table_index()
        if len(plain_text)+sub_cipher.starting_table_index > config["no_of_tables"]:
            plain_text = plain_text[:config["no_of_tables"]]
            coin_toss = random.random()
            if coin_toss <0.25:
                return json.dumps(
                {
                    'status_code': '400',
                    'status_msg': 'bad_input',
                }
            )
            if coin_toss <0.5:
                return json.dumps(
                {
                    'status_code': '200',
                    'status_msg': 'success',
                    'cipher_text': ''
                }
            )
        return json.dumps(
            {
                'status_code': '200',
                'status_msg': 'success',
                'cipher_text': sub_cipher.encrypt(plain_text)
            }
        )
    else:
        return json.dumps(
            {
                'status_code': '200',
                'status': 'success',
                'cipher_text': sub_cipher.encrypt(plain_text)
            }
        )
app.run()