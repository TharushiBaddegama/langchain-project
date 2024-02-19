from flask import Flask, render_template, request
from langchain.llms import OpenAI

app = Flask(__name__)

# Function to load OpenAI model and get responses


def get_openai_response(question):
    llm = OpenAI(
        openai_api_key=app.config['OPENAI_API_KEY'],
        model_name="text-davinci-003",
        temperature=0.5
    )
    response = llm(question)
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_question = request.form['input']
        response = get_openai_response(input_question)
        return render_template('index.html', input_question=input_question, response=response)

    return render_template('index.html')


if __name__ == '__main__':
    app.config['OPENAI_API_KEY'] = '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'
    app.run(debug=True)
