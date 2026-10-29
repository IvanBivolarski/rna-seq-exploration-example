# Exploratory RNA-seq heterogeneity analysis with sensitivity analysis

## Introduction

RNA sequencing enables the characterization of gene expression across thousands of genes within a tissue sample [1]. In exploratory studies, principal component analysis (PCA) [2], sample correlation analysis [8], and hierarchical clustering [7] are commonly used to summarize expression patterns and examine similarities between specimens. These approaches can help identify transcriptomic heterogeneity and guide subsequent analyses [1,7].

Interpreting these patterns can be challenging when only a small number of samples are available [3]. A sample with a divergent expression profile may influence the principal components and the apparent relationships among the remaining specimens [2,3]. Such divergence may reflect biological variation, differences in tissue composition, RNA degradation, library preparation, or other technical factors [4,5]. An unusual position in a PCA plot alone does not establish the underlying cause or justify excluding a sample [2,4].

Sensitivity analysis provides a practical way to examine the influence of an individual sample. Repeating an analysis after omitting a divergent specimen allows investigators to assess which descriptive patterns persist and which depend on its inclusion [6]. However, the resulting plots require careful comparison because removing a sample also changes the dataset used to calculate principal components and clustering relationships [2,7]. Sample omission should therefore be documented as an analytical comparison rather than interpreted as confirmation that the omitted specimen is invalid [6].

Reproducibility is particularly useful in this setting [6]. Explicit reporting of input data, filtering criteria, transformations, software versions, and analysis parameters allows others to inspect the workflow and repeat its steps [1,6]. A compact script that generates both the initial analysis and the corresponding sensitivity analysis can make these comparisons easier to document and review [6].

The aim of this project is to develop a lightweight Python workflow for exploring transcriptomic heterogeneity and the influence of a divergent sample in a small RNA sequencing dataset [1,3]. The workflow will be demonstrated using gene expression data from seven treatment-naïve prostate cancer specimens. It will combine PCA [2], pairwise sample correlations [8], and hierarchical clustering [7], followed by a sensitivity analysis omitting the previously identified divergent sample, PC_345813A. The intended contribution is a transparent, reproducible example of how sample influence can be examined before biological interpretations are assigned [6].

## Materials and Methods

### Study design and dataset

This exploratory methodological study will use gene-level RNA sequencing expression data from seven treatment-naïve prostate cancer tissue specimens [1]. Its purpose is to describe inter-sample transcriptomic heterogeneity and to examine how one previously identified divergent sample, PC_345813A, influences exploratory visualizations [2]. Clinical outcome prediction and differential expression testing will not be performed.

### Input data and preprocessing

The input will be a comma-separated expression matrix containing genes in rows and samples in columns, with unique identifiers for both. The expression units and normalization procedure will be confirmed from the sequencing provider's documentation before analysis [1].

The initial workflow will accept normalized, nonnegative expression values that have not undergone logarithmic transformation [1]. Raw read counts will require a separate normalization step before use [1]. Missing, nonnumeric, negative, or infinite values will trigger an error rather than automatic imputation.

Expression values will be transformed using log2(x + 1) [1]. Genes with zero variance in either the complete dataset or the dataset excluding PC_345813A will be removed, and the same retained gene set will be used in both analyses [2]. Genes will be centered for PCA without scaling each gene to unit variance [2].

### Exploratory analysis

Principal component analysis will summarize sample relationships using the first two principal components, and the proportion of variance explained by each component will be reported [2]. Pairwise Pearson correlations will be calculated between sample profiles using the transformed expression values [8]. Hierarchical clustering will use Euclidean distances and average linkage [7]. Outputs will include PCA plots, correlation heatmaps, dendrograms, and numerical tables.

### Sensitivity analysis

The analysis will first include all seven specimens and will then be repeated after omitting PC_345813A [2]. This sample was identified as divergent in the preceding descriptive analysis; its omission will therefore constitute a targeted sensitivity analysis rather than an independent one [6].

## Discussion

This project was designed as a small, transparent example of how exploratory RNA sequencing analyses can be examined before biological interpretations are assigned. Rather than testing hypotheses about prostate cancer biology, the workflow focuses on describing inter-sample transcriptomic heterogeneity and on documenting how a single divergent specimen, PC_345813A, influences the visual summaries that are commonly used in exploratory work [1,2].

The combination of PCA, pairwise correlations, and hierarchical clustering provides complementary views of sample relationships [2,7,8]. PCA summarizes the dominant axes of variation, correlations quantify the similarity of expression profiles, and hierarchical clustering places samples within a nested structure based on Euclidean distances. Because these methods emphasize different aspects of the same data, agreement across them can be more informative than any single plot, while disagreement may indicate that the apparent structure is sensitive to the method chosen [2,7].

A central methodological point is that an unusual position in a PCA plot does not, by itself, identify the cause of divergence or justify excluding a sample [2,3]. Divergence may reflect biological variation, differences in tissue composition, RNA degradation, library preparation, or other technical factors [4,5]. For this reason, the omission of PC_345813A is treated here as a targeted sensitivity analysis rather than as a correction of the dataset [6]. Repeating the analysis with and without this sample allows the reader to see which descriptive patterns persist and which depend on its inclusion [2,6].

Several limitations should be acknowledged. The dataset contains only seven specimens, which limits the stability of PCA, correlation estimates, and clustering solutions [3]. The workflow does not include differential expression testing, batch correction, or biological validation, and the expression units and normalization procedure are taken from the provider's documentation rather than re-derived [1,4]. If differential expression were to be added in future work, established frameworks such as edgeR would provide a natural starting point, although multiple-testing correction would also need to be addressed [9,10]. Consequently, the results should be read as a description of this small dataset and as a demonstration of the workflow, not as evidence about prostate cancer more broadly.

