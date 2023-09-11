
from app import app, db, Todo
import unittest

class TodoIntegrationTestCase(unittest.TestCase):

    # This method will be called before every test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test_db.sqlite'
        self.app = app.test_client()
        db.create_all()

    # This method will be called after every test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_todo_route(self):
        response = self.app.post('/add', data={'title': 'Integration Test Task'}, follow_redirects=True)
        task = Todo.query.filter_by(task='Integration Test Task').first()
        self.assertIsNotNone(task)

    def test_delete_todo_route(self):
        new_todo = Todo(task='Integration Test Task for Deletion', complete=False)
        db.session.add(new_todo)
        db.session.commit()
        task = Todo.query.filter_by(task='Integration Test Task for Deletion').first()
        response = self.app.get(f'/delete/{task.id}', follow_redirects=True)
        task = Todo.query.filter_by(task='Integration Test Task for Deletion').first()
        self.assertIsNone(task)

    def test_update_todo_route(self):
        new_todo = Todo(task='Integration Test Task for Update', complete=False)
        db.session.add(new_todo)
        db.session.commit()
        task = Todo.query.filter_by(task='Integration Test Task for Update').first()
        response = self.app.get(f'/update/{task.id}', follow_redirects=True)
        updated_task = Todo.query.filter_by(task='Integration Test Task for Update').first()
        self.assertTrue(updated_task.complete)

if __name__ == "__main__":
    unittest.main()
