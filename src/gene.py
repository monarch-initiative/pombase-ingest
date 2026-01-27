import koza
from biolink_model.datamodel.pydanticmodel_v2 import Gene


@koza.transform_record()
def transform_record(koza_transform, row):
    in_taxon = "NCBITaxon:4896"
    in_taxon_label = "Schizosaccharomyces pombe"

    gene = Gene(
        id=row["gene_systematic_id_with_prefix"],
        symbol=row["gene_name"] or row["gene_systematic_id"],
        name=row["gene_name"] or row["gene_systematic_id"],
        full_name=row["gene_name"] or row["gene_systematic_id"],
        in_taxon=[in_taxon],
        in_taxon_label=in_taxon_label,
        provided_by=["infores:pombase"],
    )

    if row["external_id"]:
        gene.xref = ["UniProtKB:" + row["external_id"]]

    if row["synonyms"]:
        gene.synonym = row["synonyms"].split(",")

    return [gene]
