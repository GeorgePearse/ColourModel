# ColourModel
Just a tool which uses OpenCV to create bounding boxes around objects of requested colours.

Just
```
pip install colour-model
```

To 'run inference':
```
from colour_model import ColourModel

colour_model = ColourModel()
colour_model.predict(file_path)
```

Demoed with fiftyone and a colour grid, very easy to swap out with your own directory. Runs very fast, so sometimes useful for looking for rare objects.

Very easy to support more colours, but part of the value in the setup is having some of that done for you.

<img width="802" alt="image" src="https://github.com/GeorgePearse/ColourModel/assets/47161914/feef04c0-7ad8-4bf5-8a04-794ceeabe6d8">

