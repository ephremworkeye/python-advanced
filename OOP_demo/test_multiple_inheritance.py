class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong', self)

class C(A):
    def pong(self):
        print('PONG', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping: ', self)
    
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


# b= B()
# print(b.ping())
# print(b.pong())

d = D()
# d.pong()
# d.ping()
d.pingpong()
# print(D.__mro__)

# print(C.pong(d))