import os
import time
import pip

print("Setting up environment...")
start_time = time.time()
all_process = [
    ['install', 'torch==1.12.1+cu113', 'torchvision==0.13.1+cu113', '--extra-index-url',
     'https://download.pytorch.org/whl/cu113'],
    ['install', '-U', 'sentence-transformers'],
    ['install', 'httpx'],
]
for process in all_process:
    pip.main(process)

end_time = time.time()
print(f"Environment set up in {end_time - start_time:.0f} seconds")
