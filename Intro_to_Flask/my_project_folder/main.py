import sqlalchemy as sa
import sqlalchemy.orm as so
from my_app import app, db
from my_app.models import User, Post

import subprocess

@app.shell_context_processor
def make_shell_context():
    return {
        'sa': sa, 
        'so': so, 
        'db': db, 
        'User': User, 
        'Post': Post,
        'gau': get_all_users,
        'trunc': truncate_tables

    }

def get_all_users():
    """Utility function to get all users from the database."""
    query = sa.select(User)
    users = db.session.scalars(query)
    print('hello')
    for u in users:
        print(f'id: {u.id} username: {u.username} email: {u.email} last seen: {u.last_seen} about me info: {u.about_me}')

def truncate_tables():
    """Utility function to truncate all tables in the database."""
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Truncating table {table}')
        db.session.execute(table.delete())
    db.session.commit()


def run_flask_app():
    # Command to run Flask
    command = ['flask', '--app', 'main', 'run', '--reload']

    # Use subprocess to run the command
    process = subprocess.Popen(command, shell=True)

    # Optionally, wait for the process to complete
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

# def run_browser_sync():
#     # Command to run Flask
#     command = ['browser-sync', 'start', '--proxy', 'localhost:5000', '--files', '"**/*"']

#     # Use subprocess to run the command
#     process = subprocess.Popen(command, shell=True)

#     # Optionally, wait for the process to complete
#     try:
#         process.wait()
#     except KeyboardInterrupt:
#         process.terminate()


if __name__ == '__main__':

    run_flask_app()
    

