from my_context_manager import MyContextManager
from payload.prime_number import prime_number

with MyContextManager('test.log'):
    prime_number(1000000)
