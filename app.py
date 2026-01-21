from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# File path for persistent storage
INVENTORY_FILE = 'inventory.json'

def load_inventory():
    """Load inventory from file, return empty list if file doesn't exist"""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_inventory(inventory):
    """Save inventory to file"""
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=2)

@app.route('/', methods=['GET'])
def home():
    """Home page with usage instructions"""
    return jsonify({
        'message': 'Inventory API',
        'endpoints': {
            'GET /inventory': 'List all items',
            'POST /inventory': 'Add new item (JSON body: {"item": "item name"})',
            'DELETE /inventory': 'Clear all items'
        }
    })

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Get all items in inventory"""
    inventory = load_inventory()
    return jsonify({
        'count': len(inventory),
        'items': inventory
    })

@app.route('/inventory', methods=['POST'])
def add_item():
    """Add a new item to inventory"""
    data = request.get_json()
    
    if not data or 'item' not in data:
        return jsonify({'error': 'Please provide an item name in JSON format: {"item": "item name"}'}), 400
    
    item_name = data['item'].strip()
    
    if not item_name:
        return jsonify({'error': 'Item name cannot be empty'}), 400
    
    inventory = load_inventory()
    inventory.append({
        'item': item_name,
        'timestamp': str(os.path.getctime(__file__)) if os.path.exists(__file__) else 'unknown'
    })
    
    save_inventory(inventory)
    
    return jsonify({
        'message': 'Item added successfully',
        'item': item_name,
        'total_items': len(inventory)
    }), 201

@app.route('/inventory', methods=['DELETE'])
def clear_inventory():
    """Clear all items from inventory"""
    save_inventory([])
    return jsonify({
        'message': 'Inventory cleared successfully'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)