import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mity",
    version="0.0.1",
    description="A sensitive Mitochondrial variant detection pipeline from WGS data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KCCG/mity",
    author="Clare Puttick",
    author_email="clare.puttick@gmail.com",
    license="see LICENSE.txt",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Bioinformaticians',
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='mitochondrial DNA genomics variant SNV INDEL',
    project_urls={
        'Documentation': 'https://github.com/KCCG/mity',
        'KCCG': 'http://garvan.org.au/kccg',
        'Mark Cowley, CCI': 'https://ccia.org.au/home/our-purpose/our-people/a-prof-mark-cowley/'
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'vcf',
        'pandas'
    ],
    python_requires='>=3',
    data_files=[
        ('anticodon_positions.csv', ['annot/anticodon_positions.csv']),
        ('b37d5.genome', ['annot/b37d5.genome']),
        ('gtf_annotations.csv', ['annot/gtf_annotations.csv']),
        ('haplotype_data.csv', ['annot/haplotype_data.csv']),
        ('mgrb_variants.csv', ['annot/mgrb_variants.csv']),
        ('mito_dna_func_loc.csv', ['annot/mito_dna_func_loc.csv']),
        ('mitomap_panel_annotations.csv', ['annot/mitomap_panel_annotations.csv']),
        ('mitotip_score_fixed_del.csv', ['annot/mitotip_score_fixed_del.csv'])
    ]
)