# CohortX Train Gold Minimal Nodes

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Source: `data/Task_3.xlsx` / sheet `Train`.
- Use: calibrate ICD node granularity before spending Kaggle submissions.
- Empty lists mean the gold cell is `Not Applicable`.

## Node Summary

| Condition | Bucket | Nodes | Expanded Codes | Cell F1 |
|---|---|---|---:|---:|
| URTI | KEEP | `B974`, `J00`, `J01`, `J02`, `J03`, `J04`, `J05`, `J06`, `J09`, `J10`, `J11`, `J30`, `J31`, `J32`, `J33`, `J34`, `J35`, `J36`, `J37`, `J38`, `J39` | 152 | 1.000 |
| URTI | ASSOCIATION | `H65`, `H66` | 101 | 1.000 |
| URTI | DIFF | `J12`, `J13`, `J14`, `J15`, `J16`, `J17`, `J18`, `J20`, `J21`, `J22`, `J40` | 56 | 1.000 |
| Aortic Aneurysm | KEEP | `I71`, `I790` | 41 | 1.000 |
| Aortic Aneurysm | ASSOCIATION | `A50`, `A539`, `M352` | 40 | 1.000 |
| Aortic Aneurysm | DIFF | `I21`, `I63` | 134 | 1.000 |
| Ischemic Heart Disease | KEEP | `I20`, `I21`, `I22`, `I23`, `I24`, `I25` | 113 | 1.000 |
| Ischemic Heart Disease | ASSOCIATION | `Not Applicable` | 0 | 1.000 |
| Ischemic Heart Disease | DIFF | `Not Applicable` | 0 | 1.000 |
| Stroke | KEEP | `G45`, `G46`, `I60`, `I61`, `I62`, `I63`, `I65`, `I66`, `I67`, `I68`, `I69` | 526 | 1.000 |
| Stroke | ASSOCIATION | `H340`, `H341` | 10 | 1.000 |
| Stroke | DIFF | `Not Applicable` | 0 | 1.000 |
| Shortness of Breadth | KEEP | `I26`, `I27`, `I28`, `I50`, `J12`, `J13`, `J14`, `J15`, `J16`, `J17`, `J18`, `J20`, `J21`, `J22`, `J41`, `J42`, `J43`, `J44`, `J80`, `J951`, `J952`, `J96`, `R05`, `R06`, `R093` | 179 | 1.000 |
| Shortness of Breadth | ASSOCIATION | `Not Applicable` | 0 | 1.000 |
| Shortness of Breadth | DIFF | `R53`, `T17`, `T180` | 243 | 1.000 |

## JSON Spec

```json
{
  "URTI": {
    "KEEP": [
      "B974",
      "J00",
      "J01",
      "J02",
      "J03",
      "J04",
      "J05",
      "J06",
      "J09",
      "J10",
      "J11",
      "J30",
      "J31",
      "J32",
      "J33",
      "J34",
      "J35",
      "J36",
      "J37",
      "J38",
      "J39"
    ],
    "ASSOCIATION": [
      "H65",
      "H66"
    ],
    "DIFF": [
      "J12",
      "J13",
      "J14",
      "J15",
      "J16",
      "J17",
      "J18",
      "J20",
      "J21",
      "J22",
      "J40"
    ]
  },
  "Aortic Aneurysm": {
    "KEEP": [
      "I71",
      "I790"
    ],
    "ASSOCIATION": [
      "A50",
      "A539",
      "M352"
    ],
    "DIFF": [
      "I21",
      "I63"
    ]
  },
  "Ischemic Heart Disease": {
    "KEEP": [
      "I20",
      "I21",
      "I22",
      "I23",
      "I24",
      "I25"
    ],
    "ASSOCIATION": [],
    "DIFF": []
  },
  "Stroke": {
    "KEEP": [
      "G45",
      "G46",
      "I60",
      "I61",
      "I62",
      "I63",
      "I65",
      "I66",
      "I67",
      "I68",
      "I69"
    ],
    "ASSOCIATION": [
      "H340",
      "H341"
    ],
    "DIFF": []
  },
  "Shortness of Breadth": {
    "KEEP": [
      "I26",
      "I27",
      "I28",
      "I50",
      "J12",
      "J13",
      "J14",
      "J15",
      "J16",
      "J17",
      "J18",
      "J20",
      "J21",
      "J22",
      "J41",
      "J42",
      "J43",
      "J44",
      "J80",
      "J951",
      "J952",
      "J96",
      "R05",
      "R06",
      "R093"
    ],
    "ASSOCIATION": [],
    "DIFF": [
      "R53",
      "T17",
      "T180"
    ]
  }
}
```

