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

Some wrapper code is available to install any extra libraries that you require via
the `PIP_PRE_INSTALL` environment variable. IF provided, it will be split by commas
and passed to `pip install`.

For example:

```
$ docker run --rm -ti -p 80:80 -e PIP_PRE_INSTALL library1,library2 astromechza/docker-jupyter-datavis
```

## run

```
$ docker run --rm -ti -p 80:80 astromechza/docker-jupyter-datavis
```

**Note**: if you run without the `-p` declaraion, you'll need to work out what
docker ip it is available on.

Mount `/workdir` if you want to keep your notebooks around. Either as a bind mount:

```
$ docker run --rm -ti -p 80:80 -v /tmp/notebooks:/workdir astromechza/docker-jupyter-datavis
```

Or as a named volume (which I prefer):

```
$ docker run --rm -ti -p 80:80 -v jnwd:/workdir astromechza/docker-jupyter-datavis
```

Any other jupyter options can be passed after the container name.
