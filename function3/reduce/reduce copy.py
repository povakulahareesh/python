
from   functools  import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # 10







'''
📊 Summary Table:
Function----	Use case	----Returns
map()  ---	Transform each element	--Map object (iterator)
filter() ---	Filter elements	 ----Filter object (iterator)
reduce() ---	Reduce to one value	---Single value
'''

# ============================================
'''
✅ map(), filter(), and reduce()
These are used for functional programming — applying functions to sequences (like lists) without writing loops.

🔸 1. map() function
📌 Purpose: Applies a function to each item in a sequence and returns a new iterator.
✅ Syntax:
python
Copy code
map(function, iterable)
✅ Example:
python
Copy code
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]
🔸 2. filter() function
📌 Purpose: Filters the sequence by keeping only items where the function returns True.
✅ Syntax:
python
Copy code
filter(function, iterable)
✅ Example:
python
Copy code
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]
🔸 3. reduce() function (from functools)
📌 Purpose: Applies a function cumulatively to reduce the sequence to a single value.
✅ Syntax:
python
Copy code
from functools import reduce
reduce(function, iterable)
✅ Example:
python
Copy code
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # 10
📊 Summary Table:
Function	Use case	Returns
map()	Transform each element	Map object (iterator)
filter()	Filter elements	Filter object (iterator)
reduce()	Reduce to one value	Single value

🧠 Bonus Tip:
To see the result, you need to convert map() and filter() outputs using list() or loop over them.


'''

























