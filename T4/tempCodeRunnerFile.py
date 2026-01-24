import random
import time

class CongestionControl:
    def __init__(self):
        self.window_size = 1
        self.max_window = 10

    def send_packets(self):  # sourcery skip: use-named-expression
        print(f"\nSending {self.window_size} packets...")
        
        # Random congestion simulation
        congestion = random.choice([True, False, False])

        if congestion:
            print("⚠ Congestion detected!")
            self.window_size = max(1, self.window_size // 2)
        else:
            print("✅ No congestion")
            if self.window_size < self.max_window:
                self.window_size += 1

    def start(self):
        for _ in range(10):
            self.send_packets()
            time.sleep(1)

# Run simulator
cc = CongestionControl()
cc.start()