# Social Vibes API

This is a Flask RESTful API for managing users, events, reviews, attended records, followings, and relationships between them.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or later.
- Visual Studio Code or an IDE of your choice.
- Postman or Insomnia for testing.

### Installing

1. Clone the repository:

   ```

   git clone git@github.com:Tee-K25/Social-Vibes-API.git
   ```

2. Run a virtual environment:

   ```
   pipenv shell
   ```

3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Navigate to the project code:

   ```
   cd Social-Vibes-API
   ```

5. Run the application:

   ```
   python app.py
   ```

   Click on the link created in the terminal, e.g., http://127.0.0.1:5555/

   Running the Tests
   Run the automated tests for this system using Postman or Insomnia.

API Endpoints

- **GET /user/<int:id>:** Returns a single user by ID.
- **PATCH /user/<int:id>:** Updates a user by ID.
- **DELETE /user/<int:id>:** Deletes a user by ID.

- **GET /user/<int:user_id>/reviews:** Returns reviews for a specific user.
- **POST /user/<int:user_id>/reviews:** Adds a new review for a specific user.
- **PATCH /user/<int:user_id>/reviews/<int:id>:** Updates a review for a specific user by ID.
- **DELETE /user/<int:user_id>/reviews/<int:id>:** Deletes a review for a specific user by ID.

- **GET /user/<int:user_id>/events/followed:** Returns events followed by a specific user.
- **POST /user/<int:user_id>/events/followed:** Adds a new event followed by a specific user.
- **DELETE /user/<int:user_id>/events/followed/<int:id>:** Deletes an event followed by a specific user by ID.

- **GET /events:** Returns a list of all events.
- **POST /events:** Adds a new event.

- **GET /event/<int:id>:** Returns a single event by ID.
- **PATCH /event/<int:id>:** Updates an event by ID.
- **DELETE /event/<int:id>:** Deletes an event by ID.

- **GET /reviews:** Returns a list of all reviews.
- **POST /reviews:** Adds a new review.

- **GET /review/<int:id>:** Returns a single review by ID.
- **PATCH /review/<int:id>:** Updates a review by ID.
- **DELETE /review/<int:id>:** Deletes a review by ID.

- **GET /event/<int:event_id>/reviews:** Returns reviews for a specific event.
- **POST /event/<int:event_id>/reviews:** Adds a new review for a specific event.
- **DELETE /event/<int:event_id>/reviews/<int:id>:** Deletes a review for a specific event by ID.

- **GET /followings:** Returns a list of all followings.
- **POST /followings:** Adds a new following.

- **DELETE /followings:** Deletes a following by user_id and event_id.

- **GET /following/<int:id>:** Returns a single following by ID.
- **PATCH /following/<int:id>:** Updates a following by ID.
- **DELETE /following/<int:id>:** Deletes a following by ID.

- **GET /event/<int:event_id>/followings:** Returns followings for a specific event.
- **POST /event/<int:event_id>/followings:** Adds a new following for a specific event.
- **DELETE /event/<int:event_id>/followings/<int:id>:** Deletes a following for a specific event by ID.

Web Browser Interaction
You can view a JSON response of users, events, reviews, attended records, and followings on the web browser by visiting http://127.0.0.1:5555/.

http://127.0.0.1:5555/users - Get all users. Add an ID at the end of the URL to get a single user.
http://127.0.0.1:5555/events - Get all events. Add an ID at the end of the URL to get a single event.
...
Built With
Flask - The web framework used.
Flask_SQLAlchemy - SQL Toolkit and ORM.
Authors
Tony Kiplagat - tony.kiplagat@moringaschool.com
