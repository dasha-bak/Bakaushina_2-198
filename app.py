import json

from flask import request

from . import create_app, database
from .models import Tools

app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    tools = database.get_all(Tools)
    all_tools = []
    for tool in tools:
        new_tool = {
            "id": tool.id,
            "name": tool.name,
            "country": tool.country,
            "price": tool.price
        }

        all_tools.append(new_tool)

    if (len(all_tools) == 0):
        return json.dumps("No tools found"), 200
    else:
        return json.dumps(all_tools), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    country = data['country']
    price = data['price']

    database.add_instance(Tools, name=name, country=country, price=price)
    return json.dumps("Added"), 200


@app.route('/remove/<tool_id>', methods=['DELETE'])
def remove(tool_id): 
    database.delete_instance(Tools, id=tool_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<tool_id>', methods=['PATCH'])
def edit(tool_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Tools, id=tool_id, price=new_price)
    return json.dumps("Edited"), 200