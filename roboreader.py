import edge_tts
import asyncio

async def speak(text):
    output = "output.mp3"
    tts = edge_tts.Communicate(text, voice="en-US-ChristopherNeural")
    await tts.save(output)
    print("Saved output.mp3")

print("Welcome")
x = input("Enter what you wanna listen: ")
asyncio.run(speak(x))
