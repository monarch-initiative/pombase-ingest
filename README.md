# pombase-ingest

PomBase is a comprehensive database for the fission yeast _Schizosaccharomyces pombe_, providing structural and functional annotation, literature curation and access to large-scale data sets. This ingest transforms gene to phenotypic feature associations; gene entities aren't yet loaded as a part of this ingest, and FYPO ontology terms are brought in directly from the ontology without transformation.

- [PomBase Bulk Downloads](https://www.pombase.org/datasets)
- [PHAF Format Description](https://www.pombase.org/downloads/phenotype-annotations)
- [PHAF Format LinkML](https://biodatamodels.github.io/ontology-associations/PombasePhafAssociation/)

## Gene Information

PomBase genes are captured directly from the PomBase [names and identifiers](https://www.pombase.org/downloads/names-and-identifiers) set, with synonyms being populated as available and UniProtKB accessions captured as xrefs if available.

**Biolink Captured:**

- `biolink:Gene`
    - id
    - symbol
    - xref (UniProtKB curie if provided)
    - synonym
    - provided_by (`["infores:pombase"]`)

## Gene to Phenotype

The [PHAF](https://www.pombase.org/downloads/phenotype-annotations) download file is extremely well documented. Alleles are provided but not captured, with the assumption that even with an allele specified the gene to phenotype is accurate with a some-some interpretation. Genotype/strain information looks uniform throughout the file and is not captured. It might be sensible to make presence of genotype information an error condition to be sure that we only get 'clean' gene to phenotype associations.

Penetrance and Severity columns are available but not captured as a part of this ingest. Penetrance values can be either FYPO_EXT terms (FYPO_EXT:0000001, FYPO_EXT:0000002, FYPO_EXT:0000003, FYPO_EXT:0000004), int/float numbers (percentages), or strings (">98", "~10", "10-20"). Severity is represented using one or more FYPO_EXT terms.

**Biolink Captured:**

- `biolink:Gene`
    - id

- `biolink:PhenotypicFeature`
    - id

- `biolink:GeneToPhenotypicFeatureAssociation`
    - id (random uuid)
    - subject (gene.id)
    - predicate (`biolink:has_phenotype`)
    - object (phenotypicFeature.id)
    - publications
    - qualifiers (optionally included from condition row)
    - aggregating_knowledge_source (`["infores:monarchinitiative"]`)
    - primary_knowledge_source (`infores:pombase`)

## Setup

```bash
just setup
```

## Usage

### Download source data

```bash
just download
```

### Run transforms

```bash
# Run all transforms
just transform-all

# Run specific transform
just transform <transform_name>
```

### Run tests

```bash
just test
```

## Adding New Ingests

Use the `create-koza-ingest` Claude skill to add new ingests to this repository.

## Citation

Harris MA, Rutherford KM, Hayles J, Lock A, Bähler J, Oliver S, Mata J, Wood V. Fission stories: Using PomBase to understand Schizosaccharomyces pombe biology. Genetics, 2021; iyab222.

## License

BSD-3-Clause
