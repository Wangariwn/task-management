import io
import sys
import subprocess
import unittest

from task_utils import add_task, view_pending_tasks, mark_task_as_complete, calculate_progress

class TaskUtilsTests(unittest.TestCase):
    def test_add_and_progress_and_mark(self):
        tasks = []
        result = add_task(tasks, "Test Task", "Desc", "2026-12-31")
        self.assertTrue(result)
        self.assertEqual(len(tasks), 1)
        self.assertAlmostEqual(calculate_progress(tasks), 0.0)
        mark_task_as_complete(tasks, 0)
        self.assertAlmostEqual(calculate_progress(tasks), 100.0)

    def test_invalid_title(self):
        tasks = []
        result = add_task(tasks, "   ", "Desc", "2026-12-31")
        self.assertFalse(result)
        self.assertEqual(len(tasks), 0)

    def test_view_pending_shows_one_based_index(self):
        tasks = []
        add_task(tasks, "One", "D", "2026-12-31")
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            view_pending_tasks(tasks)
        finally:
            sys.stdout = sys_stdout
        output = captured.getvalue()
        self.assertIn("[1] Title: One", output)

class IOMainTests(unittest.TestCase):
    def test_main_add_and_progress_flow(self):
        # Simulate user: add task, view progress, exit
        user_input = "1\nTask A\nDescription A\n2026-12-31\n4\n5\n"
        proc = subprocess.run(["python3", "main.py"], input=user_input, text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Task added successfully!", proc.stdout)
        self.assertIn("Progress:", proc.stdout)

if __name__ == "__main__":
    unittest.main()
