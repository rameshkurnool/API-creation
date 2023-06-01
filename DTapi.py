from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Sample data
events = [
    {
        'id': '1',
        'name': 'Event 1',
        'tagline': 'Tagline 1',
        'schedule': '2023-06-01',
        'description': 'Description 1',
        'moderator': 'Moderator 1',
        'category': 'Category 1',
        'sub_category': 'Subcategory 1',
        'rigor_rank': 1,
        'attendees': []
    },
    {
        'id': '2',
        'name': 'Event 2',
        'tagline': 'Tagline 2',
        'schedule': '2023-06-02',
        'description': 'Description 2',
        'moderator': 'Moderator 2',
        'category': 'Category 2',
        'sub_category': 'Subcategory 2',
        'rigor_rank': 2,
        'attendees': []
    }
]

# GET /api/v3/app/events?id=:event_id
@app.route('/api/v3/app/events', methods=['GET'])
def get_event_by_id():
    event_id = request.args.get('id')
    event = next((event for event in events if event['id'] == event_id), None)
    if event:
        return jsonify(event)
    else:
        return jsonify({'error': 'Event not found'}), 404

# GET /api/v3/app/events/latest?type=:event_type&limit=:limit&page=:page
@app.route('/api/v3/app/events/latest', methods=['GET'])
def get_latest_events():
    event_type = request.args.get('type')
    limit = int(request.args.get('limit', 10))
    page = int(request.args.get('page', 1))
    # Filter events based on event type
    filtered_events = events if not event_type else [event for event in events if event['category'] == event_type]
    
    # Calculate the start and end indices for pagination
    start_index = (page - 1) * limit
    end_index = page * limit
    
    # Fetch the latest events within the specified range
    latest_events = filtered_events[start_index:end_index]
    
    return jsonify(latest_events)
# POST /api/v3/app/events
@app.route('/api/v3/app/events', methods=['POST'])
def create_event():
    event_data = request.json
    event = {
        'id': generate_unique_id(),
        'name': event_data['name'],
        'tagline': event_data['tagline'],
        'schedule': event_data['schedule'],
        'description': event_data['description'],
        'moderator': event_data['moderator'],
        'category': event_data['category'],
        'sub_category': event_data['sub_category'],
        'rigor_rank': event_data['rigor_rank'],
        'attendees': []
    }
    events.append(event)
    return jsonify({'id': event['id']}), 201

# PUT /api/v3/app/events/:id
@app.route('/api/v3/app/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event:
        event_data = request.json
        event.update(event_data)
        return jsonify({'message': 'Event updated'})
    else:
        return jsonify({'error': 'Event not found'}), 404

# DELETE /api/v3/app/events/:id
@app.route('/api/v3/app/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event:
        events.remove(event)
        return jsonify({'message': 'Event deleted'})
    else:
        return jsonify({'error': 'Event not found'}), 404

# Helper function to generate a unique id
def generate_unique_id():
    return str(uuid.uuid4())

# Run the Flask app
if __name__ == '__main__':
    app.run()




