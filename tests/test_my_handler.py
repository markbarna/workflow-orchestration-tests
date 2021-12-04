from handlers import MyHandler

def test_my_handler():
    handler = MyHandler((4,2))
    handler.handle({})