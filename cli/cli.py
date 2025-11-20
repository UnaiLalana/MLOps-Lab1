import os
import sys

import click

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mylib import model

@click.command()
@click.argument('image_path')
def classify_image(image_path):
    """Classify an image located at IMAGE_PATH."""
    try:
        image = model.Image.open(image_path)
    except Exception as e:
        click.echo(f"Error opening image: {e}")
        return

    prediction = model.predict(image)
    click.echo(f"The predicted class for the image is: {prediction}")

