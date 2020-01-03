# Galaxy-CNNs
## Using three-band SDSS imaging to predict gas-phase metallicity

![](docs/figures/example.png)

We use convolutional neural networks (CNNs or convnets) to predict 
galaxy properties using Sloan Digital Sky Survey (SDSS) *gri* images.
Gas-phase metallicity, which is often estimated by using optical
spectroscopy, can also be estimated using our CNN.

We describe our methods in a paper: Wu & Boada ([2019, MNRAS, 484, 4683](https://ui.adsabs.harvard.edu/abs/2019MNRAS.484.4683W/abstract); [arXiv:1810.12913](https://arxiv.org/abs/1810.12913)).

See also a [simplified demo of our work](https://github.com/jwuphysics/convnet-demo).

## Table of contents
- [Usage](#usage)
  * [Dependencies](#dependencies)
  * [Data sets](#data-sets)
  * [Training and testing](#training-and-testing)
- [Citation](#citation)


## Usage
Download this repository by running
```
git clone https://github.com/jwuphysics/galaxy-cnns.git
cd galaxy-cnns
```

### Dependencies
All analysis was performed inside the Jupyter notebooks using a Python3 environment.
We use version 0.7.0 of the [fastai](https://github.com/fastai/fastai) machine 
learning framework built atop [Pytorch](https://pytorch.org/). This can be installed 
by following the instructions on the Fastai README page. We will soon have working
examples for Fastai version 1.0, which can be installed by running:
```
git clone https://github.com/fastai/fastai.git
cd fastai 
conda env create -f environment.yml
```

Note that you will need a GPU. If you don't have one, substitute the previous last line
with this instead:
```
conda env create -f environment-cpu.yml
```

Before executing any code (or running any notebooks), enter the environment
by running `conda activate fastai` (or `conda activate fastai-cpu`).

If you encounter any errors, please feel free to reach out to me (@jwuphysics)
or check [this post](https://forums.fast.ai/t/fastai-v0-7-install-issues-thread/24652) 
on the fastai forums.


### Data sets
We queried the [SDSS DR14 image cutout service](http://skyserver.sdss.org/dr14/en/help/docs/api.aspx#imgcutout) 
using the script `./download_images.py` in order to obtain *gri* images.

We queried the [SDSS MPA-JHU DR7 catalog](https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/)
of spectral line and derived galaxy properties using the commands in the `SQL` script,
`./SDSS_sql_query.sql`.

### Training and testing

To run the our notebooks, make sure that you are in the `fastai` conda environment first, 
and then run `jupyter notebook` and enter the `./notebook` directory.

If you wish to reproduce all figures from the paper, run the notebooks in the 
`./notebook/paper` directory. You will first need to have downloaded all of the
data and executed the notebooks labeled 
"06. Predicting stellar mass in addition to metallicity.ipynb" and 
"10. The effects of resolution.ipynb" first (sorry about this disorganization -- this
may be cleaned up in a future update).


## Citation
If you would like to reference our [paper]((https://arxiv.org/abs/1810.12913)), 
please use the following citation, produced by 
[NASA ADS](https://ui.adsabs.harvard.edu/abs/2019MNRAS.484.4683W):
```
@ARTICLE{2019MNRAS.484.4683W,
       author = {{Wu}, John F. and {Boada}, Steven},
        title = "{Using convolutional neural networks to predict galaxy metallicity from three-colour images}",
      journal = {Monthly Notices of the Royal Astronomical Society},
         year = "2019",
        month = "Apr",
       volume = {484},
       number = {4},
        pages = {4683-4694},
          doi = {10.1093/mnras/stz333},
archivePrefix = {arXiv},
       eprint = {1810.12913},
 primaryClass = {astro-ph.GA}
 }
```
