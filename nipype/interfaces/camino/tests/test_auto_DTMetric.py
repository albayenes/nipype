# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dti import DTMetric


def test_DTMetric_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    data_header=dict(argstr='-header %s',
    ),
    eigen_data=dict(argstr='-inputfile %s',
    mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputdatatype=dict(argstr='-inputdatatype %s',
    usedefault=True,
    ),
    metric=dict(argstr='-stat %s',
    mandatory=True,
    ),
    outputdatatype=dict(argstr='-outputdatatype %s',
    usedefault=True,
    ),
    outputfile=dict(argstr='-outputfile %s',
    genfile=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = DTMetric.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DTMetric_outputs():
    output_map = dict(metric_stats=dict(),
    )
    outputs = DTMetric.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
