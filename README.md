# Mental Health EDA & Prediction

本專案針對全球心理健康數據進行探索性資料分析（EDA）與預測建模，數據來源於多個國家與地區的心理健康相關統計。

## 目錄結構

```
calldata.py
FunctionalDescribe.py
requirement.py
test.py
Dataset/
    Adult Population Major Depression Data.csv
    Anxiety Disorders Treatment Gap.csv
    Depressive Symptoms US Population.csv
    Mental Health Adult Population Data.csv
    Mental Health Burden by Illness.csv
    Mental Health Countries Data.csv
    Mental Illnesses Prevalence.csv
```

## 安裝需求

請先安裝必要的 Python 套件：

```sh
pip install -r requirement.py
```

## 使用說明

1. 將所有資料集放於 `Dataset/` 資料夾下。
2. 執行 `calldata.py` 以載入與預處理資料。
3. 使用 `FunctionalDescribe.py` 進行資料描述與初步分析。
4. 執行 `test.py` 進行模型測試與評估。

## 主要檔案說明

- `calldata.py`：資料載入與預處理腳本。
- `FunctionalDescribe.py`：資料描述性統計與視覺化分析。
- `requirement.py`：專案所需套件列表。
- `test.py`：模型測試與效能評估腳本。
- `Dataset/`：存放所有原始資料集的資料夾。

## 資料來源

- 各資料集來源請參考 `Dataset/` 內各檔案說明或原始出處。

## 聯絡方式

如有問題請聯絡 [你的名字或Email]。

---

歡迎貢獻與指教！
