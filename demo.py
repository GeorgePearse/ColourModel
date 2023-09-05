import typer
import fiftyone as fo
from get_predictions import get_predictions
from colour_model import ColourModel

def main(
    dir_path: str = "images",
):
    """
    GroundedSAM to crop then DINO + QDrant to classify!
    """
    model = ColourModel()

    dataset = fo.Dataset.from_images_dir(dir_path)
    dataset = get_predictions(dataset, model)

    session = fo.launch_app(dataset, remote=True, address="0.0.0.0", desktop=True)
    session.wait()


if __name__ == "__main__":
    typer.run(main)
