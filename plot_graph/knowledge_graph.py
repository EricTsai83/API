# # nobel_viz.py
# from flask import Flask, send_from_directory
# from flask import Markup

# # with open('./Amazon_action_count.html', 'r', encoding='utf8') as f:
# #     fig = f.read()


# # app = Flask(__name__)
# # Serves a file from the directory—in this case, the local directory
# # (.)]—specified in the first argument.
# # @app.route('/')
# # def root():
# #     return send_from_directory('.', 'index.html')




# # @app.route("/index/",methods=["POST", "GET"])
# # def foo():
    
# #     # include_plotlyjs = True builds in the js library
# #     # output_type = 'div' outputs the html code
# #     viz = plot(fig, include_plotlyjs = True, output_type = 'div')

# #     # Markup directly renders the html code
# #     viz = Markup(Amazon_action_count)
# #     return render_template('index.html', viz = viz)





    
# from flask import Flask, render_template
# import pandas as pd
# import json
# import plotly
# import plotly.express as px
# app = Flask(__name__)
# @app.route('/')
# def notdash():
#     df = pd.DataFrame({
#       'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
#       'Bananas'],
#       'Amount': [4, 1, 2, 2, 4, 5],
#       'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
    
#     fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return render_template('notdash.html', graphJSON=graphJSON)


# if __name__ == '__main__':
#     app.run(port=8080)
from flask import Flask, render_template, request, abort
import pandas as pd
import json
import plotly
import plotly.express as px
from tinydb import TinyDB, Query

app = Flask(__name__)


df = pd.DataFrame({
  'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
  'Amount': [4, 1, 2, 2, 4, 5],
  'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
# json_df = df.to_json(orient = 'records')
# db = TinyDB(json_df)


# db = TinyDB(json_df)

@app.route('/')
def notdash():
    for key in ['City']:
        try:
            arg = request.args.get(key)
            temp_df = df.query(f"City=='{arg}'")
            fig = px.bar(temp_df, x='Fruit', y='Amount', color='City', barmode='group')
        except:
            fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('./notdash.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(port=8000, debug="on")  # local: "127.0.0.1"