The reproducibility-oriented design is also part of the contribution. Explicit reporting of input data, filtering criteria, transformations, software versions, and analysis parameters allows others to inspect and repeat the steps [6]. A compact script that generates both the initial and the sensitivity analysis makes the comparison easier to document and review, and it illustrates how sample influence can be examined in a transparent way before biological interpretations are assigned [1,6]. Where possible, implementation in a widely used environment such as R and visualization with established plotting libraries can further support inspection and reuse [11,12].

Future work could extend this framework in several directions: incorporating additional samples to stabilize the exploratory structure, adding batch information where available, and complementing descriptive analyses with formal differential expression or pathway-level methods once the dataset and design justify them [1,3,4]. Within its intended scope, however, the present workflow offers a simple and reproducible example of how the influence of an individual sample can be examined and reported.

## Limitations

Several limitations should be considered when interpreting this work. The dataset contains only seven specimens, which limits the stability of PCA, correlation estimates, and clustering solutions [3]. With such a small number of samples, the apparent structure of the data can change substantially when a single specimen is added or removed, and the sensitivity analysis presented here should therefore be read as a description of this particular dataset rather than as a general assessment of sample influence [2,6].

The workflow is descriptive and does not include differential expression testing, batch correction, or biological validation [1,4]. The expression units and normalization procedure are taken from the sequencing provider's documentation rather than re-derived, and no independent quality control of the raw reads is performed within the workflow [1,5]. As a result, technical variation cannot be separated from biological variation in the present analysis [4].

The omission of PC_345813A is a targeted sensitivity analysis, not a correction of the dataset [6]. The sample was identified as divergent in the preceding descriptive analysis, and its removal changes the dataset used to calculate principal components and clustering relationships; the resulting plots therefore require careful comparison rather than direct interpretation as confirmation that the sample is invalid [2,7].

Finally, the workflow is implemented in Python and is intended as a lightweight, reproducible example rather than a comprehensive analytical pipeline [6]. It does not cover pathway-level analysis, formal statistical testing, or integration with clinical data, and its outputs should be regarded as exploratory summaries that guide, rather than replace, subsequent analyses [1,3]. Within these limits, the present work offers a transparent example of how sample influence can be examined and reported before biological interpretations are assigned.

## Conclusions

This project presents a lightweight, reproducible Python workflow for exploring transcriptomic heterogeneity in a small RNA sequencing dataset and for examining the influence of a single divergent specimen [1,6]. Using gene-level expression data from seven treatment-naïve prostate cancer specimens, the workflow combines PCA, pairwise Pearson correlations, and hierarchical clustering, and then repeats the analysis after omitting the previously identified divergent sample, PC_345813A [2,7,8].

The main contribution is methodological rather than biological. The workflow shows how descriptive patterns can be summarized across complementary exploratory methods, and how a targeted sensitivity analysis can be used to assess which patterns persist and which depend on the inclusion of a single sample [2,6]. It also illustrates that an unusual position in a PCA plot does not by itself establish the cause of divergence or justify excluding a sample, and that sample omission should be documented as an analytical comparison rather than as a correction of the dataset [2,3,4].

The workflow is intentionally limited in scope. It does not perform differential expression testing, batch correction, or biological validation, and its results should be read as exploratory summaries of this small dataset rather than as evidence about prostate cancer more broadly [1,3,4]. Within these limits, the project offers a transparent and reproducible example of how sample influence can be examined and reported before biological interpretations are assigned [6].

## References

1. Conesa A, Madrigal P, Tarazona S, et al. A survey of best practices for RNA-seq data analysis. *Genome Biol.* 2016;17:13. doi: 10.1186/s13059-016-0881-8.
2. Jolliffe IT, Cadima J. Principal component analysis: a review and recent developments. *Philos Trans A Math Phys Eng Sci.* 2016;374(2065):20150202. doi: 10.1098/rsta.2015.0202.
3. Love MI, Huber W, Anders S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biol.* 2014;15:550. doi: 10.1186/s13059-014-0550-8.
4. Leek JT, Scharpf RB, Corrada Bravo H, et al. Tackling the widespread and critical impact of batch effects in high-throughput data. *Nat Rev Genet.* 2010;11(10):733–739. doi: 10.1038/nrg2825.
5. Wang L, Wang S, Li W. RSeQC: quality control of RNA-seq experiments. *Bioinformatics.* 2012;28(16):2184–2185. doi: 10.1093/bioinformatics/bts356.
6. Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten simple rules for reproducible computational research. *PLoS Comput Biol.* 2013;9(10):e1003285. doi: 10.1371/journal.pcbi.1003285.
7. Murtagh F, Contreras P. Algorithms for hierarchical clustering: an overview. *Wiley Interdiscip Rev Data Min Knowl Discov.* 2012;2(1):86–97. doi: 10.1002/widm.53.
8. Ballouz S, Verleyen W, Gillis J. Guidance for RNA-seq co-expression network construction and analysis: safety in numbers. *Bioinformatics.* 2015;31(13):2123–2130. doi: 10.1093/bioinformatics/btv118.
9. Robinson MD, McCarthy DJ, Smyth GK. edgeR: a Bioconductor package for differential expression analysis of digital gene expression data. *Bioinformatics.* 2010;26(1):139–140. doi: 10.1093/bioinformatics/btp616.
10. Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. *J R Stat Soc Series B Methodol.* 1995;57(1):289–300. doi: 10.1111/j.2517-6161.1995.tb02031.x.
11. R Core Team. *R: A Language and Environment for Statistical Computing*. Vienna, Austria: R Foundation for Statistical Computing; 2015.
12. Wickham H. *ggplot2: Elegant Graphics for Data Analysis*. New York: Springer-Verlag; 2016.