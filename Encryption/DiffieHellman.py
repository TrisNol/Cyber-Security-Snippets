import random

class DiffieHellman():
    p = None
    g = None

    private_key = None
    public_key = None
    shared_key = None

    def __init__(self, p, g):
        self.p = p
        self.g = g

    def generate_private_key(self):
        self.private_key = random.randint(0, 99999)

    def calc_public_key(self):
        # Equal to (self.g ** self.private_key) % self.p
        return pow(self.g, self.private_key, self.p)

    def set_public_key(self, public_key):
        self.public_key = public_key

    def calculate_shared_key(self):
        self.shared_key = pow(self.public_key, self.private_key, self.p)

if __name__ == "__main__":
    p = 7351
    g = 6 
    d1 = DiffieHellman(p, g)
    d2 = DiffieHellman(p, g)

    d1.generate_private_key()
    d2.generate_private_key() 

    d1.set_public_key(d2.calc_public_key())
    d2.set_public_key(d1.calc_public_key())

    d1.calculate_shared_key()
    d2.calculate_shared_key()

    print('Key 1: '+ str(d1.shared_key))
    print('Key 2: '+ str(d2.shared_key))