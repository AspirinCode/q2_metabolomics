from qiime2.plugin import Plugin
import qiime2.plugin
from q2_types.feature_table import FeatureTable, Frequency
import q2_metabolomics

plugin = Plugin(
    name='metabolomics',
    version=q2_metabolomics.__version__,
    website='https://gnps.ucsd.edu',
    user_support_text='https://gnps.ucsd.edu',
    description='Plugin for the creation of a biom feature table for metabolomics data.',
    short_description='Plugin for the creation of a biom feature table for metabolomics data.',
    package='q2_metabolomics'
)

plugin.methods.register_function(
    function=q2_metabolomics.gnps_clustering,
    inputs={},
    parameters={'manifest': qiime2.plugin.Str, 'credentials': qiime2.plugin.Str},
    input_descriptions={},
    outputs=[('feature_table', FeatureTable[Frequency])],
    parameter_descriptions={
        'manifest': 'Manifest file for describing information about each file. Headers of sample-id and filepath',
        'credentials': 'GNPS login credentials json'
    },
    output_descriptions={'feature_table': 'Resulting feature table'},
    name='GNPS Metabolomics MS/MS Spectral Counts',
    description=("Computes feature BioM for metabolomics using GNPS Molecular Networking"),
    citations=[]
)

plugin.methods.register_function(
    function=q2_metabolomics.gnps_clustering_taskimport,
    inputs={},
    parameters={'manifest': qiime2.plugin.Str, 'taskid': qiime2.plugin.Str},
    input_descriptions={},
    outputs=[('feature_table', FeatureTable[Frequency])],
    parameter_descriptions={
        'manifest': 'Manifest file for describing information about each file. Headers of sample-id and filepath',
        'taskid': 'GNPS Task ID'
    },
    output_descriptions={'feature_table': 'Resulting feature table'},
    name='GNPS Metabolomics MS/MS Spectral Counts - Import Existing GNPS Task',
    description=("Computes feature BioM for metabolomics by importing GNPS Molecular Networking Task"),
    citations=[]
)


plugin.methods.register_function(
    function=q2_metabolomics.mzmine2_clustering,
    inputs={},
    parameters={'manifest': qiime2.plugin.Str, 'quantificationtable': qiime2.plugin.Str},
    input_descriptions={},
    outputs=[('feature_table', FeatureTable[Frequency])],
    parameter_descriptions={
        'manifest': 'Manifest file for describing information about each file. Headers of sample-id and filepath',
        'quantificationtable': 'Quantification Table output from MZMine2'
    },
    output_descriptions={'feature_table': 'Resulting feature table'},
    name='Metabolomics MZMine2 Quantitification',
    description=("Computes feature biom for metabolomics using MZMine2 quantification output."),
    citations=[]
)