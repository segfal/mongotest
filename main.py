import numpy as np
from pymongo import MongoClient
import random


client = MongoClient('uri');
back = client["backend"]
r = back["random"]

def square(i : int) -> int:
    r.insert_one({"3":"hello"});
    np.abs(i);
    random.random();
    r.insert_one({"3":"Recorded"});
    return i*i;


def backups() -> bool:
    x = 42;

    
    return True;


square(5);
square(10);
square(6);
square(52);