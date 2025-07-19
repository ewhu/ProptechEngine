# test_proptechengine.py
"""
Tests for ProptechEngine module.
"""

import unittest
from proptechengine import ProptechEngine

class TestProptechEngine(unittest.TestCase):
    """Test cases for ProptechEngine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProptechEngine()
        self.assertIsInstance(instance, ProptechEngine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProptechEngine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
