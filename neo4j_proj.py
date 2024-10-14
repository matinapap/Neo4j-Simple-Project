from dotenv import load_dotenv
import os

from langchain_community.graphs import Neo4jGraph

# Warning control
import warnings
warnings.filterwarnings("ignore")

load_dotenv('.env', override=True)
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
NEO4J_DATABASE = os.getenv('NEO4J_DATABASE')

kg = Neo4jGraph(
    url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE
)

cypher = """
  MATCH (n:Student) 
  RETURN count(n) AS numberOfStudents
  """
result = kg.query(cypher)
result
print(f"There are {result[0]['numberOfStudents']} students in the school.")


cypher = """
  MATCH (student1:Student {name:"Jane Smith"}) 
  RETURN student1.name, student1.grade, student1.age
  """
result = kg.query(cypher)
result
print(f"The student {result[0]['student1.name']} has the grade {result[0]['student1.grade']} and she is {result[0]['student1.age']} years old.")

