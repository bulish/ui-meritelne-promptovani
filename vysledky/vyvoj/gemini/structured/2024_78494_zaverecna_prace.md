### 1. Summary

#### Goal

This study aims to examine and compare income inequality across all 27 European Union (EU) member states from 2007 to 2023. It evaluates how different established metrics capture variations in income distribution and highlights regional disparities over time.

#### Methods

The research utilizes disposable income share data by deciles from Eurostat (2024), supplemented by the Croatian Bureau of Statistics for Croatia prior to 2010. It applies three prominent inequality measures: the **Gini coefficient** (alongside the Lorenz curve), the **Atkinson Index** (with inequality aversion parameters $\epsilon = 0.5, 1.0, 2.0$), and **Generalized Entropy (GE) indices** (with sensitivity parameters $\alpha = 0.0, 1.0, 2.0$). Computations were performed using R's "ineq" library.

#### Main Results

Income inequality trends varied widely across the EU. Romania experienced the largest Gini reduction, dropping from $0.375$ in 2007 to $0.305$ in 2023, driven by income gains in lower deciles and losses in the top decile. Poland also saw its Gini fall from $0.315$ to $0.265$. Conversely, Sweden and Malta saw significant increases in inequality, with Gini values rising by approximately $+0.06$ and GE($2.0$) surging by $65.7\%$ and $76.5\%$ respectively, led by top-income concentration. Countries like Slovakia and Czechia consistently maintained low inequality levels.

#### Conclusions

While the aggregate EU average inequality remained relatively stable, this masked divergent national trajectories. Relying solely on the Gini coefficient obscures important distributional nuances. Utilizing complementary measures like the Atkinson and GE indices reveals specific concentrations of inequality at the lower or upper ends of the income spectrum, emphasizing the need for tailored, multi-dimensional policy approaches.

---

### 2. Supporting Source Passages

* **Goal:** "The primary goal of this study is to compare income inequality in the selected countries using various established measures. By applying multiple metrics, the research also aims to explore how these measures catch variations in income distribution and highlight regional differences within and across countries over time."


* **Methods:** "This thesis applies these three inequality measures - Gini, Atkinson and Generalized Entropy - to analyze income inequality across all current 27 member states between 2007 and 2023 years."


* **Methods:** "The raw data utilized in the analysis comes from Eurostat (2024), the dataset titled 'Distribution of income by quantiles'."


* **Main Results:** "Romania, for example, saw the largest reduction in inequality. Its Gini coefficient decreased sharply from 0.375 in 2007... to 0.305 in 2023..."


* **Main Results:** "Sweden, for example, was one of the most equal countries and in 2007 alone it was ranked 2nd. Its Gini was 0.229 in 2007 and by 2023 it increased to 0.286..."


* **Conclusions:** "While the average inequality levels have remained relatively stable in the region, this hides significant variations among member states."


* **Conclusions:** "This research has also illustrated the importance of employing multiple measures to fully capture the subtleties of inequality. Many studies rely solely on the Gini coefficient, overlooking the deeper insights offered by the Atkinson and Generalized Entropy indices."