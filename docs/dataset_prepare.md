## HazeWorld

**HazeWorld** is a large-scale synthetic outdoor video dehazing dataset, 
which is built upon [Cityscapes](https://www.cityscapes-dataset.com/),
[DDAD](https://github.com/TRI-ML/DDAD),
[UA-DETRAC](https://detrac-db.rit.albany.edu/),
[VisDrone](https://github.com/VisDrone/VisDrone-Dataset),
[DAVIS](https://davischallenge.org/),
and [REDS](https://seungjunnah.github.io/Datasets/reds.html).
We use [RCVD](https://robust-cvd.github.io/) to estimate the temporally consistent video depths, which are used to synthesize the hazy videos.

## Prepare datasets

It is recommended to symlink the dataset root to `$MAP-NET/data`.
If your folder structure is different, you may need to change the corresponding paths in config files.



### Cityscapes

The data could be found [here](https://www.cityscapes-dataset.com/downloads/) after registration.

### Others

For others, we provide the processed data [here]().
You can also refer to their official websites for the original data.