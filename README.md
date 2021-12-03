# hse21_hw3

Ссылка на 1 часть: [https://colab.research.google.com/drive/19O6sdnHVjBC3Na8NeyeZcbh2u3kbPYWp?usp=sharing](https://colab.research.google.com/drive/19O6sdnHVjBC3Na8NeyeZcbh2u3kbPYWp?usp=sharing)

Ссылка на часть с R: [https://colab.research.google.com/drive/10X7_12S413H2nZDPFoVMVzVTeMGlzM3Q?usp=sharing](https://colab.research.google.com/drive/10X7_12S413H2nZDPFoVMVzVTeMGlzM3Q?usp=sharing)

Я заметил, что я перепутал колонки в ALL.counts, поэтому я написал скрипт на питоне который все правит (`main.py` в папке `data/`).

Отчет fastq лежит в `multiqc_report.html`.

![1](./resources/multiqc_1.png)

![1](./resources/multiqc_2.png)

![1](./resources/multiqc_3.png)

HISAT:

![hs](./resources/hisat.png)

Уникальные чтения:

![u](./resources/unique.png)

HTSEQ:

![ht](./resources/h2s.png)

Общее число чтений:
```
SRR3414629_1: 16049609
SRR3414630_1: 11465320
SRR3414631_1: 18408844
SRR3414635_1: 16275994
SRR3414636_1: 15757574
SRR3414637_1: 15736976
```

Графики DESEq2

![1](resources/plot_1.png)

![1](resources/plot_2.png)

![1](resources/plot_3.png)

Графики для генов которые наиболее значимо поменяли свою экспрессию (55402, 55403, 5409, 265).

![1](./resources/graph_1.png)

![2](./resources/graph_2.png)

![3](./resources/graph_3.png)

![4](./resources/graph_4.png)