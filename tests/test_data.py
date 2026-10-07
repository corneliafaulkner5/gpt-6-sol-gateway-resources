import json,pathlib,unittest
class T(unittest.TestCase):
 def test_resource(self):
  d=json.loads((pathlib.Path(__file__).parents[1]/"data/resources.json").read_text());self.assertEqual(d["model"],"gpt-6-sol")
if __name__=="__main__":unittest.main()
