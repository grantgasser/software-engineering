
# given int n > 0, generate all valid combinations of n pairs of parenthesis

# 1, ()
# 2, (()), ()()
# 3, ((())), ()()(), (()()), (()) (), () (())

def valid_combinations(n):
  combinations = set(["()"])
  
  # wrap (x), append to end x (), append to begin () x
  for i in range(1, n):
    new_combinations = set()
    for j in combinations:
      # wrap 
      wrapped = "(" + j + ")"
      new_combinations.add(wrapped)
      
      # append to end
      end = j + "()"
      new_combinations.add(end)
      
      # append to begin
      begin = "()" + j
      new_combinations.add(begin)
    
    # update  
    combinations = new_combinations
 
  return combinations   
  
  
  


if __name__ == "__main__":
  print(valid_combinations(n=1))
  print(valid_combinations(n=2))
  print(valid_combinations(n=3))
  
  
