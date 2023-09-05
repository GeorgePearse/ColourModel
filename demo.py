import typer
import os
import fiftyone as fo
from get_predictions import get_predictions


def main(
    limit: int = 10,
    dir_path: str = "../data/test_dataset/data",
):
    """
    GroundedSAM to crop then DINO + QDrant to classify!
    """
    file_paths = [
        os.path.join(test_path, file_name) for file_name in os.listdir(test_path)
    ]

    if limit:
        file_paths = file_paths[:limit]

    model = vc.ModelChain(
        [
            vc.ConditionalDetector(
                model=yolov8,
            ),
            vc.ConditionalDetector(
                model=grounded_sam, 
                frame_level_condition = lambda predictions: any([score < 0.5 for score in predictions.scores]),
                prediction_level_condition = lambda pred: 'cat' in pred.label,
            ),
            vc.ConditionalClassifier(
                model=nn_classifier,
                prediction_level_condition = lambda pred: 'dog' in pred.label,
            ),
        ],
        log_level = 'verbose',
    )

    dataset = fo.Dataset.from_images_dir(dir_path, max_samples=limit)
    dataset = get_predictions(dataset, model)

    session = fo.launch_app(dataset, remote=True, address="0.0.0.0", desktop=True)
    session.wait()


if __name__ == "__main__":
    typer.run(main)
