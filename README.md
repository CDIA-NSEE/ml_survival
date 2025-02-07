# Study Machine Learning Survival  

Work still in progress...

## **Introduction**  

This study was developed by the **Núcleo de Sistemas Eletrônicos Embarcados (NSEE)** at **Instituto Mauá de Tecnologia**, in collaboration with **Fundação Oncocentro de São Paulo (FOSP)**, **Faculdade de Saúde Pública da USP (Universidade de São Paulo)**, and **A.C. Camargo Cancer Center**.  

The objective is to explore the application of **machine learning algorithms for survival analysis** to predict cancer patient survival and identify the most impactful variables in these predictions. The study includes data from patients diagnosed with **cervical, colorectal, lung, prostate, and breast cancer** between **2000 and 2024**.  

The dataset used in this research is **open-source** and is called **Registro Hospitalar de Câncer (RHC-SP)**, available on the [FOSP website](https://fosp.saude.sp.gov.br/fosp/diretoria-adjunta-de-informacao-e-epidemiologia/rhc-registro-hospitalar-de-cancer/banco-de-dados-do-rhc/).  

---

## **How to Run**  

To run the notebooks in this repository, follow these steps:  

1. Clone this repository to your local environment:  

    ```bash
    git clone https://github.com/CDIA-NSEE/ml_survival
    ```  

2. Open the notebooks using a **Python development environment**, preferably [Google Colaboratory](https://research.google.com/colaboratory/), but you can also use [Jupyter Notebook](https://jupyter.org/) or [VS Code](https://code.visualstudio.com/) locally.  

3. Install the required Python libraries.  

---

## **Setting Up the Project Locally**  

### **Creating the Virtual Environment (venv)**  

#### Windows  

```bash
python -m venv venv
```  

#### Linux  

```bash
virtualenv -p python3.10 venv
```  

### **Activating the Virtual Environment**  

#### Windows  

```bash
venv\Scripts\activate
```  

#### Linux  

```bash
source venv/bin/activate
```  

### **Installing Dependencies**  

```bash
pip install -e .
pip install -r requirements.txt
```  

---

## **Contributions**  

We welcome contributions from students, researchers, and data science enthusiasts. If you would like to contribute, follow these steps:  

1. **Fork** this repository.  
2. Make your modifications in your fork.  
3. Submit a **pull request**, describing your changes and the rationale behind them.  

---

## **Contact**  

For any questions or support, feel free to reach out via email:  

📧 [Lucas Buk Cardoso](mailto:lucas.cardoso@maua.br)  
📧 [NSEE](mailto:nsee@maua.br)  

---

## **Authors**  

- [Lucas Buk Cardoso](https://www.linkedin.com/in/lucasbukcardoso/) - Instituto Mauá de Tecnologia  
- Vanderlei Cunha Parro - Instituto Mauá de Tecnologia  
- Simone Aldrey Angelo - Instituto Mauá de Tecnologia  
- Yasmin Pacheco Gil Bonilha - Instituto Mauá de Tecnologia  
- Adeylson Ribeiro - Fundação Oncocentro de São Paulo (FOSP)  
- Fernando Maia - Faculdade de Saúde Pública da Universidade de São Paulo
- Nanci Utida - Faculdade de Saúde Pública da Universidade de São Paulo
- Maria Paula Curado - A.C. Camargo Cancer Center  
- Gisele Fernandes - A.C. Camargo Cancer Center  
- Victor Wünsch Filho - Fundação Oncocentro de São Paulo e Faculdade de Saúde Pública da Universidade de São Paulo  
- Tatiana Natasha Toporcov - Faculdade de Saúde Pública da Universidade de São Paulo  

