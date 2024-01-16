from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

chart_mapping = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05',
                 'F': '06', 'G': '07', 'H': '08', 'I': '09', 'J': '10',
                 'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15',
                 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
                 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26',
                 ' ': '27', ',': '28', '.': '29', '!': '30', '?': '31'}



uppercase_letters = list(string.ascii_uppercase)
def encrypt_pass(input_user):
    result = ""
    for i in input_user:
        numeric = chart_mapping.get(i, "00")
        result += numeric
        result += random.choice(uppercase_letters)
    result += "ENCRYPTED"  
    return result

def decrypt_pass(encrypted_text):
    reverse_mapping = {v: k for k, v in chart_mapping.items()}
    decrypted_result = ""
    
    current_numeric = ""
    
    for i in range(0, len(encrypted_text), 2):  
        pair = encrypted_text[i:i + 2]
        
        current_numeric = ""
        original_char = reverse_mapping.get(pair, '??')
        decrypted_result += original_char.lower()

    return decrypted_result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        user_input = request.form['user_input'].upper()
        modified_input = ""


        if "ENCRYPTED"  in user_input:

            for x in user_input:
                if x.isnumeric():
                    modified_input += x

            result = decrypt_pass(modified_input)
            

        else:
            result=encrypt_pass(user_input)    
             

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
