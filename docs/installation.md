## Local Installation

The `Q-Twin` software can be installed using conda. Assuming conda is already installed, run the following command in a terminal:
```bash
conda create --name qtwin --file requirements.txt
conda activate qtwin
```

<details>
<summary><b>Click to view the installation logs</b></summary>

```text
> conda create --name qtwin --file requirements.txt
Retrieving notices: done
Channels:
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
    current version: 25.11.0
    latest version: 26.7.2

Please update conda by running

    $ conda update -n base -c conda-forge conda



## Package Plan ##

  environment location: /global/homes/g/guangc/.conda/envs/qtwin

  added / updated specs:
    - mdanalysis==2.10.0
    - numba==0.63.1
    - numpy==2.3.5
    - pandas==2.3.3
    - plotly==6.5.0
    - scipy==1.16.3
    - streamlit==1.52.2


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    _openmp_mutex-4.5          |           20_gnu          28 KB  conda-forge
    _python_abi3_support-1.0   |       hd8ed1ab_3           8 KB  conda-forge
    altair-6.2.2               |     pyhd8ed1ab_0         554 KB  conda-forge
    attrs-26.1.0               |     pyhcf101f3_0          63 KB  conda-forge
    aws-c-auth-0.10.4          |       hb7a77c6_1         132 KB  conda-forge
    aws-c-cal-0.9.14           |       h2aa3ae6_4          55 KB  conda-forge
    aws-c-common-0.14.2        |       hb03c661_0         240 KB  conda-forge
    aws-c-compression-0.3.2    |       h720e601_4          22 KB  conda-forge
    aws-c-event-stream-0.7.1   |       h6ffeea8_4          58 KB  conda-forge
    aws-c-http-0.11.0          |       h38ae05a_4         226 KB  conda-forge
    aws-c-io-0.27.3            |       h6f4d18d_1         179 KB  conda-forge
    aws-c-mqtt-0.16.0          |       h21f4ec5_2         220 KB  conda-forge
    aws-c-s3-0.12.8            |       h46fcd08_1         153 KB  conda-forge
    aws-c-sdkutils-0.2.7       |       h720e601_2          67 KB  conda-forge
    aws-checksums-0.2.10       |       h720e601_4         100 KB  conda-forge
    aws-crt-cpp-0.40.1         |       h102d43b_3         407 KB  conda-forge
    aws-sdk-cpp-1.11.833       |       hc7390e0_9         3.2 MB  conda-forge
    azure-core-cpp-1.16.3      |       h206d751_0         341 KB  conda-forge
    azure-identity-cpp-1.13.3  |       h71f81a8_2         245 KB  conda-forge
    azure-storage-blobs-cpp-12.18.0|       h74b55db_1         576 KB  conda-forge
    azure-storage-common-cpp-12.14.0|       hf596fc9_1         156 KB  conda-forge
    azure-storage-files-datalake-cpp-12.16.0|       h1f05bef_1         301 KB  conda-forge
    backports.zstd-1.7.0       |  py314h680f03e_1           7 KB  conda-forge
    blinker-1.9.0              |     pyhff2d567_0          14 KB  conda-forge
    brotli-1.2.0               |       h505cf86_4          20 KB  conda-forge
    brotli-bin-1.2.0           |       h9908984_4          21 KB  conda-forge
    brotli-python-1.2.0        |  py314hcd2bdb6_4         359 KB  conda-forge
    bzip2-1.0.8                |      hda65f42_10         252 KB  conda-forge
    c-ares-1.34.8              |       hebe6cf0_2         223 KB  conda-forge
    ca-certificates-2026.7.22  |       hbd8a1cb_0         129 KB  conda-forge
    cached-property-2.0.1      |     pyhcf101f3_0           4 KB  conda-forge
    cached_property-2.0.1      |     pyhcf101f3_0          16 KB  conda-forge
    cachetools-6.2.6           |     pyhd8ed1ab_0          17 KB  conda-forge
    cairo-1.18.4               |       h3c89d7e_3         968 KB  conda-forge
    certifi-2026.7.22          |     pyhd8ed1ab_0         134 KB  conda-forge
    cftime-1.6.5               |  py314h12ceea2_2         467 KB  conda-forge
    charset-normalizer-3.5.1   |     pyhd8ed1ab_0          63 KB  conda-forge
    click-8.5.0                |     pyh5ded981_0         110 KB  conda-forge
    cloudpickle-3.1.2          |     pyhcf101f3_1          27 KB  conda-forge
    contourpy-1.4.0            |  py314h5383ef5_0         324 KB  conda-forge
    cpython-3.14.7             |py314hd8ed1ab_106          50 KB  conda-forge
    cycler-0.12.1              |     pyhcf101f3_2          14 KB  conda-forge
    filelock-3.32.6            |     pyhd8ed1ab_0          77 KB  conda-forge
    fontconfig-2.18.3          |       h4db4eae_1         289 KB  conda-forge
    fonts-conda-forge-1        |       hc364b38_1           4 KB  conda-forge
    fonttools-4.65.0           |  py314hd42368d_0         3.0 MB  conda-forge
    formulaic-1.2.2            |     pyhd8ed1ab_0          88 KB  conda-forge
    freetype-2.14.3            |       ha770c72_2         171 KB  conda-forge
    fribidi-1.0.16             |       h7cc23a3_2          61 KB  conda-forge
    gflags-2.3.1               |       h54a6638_0         128 KB  conda-forge
    gitdb-4.0.12               |     pyhd8ed1ab_0          52 KB  conda-forge
    gitpython-3.1.62           |     pyh5ded981_0         175 KB  conda-forge
    glog-0.7.1                 |       hb7133d2_1         146 KB  conda-forge
    graphite2-1.3.15           |       h54a6638_1         100 KB  conda-forge
    griddataformats-1.2.0      |     pyhd8ed1ab_0         5.3 MB  conda-forge
    gsd-5.0.1                  |       h7c397b8_1         236 KB  conda-forge
    h2-4.4.1                   |     pyhcf101f3_0          98 KB  conda-forge
    h5py-3.16.0                |nompi_py314he0d6181_104         1.3 MB  conda-forge
    hdf5-1.14.6                |nompi_h19486de_110         3.5 MB  conda-forge
    hpack-4.2.0                |     pyhd8ed1ab_0          32 KB  conda-forge
    icu-78.3                   |  py310h44b86e0_2        13.8 MB  conda-forge
    idna-3.19                  |     pyhcf101f3_0         173 KB  conda-forge
    importlib-metadata-9.0.1   |     pyhcf101f3_0          34 KB  conda-forge
    interface_meta-1.3.0       |     pyhd8ed1ab_1          18 KB  conda-forge
    jinja2-3.1.6               |     pyhcf101f3_1         118 KB  conda-forge
    joblib-1.6.0               |     pyhcf101f3_0         223 KB  conda-forge
    jsonschema-4.26.0          |     pyhcf101f3_1          80 KB  conda-forge
    jsonschema-specifications-2025.9.1|     pyhcf101f3_0          19 KB  conda-forge
    keyutils-1.6.3             |       h7cc23a3_1         132 KB  conda-forge
    kiwisolver-1.5.1           |  py314h5383ef5_1          74 KB  conda-forge
    krb5-1.22.2                |       hbc21106_2         1.3 MB  conda-forge
    lcms2-2.19.1               |       h9073bf1_3         248 KB  conda-forge
    ld_impl_linux-64-2.46.1    |default_hbd61a6d_102         728 KB  conda-forge
    lerc-4.2.0                 |       hdb68285_0         265 KB  conda-forge
    libabseil-20260107.1       | cxx17_h7b12aa8_0         1.3 MB  conda-forge
    libaec-1.1.5               |       h088129d_0          36 KB  conda-forge
    libarrow-24.0.0            |   h3e48024_9_cpu         6.2 MB  conda-forge
    libarrow-acero-24.0.0      |   h635bf11_9_cpu         577 KB  conda-forge
    libarrow-compute-24.0.0    |   h53684a4_9_cpu         2.9 MB  conda-forge
    libarrow-dataset-24.0.0    |   h635bf11_9_cpu         577 KB  conda-forge
    libarrow-substrait-24.0.0  |   hb4dd7c2_9_cpu         489 KB  conda-forge
    libblas-3.11.0             |11_h4a7cf45_openblas          18 KB  conda-forge
    libbrotlicommon-1.2.0      |       h39a168f_4          79 KB  conda-forge
    libbrotlidec-1.2.0         |       ha411449_4          34 KB  conda-forge
    libbrotlienc-1.2.0         |       h018ffa1_4         291 KB  conda-forge
    libcblas-3.11.0            |11_h0358290_openblas          18 KB  conda-forge
    libcrc32c-1.1.2            |       h9c3ff4c_0          20 KB  conda-forge
    libcurl-8.22.0             |       ha042cf0_0         488 KB  conda-forge
    libdeflate-1.25            |       hd45a770_1          72 KB  conda-forge
    libedit-3.1.20250104       | pl5321h373387f_1         132 KB  conda-forge
    libev-4.33                 |       h280c20c_3          42 KB  conda-forge
    libevent-2.1.12            |       h5348a74_2         421 KB  conda-forge
    libexpat-2.8.1             |       hecca717_1          76 KB  conda-forge
    libffi-3.7.0               |       h81df57d_1          66 KB  conda-forge
    libfreetype-2.14.3         |       ha770c72_2           8 KB  conda-forge
    libfreetype6-2.14.3        |       h5e6c136_2         379 KB  conda-forge
    libgcc-16.2.0              |       ha9f2e26_5         1.0 MB  conda-forge
    libgcc-ng-16.2.0           |       h69a702a_5          28 KB  conda-forge
    libgfortran-16.2.0         |       h69a702a_5          28 KB  conda-forge
    libgfortran5-16.2.0        |       h6b99dfc_5         2.4 MB  conda-forge
    libglib-2.90.0             |       h569388d_0         4.6 MB  conda-forge
    libgomp-16.2.0             |       he0feb66_5         627 KB  conda-forge
    libgoogle-cloud-3.6.0      |       h8d2ee43_0         2.6 MB  conda-forge
    libgoogle-cloud-storage-3.6.0|       hdbdcf42_0         767 KB  conda-forge
    libgrpc-1.78.1             |       h1d1128b_0         6.7 MB  conda-forge
    libharfbuzz-14.4.0         |       h23af247_1         1.3 MB  conda-forge
    libiconv-1.18              |       h0cb94f2_3         771 KB  conda-forge
    libjpeg-turbo-3.2.0        |       hb03c661_1         635 KB  conda-forge
    liblapack-3.11.0           |11_h47877c9_openblas          18 KB  conda-forge
    liblzma-5.8.3              |       hb03c661_1         110 KB  conda-forge
    libmpdec-4.0.0             |       hb03c661_2          91 KB  conda-forge
    libnetcdf-4.10.1           |nompi_h3fa17b5_201         982 KB  conda-forge
    libnghttp2-1.68.1          |       h74cf4be_1         635 KB  conda-forge
    libopenblas-0.3.34         |pthreads_hf13c14d_2         6.5 MB  conda-forge
    libopentelemetry-cpp-1.27.0|       h9692893_0         921 KB  conda-forge
    libopentelemetry-cpp-headers-1.27.0|       ha770c72_0         383 KB  conda-forge
    libparquet-24.0.0          |   h7376487_9_cpu         1.4 MB  conda-forge
    libpng-1.6.58              |       h922cc85_1         309 KB  conda-forge
    libprotobuf-6.33.5         |       h538a264_2         3.5 MB  conda-forge
    libpsl-0.23.1              |       hd9e3e90_1          71 KB  conda-forge
    libpython-3.14.7           |hdc7f604_106_cp314        10.0 MB  conda-forge
    libraqm-0.11.0             |       h6406941_0          33 KB  conda-forge
    libre2-11-2025.11.05       |       h0dc7533_1         208 KB  conda-forge
    libsqlite-3.53.4           |       h13e7031_1         952 KB  conda-forge
    libssh2-1.11.1             |       h6154650_1         299 KB  conda-forge
    libstdcxx-16.2.0           |       h934c35e_5         6.3 MB  conda-forge
    libstdcxx-ng-16.2.0        |       hdf11a46_5          28 KB  conda-forge
    libthrift-0.22.0           |       h7d032f7_2         414 KB  conda-forge
    libtiff-4.7.2              |       hcc2c06a_1         449 KB  conda-forge
    libutf8proc-2.11.3         |       hfe17d71_0          84 KB  conda-forge
    libuuid-2.42.3             |       hcfc3c73_0          39 KB  conda-forge
    libwebp-base-1.6.0         |       hd42ef1d_1         418 KB  conda-forge
    libxcb-1.17.0              |       hb83e432_2         386 KB  conda-forge
    libxml2-2.15.4             |       h7df9aa5_0          46 KB  conda-forge
    libxml2-16-2.15.4          |       hf3af7cc_0         556 KB  conda-forge
    libzip-1.11.2              |       h6008cf6_1         110 KB  conda-forge
    libzlib-1.3.2              |       h25fd6f3_3          62 KB  conda-forge
    llvmlite-0.46.0            |  py314h946fb2a_0        32.5 MB  conda-forge
    lz4-c-1.10.0               |       hee9eb32_2         178 KB  conda-forge
    markupsafe-3.0.3           |  py314h67df5f8_1          27 KB  conda-forge
    matplotlib-base-3.11.2     |  py314h9124352_0         8.8 MB  conda-forge
    mda-xdrlib-0.2.0           |     pyhd8ed1ab_1          16 KB  conda-forge
    mdanalysis-2.10.0          |  py314ha0b5721_1         5.1 MB  conda-forge
    mrcfile-1.5.4              |     pyhd8ed1ab_0          38 KB  conda-forge
    msgpack-python-1.2.2       |  py314h5383ef5_2         113 KB  conda-forge
    munkres-1.1.4              |     pyhd8ed1ab_1          15 KB  conda-forge
    narwhals-2.26.0            |     pyh5ded981_0         290 KB  conda-forge
    ncurses-6.6                |       hdb14827_1         890 KB  conda-forge
    netcdf4-1.7.4              |nompi_py311hc841c2f_109         1.0 MB  conda-forge
    networkx-3.6.1             |     pyhcf101f3_0         1.5 MB  conda-forge
    nlohmann_json-3.12.0       |       h54a6638_2         133 KB  conda-forge
    numba-0.63.1               |  py314h8169c2f_0         5.5 MB  conda-forge
    numpy-2.3.5                |  py314h2b28147_1         8.6 MB  conda-forge
    openjpeg-2.5.4             |       heb1ab33_2         382 KB  conda-forge
    openssl-3.6.4              |       h781a0a9_0         3.1 MB  conda-forge
    orc-2.3.0                  |       h21090e2_0         1.4 MB  conda-forge
    packaging-26.3             |     pyhc364b38_0         114 KB  conda-forge
    pandas-2.3.3               |  py314ha0b5721_2        14.5 MB  conda-forge
    patsy-1.0.3                |     pyhcf101f3_0         189 KB  conda-forge
    pcre2-10.47                |       h8b3dc9c_1         1.2 MB  conda-forge
    pillow-12.3.0              |  py314h50bfbbb_4         1.1 MB  conda-forge
    pip-26.2.1                 |     pyh145f28c_0         1.1 MB  conda-forge
    pixman-0.46.4              |       h54a6638_3         368 KB  conda-forge
    plotly-6.5.0               |     pyhd8ed1ab_0         4.9 MB  conda-forge
    prometheus-cpp-1.3.0       |       h26ae035_1         191 KB  conda-forge
    protobuf-6.33.5            |  py314h61e7c5f_2         480 KB  conda-forge
    pthread-stubs-0.4          |    h7cc23a3_1004           9 KB  conda-forge
    pyarrow-24.0.0             |  py314hdafbbf9_0          26 KB  conda-forge
    pyarrow-core-24.0.0        |py314h969be7f_0_cpu         4.6 MB  conda-forge
    pydeck-0.9.3               |     pyhd8ed1ab_0         8.0 MB  conda-forge
    pyedr-0.8.0                |     pyhd8ed1ab_1         337 KB  conda-forge
    pyparsing-3.3.2            |     pyhcf101f3_0         108 KB  conda-forge
    python-3.14.7              |hcd007b5_106_cp314        25.3 MB  conda-forge
    python-gil-3.14.7          |     h4df99d1_106          50 KB  conda-forge
    python-tzdata-2026.3       |     pyhd8ed1ab_0         143 KB  conda-forge
    python_abi-3.14            |          9_cp314           7 KB  conda-forge
    pytng-0.3.4                |  py314hddf221e_0         510 KB  conda-forge
    pytz-2026.3.post1          |     pyhcf101f3_0         196 KB  conda-forge
    pyyaml-6.0.3               |  py314h67df5f8_1         198 KB  conda-forge
    qhull-2020.2               |       h434a139_5         540 KB  conda-forge
    re2-2025.11.05             |       h5301d42_1          27 KB  conda-forge
    readline-8.3               |       hd6e31c0_1         341 KB  conda-forge
    referencing-0.37.0         |     pyhcf101f3_0          51 KB  conda-forge
    requests-2.34.2            |     pyhcf101f3_0          67 KB  conda-forge
    rpds-py-2026.6.3           |  py314h7e8cd81_2         293 KB  conda-forge
    s2n-1.7.5                  |       h7e3ee7f_1         383 KB  conda-forge
    scikit-learn-1.9.1         |np2py314h9e1d7c2_0         9.8 MB  conda-forge
    scipy-1.16.3               |  py314hf07bd8e_2        16.2 MB  conda-forge
    seaborn-0.13.2             |       hd8ed1ab_3           7 KB  conda-forge
    seaborn-base-0.13.2        |     pyhd8ed1ab_3         223 KB  conda-forge
    smmap-5.0.3                |     pyhcf101f3_1          27 KB  conda-forge
    snappy-1.2.2               |       h03e3b7b_1          45 KB  conda-forge
    statsmodels-0.15.0         |np2py314h8874201_1        13.5 MB  conda-forge
    streamlit-1.52.2           |     pyhd8ed1ab_0         7.1 MB  conda-forge
    tenacity-9.1.4             |     pyhcf101f3_0          31 KB  conda-forge
    threadpoolctl-3.7.0        |     pyhc455866_0          31 KB  conda-forge
    tk-8.6.13                  | noxft_h1df4ec4_4         3.4 MB  conda-forge
    toml-0.10.2                |     pyhcf101f3_3          23 KB  conda-forge
    tornado-6.5.8              |  py314h89acca1_2         904 KB  conda-forge
    tqdm-4.70.1                |     pyhfa0c392_0          94 KB  conda-forge
    typing-extensions-4.16.0   |       h69aa097_0          92 KB  conda-forge
    typing_extensions-4.16.0   |     pyhcf101f3_0          51 KB  conda-forge
    tzdata-2026c               |       h151e31d_0         116 KB  conda-forge
    urllib3-2.8.0              |     pyhd8ed1ab_0         105 KB  conda-forge
    watchdog-6.0.0             |  py314h9e666f3_4         159 KB  conda-forge
    wrapt-2.4.0                |  py314hfe1a184_2         143 KB  conda-forge
    xorg-libice-1.1.2          |       h280c20c_0          61 KB  conda-forge
    xorg-libsm-1.2.6           |       h0d788c3_1          30 KB  conda-forge
    xorg-libx11-1.8.13         |       he1eb515_1         820 KB  conda-forge
    xorg-libxau-1.0.12         |       h7cc23a3_2          18 KB  conda-forge
    xorg-libxdmcp-1.1.5        |       hb03c661_2          21 KB  conda-forge
    xorg-libxext-1.3.7         |       h7cc23a3_1          52 KB  conda-forge
    xorg-libxrender-0.9.12     |       hb03c661_1          34 KB  conda-forge
    yaml-0.2.5                 |       hebe6cf0_3          83 KB  conda-forge
    zipp-4.1.0                 |     pyhcf101f3_0          24 KB  conda-forge
    zlib-1.3.2                 |       h25fd6f3_3          94 KB  conda-forge
    zlib-ng-2.3.3              |       hce19668_1         121 KB  conda-forge
    zstd-1.5.7                 |       hb78ec9c_7         587 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       301.7 MB

The following NEW packages will be INSTALLED:

  _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-20_gnu 
  _python_abi3_supp~ conda-forge/noarch::_python_abi3_support-1.0-hd8ed1ab_3 
  altair             conda-forge/noarch::altair-6.2.2-pyhd8ed1ab_0 
  attrs              conda-forge/noarch::attrs-26.1.0-pyhcf101f3_0 
  aws-c-auth         conda-forge/linux-64::aws-c-auth-0.10.4-hb7a77c6_1 
  aws-c-cal          conda-forge/linux-64::aws-c-cal-0.9.14-h2aa3ae6_4 
  aws-c-common       conda-forge/linux-64::aws-c-common-0.14.2-hb03c661_0 
  aws-c-compression  conda-forge/linux-64::aws-c-compression-0.3.2-h720e601_4 
  aws-c-event-stream conda-forge/linux-64::aws-c-event-stream-0.7.1-h6ffeea8_4 
  aws-c-http         conda-forge/linux-64::aws-c-http-0.11.0-h38ae05a_4 
  aws-c-io           conda-forge/linux-64::aws-c-io-0.27.3-h6f4d18d_1 
  aws-c-mqtt         conda-forge/linux-64::aws-c-mqtt-0.16.0-h21f4ec5_2 
  aws-c-s3           conda-forge/linux-64::aws-c-s3-0.12.8-h46fcd08_1 
  aws-c-sdkutils     conda-forge/linux-64::aws-c-sdkutils-0.2.7-h720e601_2 
  aws-checksums      conda-forge/linux-64::aws-checksums-0.2.10-h720e601_4 
  aws-crt-cpp        conda-forge/linux-64::aws-crt-cpp-0.40.1-h102d43b_3 
  aws-sdk-cpp        conda-forge/linux-64::aws-sdk-cpp-1.11.833-hc7390e0_9 
  azure-core-cpp     conda-forge/linux-64::azure-core-cpp-1.16.3-h206d751_0 
  azure-identity-cpp conda-forge/linux-64::azure-identity-cpp-1.13.3-h71f81a8_2 
  azure-storage-blo~ conda-forge/linux-64::azure-storage-blobs-cpp-12.18.0-h74b55db_1 
  azure-storage-com~ conda-forge/linux-64::azure-storage-common-cpp-12.14.0-hf596fc9_1 
  azure-storage-fil~ conda-forge/linux-64::azure-storage-files-datalake-cpp-12.16.0-h1f05bef_1 
  backports.zstd     conda-forge/noarch::backports.zstd-1.7.0-py314h680f03e_1 
  blinker            conda-forge/noarch::blinker-1.9.0-pyhff2d567_0 
  blosc              conda-forge/linux-64::blosc-1.21.6-he440d0b_1 
  brotli             conda-forge/linux-64::brotli-1.2.0-h505cf86_4 
  brotli-bin         conda-forge/linux-64::brotli-bin-1.2.0-h9908984_4 
  brotli-python      conda-forge/linux-64::brotli-python-1.2.0-py314hcd2bdb6_4 
  bzip2              conda-forge/linux-64::bzip2-1.0.8-hda65f42_10 
  c-ares             conda-forge/linux-64::c-ares-1.34.8-hebe6cf0_2 
  ca-certificates    conda-forge/noarch::ca-certificates-2026.7.22-hbd8a1cb_0 
  cached-property    conda-forge/noarch::cached-property-2.0.1-pyhcf101f3_0 
  cached_property    conda-forge/noarch::cached_property-2.0.1-pyhcf101f3_0 
  cachetools         conda-forge/noarch::cachetools-6.2.6-pyhd8ed1ab_0 
  cairo              conda-forge/linux-64::cairo-1.18.4-h3c89d7e_3 
  certifi            conda-forge/noarch::certifi-2026.7.22-pyhd8ed1ab_0 
  cftime             conda-forge/linux-64::cftime-1.6.5-py314h12ceea2_2 
  charset-normalizer conda-forge/noarch::charset-normalizer-3.5.1-pyhd8ed1ab_0 
  click              conda-forge/noarch::click-8.5.0-pyh5ded981_0 
  cloudpickle        conda-forge/noarch::cloudpickle-3.1.2-pyhcf101f3_1 
  contourpy          conda-forge/linux-64::contourpy-1.4.0-py314h5383ef5_0 
  cpython            conda-forge/noarch::cpython-3.14.7-py314hd8ed1ab_106 
  cycler             conda-forge/noarch::cycler-0.12.1-pyhcf101f3_2 
  filelock           conda-forge/noarch::filelock-3.32.6-pyhd8ed1ab_0 
  font-ttf-dejavu-s~ conda-forge/noarch::font-ttf-dejavu-sans-mono-2.37-hab24e00_0 
  font-ttf-inconsol~ conda-forge/noarch::font-ttf-inconsolata-3.000-h77eed37_0 
  font-ttf-source-c~ conda-forge/noarch::font-ttf-source-code-pro-2.038-h77eed37_0 
  font-ttf-ubuntu    conda-forge/noarch::font-ttf-ubuntu-0.83-h77eed37_3 
  fontconfig         conda-forge/linux-64::fontconfig-2.18.3-h4db4eae_1 
  fonts-conda-ecosy~ conda-forge/noarch::fonts-conda-ecosystem-1-0 
  fonts-conda-forge  conda-forge/noarch::fonts-conda-forge-1-hc364b38_1 
  fonttools          conda-forge/linux-64::fonttools-4.65.0-py314hd42368d_0 
  formulaic          conda-forge/noarch::formulaic-1.2.2-pyhd8ed1ab_0 
  freetype           conda-forge/linux-64::freetype-2.14.3-ha770c72_2 
  fribidi            conda-forge/linux-64::fribidi-1.0.16-h7cc23a3_2 
  gflags             conda-forge/linux-64::gflags-2.3.1-h54a6638_0 
  gitdb              conda-forge/noarch::gitdb-4.0.12-pyhd8ed1ab_0 
  gitpython          conda-forge/noarch::gitpython-3.1.62-pyh5ded981_0 
  glog               conda-forge/linux-64::glog-0.7.1-hb7133d2_1 
  graphite2          conda-forge/linux-64::graphite2-1.3.15-h54a6638_1 
  griddataformats    conda-forge/noarch::griddataformats-1.2.0-pyhd8ed1ab_0 
  gsd                conda-forge/linux-64::gsd-5.0.1-h7c397b8_1 
  h2                 conda-forge/noarch::h2-4.4.1-pyhcf101f3_0 
  h5py               conda-forge/linux-64::h5py-3.16.0-nompi_py314he0d6181_104 
  hdf4               conda-forge/linux-64::hdf4-4.2.15-h2a13503_7 
  hdf5               conda-forge/linux-64::hdf5-1.14.6-nompi_h19486de_110 
  hpack              conda-forge/noarch::hpack-4.2.0-pyhd8ed1ab_0 
  hyperframe         conda-forge/noarch::hyperframe-6.1.0-pyhd8ed1ab_0 
  icu                conda-forge/linux-64::icu-78.3-py310h44b86e0_2 
  idna               conda-forge/noarch::idna-3.19-pyhcf101f3_0 
  importlib-metadata conda-forge/noarch::importlib-metadata-9.0.1-pyhcf101f3_0 
  interface_meta     conda-forge/noarch::interface_meta-1.3.0-pyhd8ed1ab_1 
  jinja2             conda-forge/noarch::jinja2-3.1.6-pyhcf101f3_1 
  joblib             conda-forge/noarch::joblib-1.6.0-pyhcf101f3_0 
  jsonschema         conda-forge/noarch::jsonschema-4.26.0-pyhcf101f3_1 
  jsonschema-specif~ conda-forge/noarch::jsonschema-specifications-2025.9.1-pyhcf101f3_0 
  keyutils           conda-forge/linux-64::keyutils-1.6.3-h7cc23a3_1 
  kiwisolver         conda-forge/linux-64::kiwisolver-1.5.1-py314h5383ef5_1 
  krb5               conda-forge/linux-64::krb5-1.22.2-hbc21106_2 
  lcms2              conda-forge/linux-64::lcms2-2.19.1-h9073bf1_3 
  ld_impl_linux-64   conda-forge/linux-64::ld_impl_linux-64-2.46.1-default_hbd61a6d_102 
  lerc               conda-forge/linux-64::lerc-4.2.0-hdb68285_0 
  libabseil          conda-forge/linux-64::libabseil-20260107.1-cxx17_h7b12aa8_0 
  libaec             conda-forge/linux-64::libaec-1.1.5-h088129d_0 
  libarrow           conda-forge/linux-64::libarrow-24.0.0-h3e48024_9_cpu 
  libarrow-acero     conda-forge/linux-64::libarrow-acero-24.0.0-h635bf11_9_cpu 
  libarrow-compute   conda-forge/linux-64::libarrow-compute-24.0.0-h53684a4_9_cpu 
  libarrow-dataset   conda-forge/linux-64::libarrow-dataset-24.0.0-h635bf11_9_cpu 
  libarrow-substrait conda-forge/linux-64::libarrow-substrait-24.0.0-hb4dd7c2_9_cpu 
  libblas            conda-forge/linux-64::libblas-3.11.0-11_h4a7cf45_openblas 
  libbrotlicommon    conda-forge/linux-64::libbrotlicommon-1.2.0-h39a168f_4 
  libbrotlidec       conda-forge/linux-64::libbrotlidec-1.2.0-ha411449_4 
  libbrotlienc       conda-forge/linux-64::libbrotlienc-1.2.0-h018ffa1_4 
  libcblas           conda-forge/linux-64::libcblas-3.11.0-11_h0358290_openblas 
  libcrc32c          conda-forge/linux-64::libcrc32c-1.1.2-h9c3ff4c_0 
  libcurl            conda-forge/linux-64::libcurl-8.22.0-ha042cf0_0 
  libdeflate         conda-forge/linux-64::libdeflate-1.25-hd45a770_1 
  libedit            conda-forge/linux-64::libedit-3.1.20250104-pl5321h373387f_1 
  libev              conda-forge/linux-64::libev-4.33-h280c20c_3 
  libevent           conda-forge/linux-64::libevent-2.1.12-h5348a74_2 
  libexpat           conda-forge/linux-64::libexpat-2.8.1-hecca717_1 
  libffi             conda-forge/linux-64::libffi-3.7.0-h81df57d_1 
  libfreetype        conda-forge/linux-64::libfreetype-2.14.3-ha770c72_2 
  libfreetype6       conda-forge/linux-64::libfreetype6-2.14.3-h5e6c136_2 
  libgcc             conda-forge/linux-64::libgcc-16.2.0-ha9f2e26_5 
  libgcc-ng          conda-forge/linux-64::libgcc-ng-16.2.0-h69a702a_5 
  libgfortran        conda-forge/linux-64::libgfortran-16.2.0-h69a702a_5 
  libgfortran5       conda-forge/linux-64::libgfortran5-16.2.0-h6b99dfc_5 
  libglib            conda-forge/linux-64::libglib-2.90.0-h569388d_0 
  libgomp            conda-forge/linux-64::libgomp-16.2.0-he0feb66_5 
  libgoogle-cloud    conda-forge/linux-64::libgoogle-cloud-3.6.0-h8d2ee43_0 
  libgoogle-cloud-s~ conda-forge/linux-64::libgoogle-cloud-storage-3.6.0-hdbdcf42_0 
  libgrpc            conda-forge/linux-64::libgrpc-1.78.1-h1d1128b_0 
  libharfbuzz        conda-forge/linux-64::libharfbuzz-14.4.0-h23af247_1 
  libiconv           conda-forge/linux-64::libiconv-1.18-h0cb94f2_3 
  libjpeg-turbo      conda-forge/linux-64::libjpeg-turbo-3.2.0-hb03c661_1 
  liblapack          conda-forge/linux-64::liblapack-3.11.0-11_h47877c9_openblas 
  liblzma            conda-forge/linux-64::liblzma-5.8.3-hb03c661_1 
  libmpdec           conda-forge/linux-64::libmpdec-4.0.0-hb03c661_2 
  libnetcdf          conda-forge/linux-64::libnetcdf-4.10.1-nompi_h3fa17b5_201 
  libnghttp2         conda-forge/linux-64::libnghttp2-1.68.1-h74cf4be_1 
  libopenblas        conda-forge/linux-64::libopenblas-0.3.34-pthreads_hf13c14d_2 
  libopentelemetry-~ conda-forge/linux-64::libopentelemetry-cpp-1.27.0-h9692893_0 
  libopentelemetry-~ conda-forge/linux-64::libopentelemetry-cpp-headers-1.27.0-ha770c72_0 
  libparquet         conda-forge/linux-64::libparquet-24.0.0-h7376487_9_cpu 
  libpng             conda-forge/linux-64::libpng-1.6.58-h922cc85_1 
  libprotobuf        conda-forge/linux-64::libprotobuf-6.33.5-h538a264_2 
  libpsl             conda-forge/linux-64::libpsl-0.23.1-hd9e3e90_1 
  libpython          conda-forge/linux-64::libpython-3.14.7-hdc7f604_106_cp314 
  libraqm            conda-forge/linux-64::libraqm-0.11.0-h6406941_0 
  libre2-11          conda-forge/linux-64::libre2-11-2025.11.05-h0dc7533_1 
  libsqlite          conda-forge/linux-64::libsqlite-3.53.4-h13e7031_1 
  libssh2            conda-forge/linux-64::libssh2-1.11.1-h6154650_1 
  libstdcxx          conda-forge/linux-64::libstdcxx-16.2.0-h934c35e_5 
  libstdcxx-ng       conda-forge/linux-64::libstdcxx-ng-16.2.0-hdf11a46_5 
  libthrift          conda-forge/linux-64::libthrift-0.22.0-h7d032f7_2 
  libtiff            conda-forge/linux-64::libtiff-4.7.2-hcc2c06a_1 
  libutf8proc        conda-forge/linux-64::libutf8proc-2.11.3-hfe17d71_0 
  libuuid            conda-forge/linux-64::libuuid-2.42.3-hcfc3c73_0 
  libwebp-base       conda-forge/linux-64::libwebp-base-1.6.0-hd42ef1d_1 
  libxcb             conda-forge/linux-64::libxcb-1.17.0-hb83e432_2 
  libxml2            conda-forge/linux-64::libxml2-2.15.4-h7df9aa5_0 
  libxml2-16         conda-forge/linux-64::libxml2-16-2.15.4-hf3af7cc_0 
  libzip             conda-forge/linux-64::libzip-1.11.2-h6008cf6_1 
  libzlib            conda-forge/linux-64::libzlib-1.3.2-h25fd6f3_3 
  llvmlite           conda-forge/linux-64::llvmlite-0.46.0-py314h946fb2a_0 
  lz4-c              conda-forge/linux-64::lz4-c-1.10.0-hee9eb32_2 
  markupsafe         conda-forge/linux-64::markupsafe-3.0.3-py314h67df5f8_1 
  matplotlib-base    conda-forge/linux-64::matplotlib-base-3.11.2-py314h9124352_0 
  mda-xdrlib         conda-forge/noarch::mda-xdrlib-0.2.0-pyhd8ed1ab_1 
  mdanalysis         conda-forge/linux-64::mdanalysis-2.10.0-py314ha0b5721_1 
  mmtf-python        conda-forge/noarch::mmtf-python-1.1.3-pyhd8ed1ab_0 
  mrcfile            conda-forge/noarch::mrcfile-1.5.4-pyhd8ed1ab_0 
  msgpack-python     conda-forge/linux-64::msgpack-python-1.2.2-py314h5383ef5_2 
  munkres            conda-forge/noarch::munkres-1.1.4-pyhd8ed1ab_1 
  narwhals           conda-forge/noarch::narwhals-2.26.0-pyh5ded981_0 
  ncurses            conda-forge/linux-64::ncurses-6.6-hdb14827_1 
  netcdf4            conda-forge/linux-64::netcdf4-1.7.4-nompi_py311hc841c2f_109 
  networkx           conda-forge/noarch::networkx-3.6.1-pyhcf101f3_0 
  nlohmann_json      conda-forge/linux-64::nlohmann_json-3.12.0-h54a6638_2 
  numba              conda-forge/linux-64::numba-0.63.1-py314h8169c2f_0 
  numpy              conda-forge/linux-64::numpy-2.3.5-py314h2b28147_1 
  openjpeg           conda-forge/linux-64::openjpeg-2.5.4-heb1ab33_2 
  openssl            conda-forge/linux-64::openssl-3.6.4-h781a0a9_0 
  orc                conda-forge/linux-64::orc-2.3.0-h21090e2_0 
  packaging          conda-forge/noarch::packaging-26.3-pyhc364b38_0 
  pandas             conda-forge/linux-64::pandas-2.3.3-py314ha0b5721_2 
  patsy              conda-forge/noarch::patsy-1.0.3-pyhcf101f3_0 
  pcre2              conda-forge/linux-64::pcre2-10.47-h8b3dc9c_1 
  pillow             conda-forge/linux-64::pillow-12.3.0-py314h50bfbbb_4 
  pip                conda-forge/noarch::pip-26.2.1-pyh145f28c_0 
  pixman             conda-forge/linux-64::pixman-0.46.4-h54a6638_3 
  plotly             conda-forge/noarch::plotly-6.5.0-pyhd8ed1ab_0 
  prometheus-cpp     conda-forge/linux-64::prometheus-cpp-1.3.0-h26ae035_1 
  protobuf           conda-forge/linux-64::protobuf-6.33.5-py314h61e7c5f_2 
  pthread-stubs      conda-forge/linux-64::pthread-stubs-0.4-h7cc23a3_1004 
  pyarrow            conda-forge/linux-64::pyarrow-24.0.0-py314hdafbbf9_0 
  pyarrow-core       conda-forge/linux-64::pyarrow-core-24.0.0-py314h969be7f_0_cpu 
  pydeck             conda-forge/noarch::pydeck-0.9.3-pyhd8ed1ab_0 
  pyedr              conda-forge/noarch::pyedr-0.8.0-pyhd8ed1ab_1 
  pyparsing          conda-forge/noarch::pyparsing-3.3.2-pyhcf101f3_0 
  pysocks            conda-forge/noarch::pysocks-1.7.1-pyha55dd90_7 
  python             conda-forge/linux-64::python-3.14.7-hcd007b5_106_cp314 
  python-dateutil    conda-forge/noarch::python-dateutil-2.9.0.post0-pyhe01879c_2 
  python-gil         conda-forge/noarch::python-gil-3.14.7-h4df99d1_106 
  python-tzdata      conda-forge/noarch::python-tzdata-2026.3-pyhd8ed1ab_0 
  python_abi         conda-forge/noarch::python_abi-3.14-9_cp314 
  pytng              conda-forge/linux-64::pytng-0.3.4-py314hddf221e_0 
  pytz               conda-forge/noarch::pytz-2026.3.post1-pyhcf101f3_0 
  pyyaml             conda-forge/linux-64::pyyaml-6.0.3-py314h67df5f8_1 
  qhull              conda-forge/linux-64::qhull-2020.2-h434a139_5 
  re2                conda-forge/linux-64::re2-2025.11.05-h5301d42_1 
  readline           conda-forge/linux-64::readline-8.3-hd6e31c0_1 
  referencing        conda-forge/noarch::referencing-0.37.0-pyhcf101f3_0 
  requests           conda-forge/noarch::requests-2.34.2-pyhcf101f3_0 
  rpds-py            conda-forge/linux-64::rpds-py-2026.6.3-py314h7e8cd81_2 
  s2n                conda-forge/linux-64::s2n-1.7.5-h7e3ee7f_1 
  scikit-learn       conda-forge/linux-64::scikit-learn-1.9.1-np2py314h9e1d7c2_0 
  scipy              conda-forge/linux-64::scipy-1.16.3-py314hf07bd8e_2 
  seaborn            conda-forge/noarch::seaborn-0.13.2-hd8ed1ab_3 
  seaborn-base       conda-forge/noarch::seaborn-base-0.13.2-pyhd8ed1ab_3 
  six                conda-forge/noarch::six-1.17.0-pyhe01879c_1 
  smmap              conda-forge/noarch::smmap-5.0.3-pyhcf101f3_1 
  snappy             conda-forge/linux-64::snappy-1.2.2-h03e3b7b_1 
  statsmodels        conda-forge/linux-64::statsmodels-0.15.0-np2py314h8874201_1 
  streamlit          conda-forge/noarch::streamlit-1.52.2-pyhd8ed1ab_0 
  tenacity           conda-forge/noarch::tenacity-9.1.4-pyhcf101f3_0 
  threadpoolctl      conda-forge/noarch::threadpoolctl-3.7.0-pyhc455866_0 
  tidynamics         conda-forge/noarch::tidynamics-1.1.2-pyhd8ed1ab_0 
  tk                 conda-forge/linux-64::tk-8.6.13-noxft_h1df4ec4_4 
  toml               conda-forge/noarch::toml-0.10.2-pyhcf101f3_3 
  tornado            conda-forge/linux-64::tornado-6.5.8-py314h89acca1_2 
  tqdm               conda-forge/noarch::tqdm-4.70.1-pyhfa0c392_0 
  typing-extensions  conda-forge/noarch::typing-extensions-4.16.0-h69aa097_0 
  typing_extensions  conda-forge/noarch::typing_extensions-4.16.0-pyhcf101f3_0 
  tzdata             conda-forge/noarch::tzdata-2026c-h151e31d_0 
  urllib3            conda-forge/noarch::urllib3-2.8.0-pyhd8ed1ab_0 
  watchdog           conda-forge/linux-64::watchdog-6.0.0-py314h9e666f3_4 
  wrapt              conda-forge/linux-64::wrapt-2.4.0-py314hfe1a184_2 
  xorg-libice        conda-forge/linux-64::xorg-libice-1.1.2-h280c20c_0 
  xorg-libsm         conda-forge/linux-64::xorg-libsm-1.2.6-h0d788c3_1 
  xorg-libx11        conda-forge/linux-64::xorg-libx11-1.8.13-he1eb515_1 
  xorg-libxau        conda-forge/linux-64::xorg-libxau-1.0.12-h7cc23a3_2 
  xorg-libxdmcp      conda-forge/linux-64::xorg-libxdmcp-1.1.5-hb03c661_2 
  xorg-libxext       conda-forge/linux-64::xorg-libxext-1.3.7-h7cc23a3_1 
  xorg-libxrender    conda-forge/linux-64::xorg-libxrender-0.9.12-hb03c661_1 
  yaml               conda-forge/linux-64::yaml-0.2.5-hebe6cf0_3 
  zipp               conda-forge/noarch::zipp-4.1.0-pyhcf101f3_0 
  zlib               conda-forge/linux-64::zlib-1.3.2-h25fd6f3_3 
  zlib-ng            conda-forge/linux-64::zlib-ng-2.3.3-hce19668_1 
  zstd               conda-forge/linux-64::zstd-1.5.7-hb78ec9c_7 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                                           
Preparing transaction: done                                                                                                                                                                
Verifying transaction: done                                                                                                                                                                
Executing transaction: done                                                                                                                                                                
#                                                                                                                                                                                          
# To activate this environment, use                                                                                                                                                        
#                                                                                                                                                                                          
#     $ conda activate qtwin                                                                                                                                                               
#                                                                                                                                                                                          
# To deactivate an active environment, use                                                                                                                                                 
#                                                                                                                                                                                          
#     $ conda deactivate      
```

</details>

To launch the GUI of the software locally, 
```bash
conda activate qtwin
(qtwin) streamlit run app.py
```

For a tutorial on loading trajectories, performing analyses, and running the analysis from the command line, see the [Usage Procedure & Examples](../workflow) section.

## Install-Free Cloud Usage
A cloud-based GUI without installation is available at [https://q-twin.streamlit.app/](https://q-twin.streamlit.app/). 
