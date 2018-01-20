# docker-jupyter-datavis

A jupyter notebook for data visualisation encapsulated into a Docker container.

Great for quickly graphing something when you need it!

Or.. keep it running in the background and know that its always available!

## libraries available

```
matplotlib
numpy
scipy
pandas
seaborn
```

Matplotlib is configured with `inline` mode and a `15 x 10` figsize.

A `demo.ipynb` is available in the notebook to get you started.

## build

```
$ docker build -t jn .
```

- Use whatever tag you need, I use `jn` because its short and quick.

## run

```
$ docker run --rm -ti -p 8888:80 jn
```

**Note**: if you run without the `-p` declaraion, you'll need to work out what
docker ip it is available on.

Mount `/workdir` if you want to keep your notebooks around. Either as a bind mount:

```
$ docker run --rm -ti -p 8888:80 -v /tmp/notebooks:/workdir jn
```

Or as a named volume (which I prefer):

```
$ docker run --rm -ti -p 8888:80 -v jnwd:/workdir jn
```

Any other jupyter options can be passed after the `jn`.
