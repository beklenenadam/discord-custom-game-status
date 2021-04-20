from pypresence import Presence
import time

client_id = '833878367140970527'  # Your game client IP
RPC = Presence(client_id)
RPC.connect() # Start the handshake loop

print(RPC.update(state="Oyunda", small_image="sm", large_image="faul", details="Anlatıyor...", party_id="sa", party_size=[4,4], start="13", end="23", buttons=[{"label": "Lobi Oluştur", "url": "https://faul.ga"}]))

while True:
    time.sleep(15) # Can only update rich presence every 15 seconds
