
from app import app, db, Todo
import unittest

class TodoUnitTestCase(unittest.TestCase):

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

    def test_add_todo(self):
        new_todo = Todo(task='Test Task', complete=False)
        db.session.add(new_todo)
        db.session.commit()
        task = Todo.query.filter_by(task='Test Task').first()
        self.assertIsNotNone(task)

    def test_get_todo(self):
        new_todo = Todo(task='Test Task', complete=False)
        db.session.add(new_todo)
        db.session.commit()
        task = Todo.query.filter_by(task='Test Task').first()
        self.assertEqual(task.task, 'Test Task')

    def test_update_todo(self):
        new_todo = Todo(task='Test Task', complete=False)
        db.session.add(new_todo)
        db.session.commit()
        task = Todo.query.filter_by(task='Test Task').first()
        task.complete = True
        db.session.commit()
        updated_task = Todo.query.filter_by(task='Test Task').first()
        self.assertTrue(updated_task.complete)

    def test_delete_todo(self):
        new_todo = Todo(task='Test Task', complete=False)
        db.session.add(new_todo)
        db.session.commit()
        task = Todo.query.filter_by(task='Test Task').first()
        db.session.delete(task)
        db.session.commit()
        task = Todo.query.filter_by(task='Test Task').first()
        self.assertIsNone(task)

if __name__ == "__main__":
    unittest.main()
