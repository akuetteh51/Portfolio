import click
from flask import Flask
import os
from pathlib import Path

images=os.scandir()
for i in images:
	print(Path(images))

