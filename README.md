
# Flask Blog API Consumer

A simple Flask application that displays blog posts using local JSON data.
![simple_blog.png](simple_blog.png)
## Features

- Reads posts from a local JSON file.
- Displays a list of all posts on the homepage.
- Provides a detailed view of a specific post when clicked.

## Setup & Installation

1. Ensure you have Python and Flask installed.
2. Clone the repository:
   ```
   git clone https://github.com/j-breedlove/simple_blog.git
   ```
3. Navigate to the project directory:
   ```
   cd simple_blog
   ```
4. Create environment and Install required packages:
   ```
   pip install pipenv
   pipenv install
   pipenv shell
   pipenv install <package_name>
   ```
5. Run the application:
   ```
   python main.py
   ```

## Endpoints

1. **Homepage** - Displays a list of all posts.
   ```
   GET /
   ```
2. **Specific Post** - Displays details of a specific post.
   ```
   GET /post/<int:post_id>
   ```

## Future Improvements

- Integrate with a database for persistent storage.
- Add authentication and user accounts.
- Allow users to create, update, or delete posts.

