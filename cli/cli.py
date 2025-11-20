import os
import sys

import click

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mylib import model


@click.group()
def cli():
    """CLI for the model operations."""
    pass


@cli.command()
@click.argument("image_path")
def predict(image_path):
    """Classify an image located at IMAGE_PATH."""
    try:
        image = model.Image.open(image_path)
    except Exception as e:
        click.echo(f"Error opening image: {e}")
        return

    prediction = model.predict(image)
    click.echo(f"The predicted class for the image is: {prediction}")


@cli.command()
@click.argument("image_path")
@click.argument("output_path")
@click.option("--width", type=int, required=True, help="Width of the resized image")
@click.option("--height", type=int, required=True, help="Height of the resized image")
def resize(image_path, output_path, width, height):
    """Resize an image to WIDTH x HEIGHT."""
    try:
        image = model.Image.open(image_path)
        resized_image = model.resize_image(image, (width, height))
        resized_image.save(output_path)
        click.echo(f"Image saved to {output_path}")
    except Exception as e:
        click.echo(f"Error processing image: {e}")


@cli.command()
@click.argument("image_path")
@click.argument("output_path")
def grayscale(image_path, output_path):
    """Convert an image to grayscale."""
    try:
        image = model.Image.open(image_path)
        grayscale_image = model.convert_to_grayscale(image)
        grayscale_image.save(output_path)
        click.echo(f"Grayscale image saved to {output_path}")
    except Exception as e:
        click.echo(f"Error processing image: {e}")


if __name__ == "__main__":
    cli()
