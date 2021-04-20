from adder import Adder

def test_add_empty_string():
    adder = Adder()

    assert adder.add("") == 0                   

def test_add_one_value():
    adder = Adder()

    assert adder.add("8") == 8                 

def test_add_two_values():
   adder = Adder()

   assert adder.add("15, 9") == 24                

