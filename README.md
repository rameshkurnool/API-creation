# API-creation

# Event Management API

This is a Flask-based API for managing events. It provides endpoints to create, retrieve, update, and delete events. The API supports features such as searching events by ID, retrieving the latest events, and pagination.

## API Endpoints

- `GET /api/v3/app/events?id=:event_id`: Retrieve an event by its ID.
- `GET /api/v3/app/events/latest?type=:event_type&limit=:limit&page=:page`: Retrieve the latest events, filtered by type and paginated.
- `POST /api/v3/app/events`: Create a new event.
- `PUT /api/v3/app/events/:id`: Update an existing event by its ID.
- `DELETE /api/v3/app/events/:id`: Delete an event by its ID.

## Sample Data

The API comes with sample data for testing purposes. You can find the sample events in the `events` list defined in the code.

## Installation

To run the API locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repository.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`

Make sure to have Python and pip installed on your system.

## Usage

You can interact with the API using HTTP client tools like cURL or software like Postman. Here are some example requests:

- Retrieve an event by ID:
GET /api/v3/app/events?id=1

- Create a new event:
POST /api/v3/app/events
Content-Type: application/json

{
"name": "New Event",
"tagline": "Tagline",
"schedule": "2023-06-03",
"description": "Description",
"moderator": "Moderator",
"category": "Category",
"sub_category": "Subcategory",
"rigor_rank": 3
}


- Update an existing event:
PUT /api/v3/app/events/1
Content-Type: application/json

{
"name": "Updated Event",
"description": "Updated description"
}


- Delete an event:
DELETE /api/v3/app/events/1


Feel free to explore the API and customize it according to your requirements.
