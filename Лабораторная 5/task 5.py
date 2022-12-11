from random import sample
import string
def get_random_password() -> str:
    n=8
    alphabet=string.ascii_uppercase+string.ascii_lowercase+string.digits
    return ''.join(sample(alphabet, n))

print(get_random_password())
