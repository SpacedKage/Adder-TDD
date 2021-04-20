class Adder:
    def add(self, numbers):

        if numbers == "":
            return 0
        elif len(numbers) == 1:
            return int(numbers)
        
        num_list = numbers.split(" , ")
        num_list = [int(num_str) for num_str in  num_list]
        return sum(num_list)
    
