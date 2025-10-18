from datetime import datetime

now = datetime.now()
print(f"Jest teraz godzina {now.time()}.")
print(f"Jest teraz godzina {now.strftime("%H:%M:%S")}.")
