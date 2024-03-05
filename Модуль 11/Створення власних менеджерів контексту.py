class Session:
    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f"connected to {self.addr}:{self.port}")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.connected = False
        if exception_type is not None:
            print("Some error!")
        else:
            print("No problem")

localhost_session = Session("localhost")

with localhost_session as session:
    print(session is localhost_session)     # True
    print(localhost_session.connected)      # True

print(localhost_session.connected)          # False

with Session("localhost") as session:
    print(session.connected)      # True

with Session("host", "port") as session:
    raise Exception("OH NO!")
