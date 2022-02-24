# helloWorld.py
from diagrams import Diagram
from diagrams.aws.database import RDS
from diagrams.aws.compute import Lambda

with Diagram("helloWorld", show=False):
    Lambda("Hello world") >> RDS("My database")
