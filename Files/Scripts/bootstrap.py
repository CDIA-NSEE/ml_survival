import os
import sys
import subprocess
import importlib.metadata as md
from pathlib import Path
from IPython.display import Javascript, display


REQ_DIR = Path("requirements")
REQ_DIR.mkdir(exist_ok=True)

_selected_groups = []


def _check_project():
    if PROJECT_PATH is None:
        raise Exception(
            "Projeto não configurado. "
            "Use set_project('/caminho/do/projeto')"
        )

def set_project(project_path):

    global PROJECT_PATH, REQ_DIR

    PROJECT_PATH = Path(project_path)

    if not PROJECT_PATH.exists():
        raise FileNotFoundError(
            f"Projeto não encontrado: {PROJECT_PATH}"
        )

    REQ_DIR = PROJECT_PATH / "requirements"

    if not REQ_DIR.exists():
        raise FileNotFoundError(
            f"Pasta requirements não encontrada em: {REQ_DIR}"
        )

    print(f"Projeto definido: {PROJECT_PATH}")


def _parse_requirements(req_file):
    packages = {}

    if not req_file.exists():
        return packages

    with open(req_file, "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "==" in line:
                pkg, version = line.split("==")
                packages[pkg.strip()] = version.strip()

    return packages


def _needs_install(pkg, required_version):
    try:
        installed = md.version(pkg)
        return installed != required_version
    except:
        return True

def _get_installed_version(pkg):
    try:
        return md.version(pkg)
    except md.PackageNotFoundError:
        return None

def setup():
    global _selected_groups

    available = sorted([f.stem for f in REQ_DIR.glob("*.txt")])

    print("\nGrupos disponíveis:")
    for i, g in enumerate(available, 1):
        print(f"{i}. {g}")
    print(f"{len(available)+1}. Criar novo grupo")

    raw = input("\nEscolha (ex: 1,3): ").strip()
    indices = [int(x.strip()) for x in raw.split(",")]

    selected = []

    for idx in indices:

        if idx == len(available) + 1:
            new_group = input("Nome do novo grupo: ").strip()

            if not new_group:
                print("Nome inválido.")
                continue

            req_file = REQ_DIR / f"{new_group}.txt"

            defaults = []
            for pkg in ("pandas", "numpy", "matplotlib"):
                v = _get_installed_version(pkg)
                if v:
                    defaults.append(f"{pkg}=={v}")

            req_file.write_text("\n".join(defaults))
            selected.append(new_group)

            print(f"\nNovo grupo criado: {new_group}")

            if defaults:
                print("Bibliotecas implementadas no notebook:")
                for dep in defaults:
                    print(f"  + {dep}")
            else:
                print("O arquivo não tem dependências a serem instaladas")

        elif 1 <= idx <= len(available):
            group = available[idx - 1]
            req_file = REQ_DIR / f"{group}.txt"

            selected.append(group)

            if req_file.exists():
                deps = [
                    line.strip()
                    for line in req_file.read_text().splitlines()
                    if line.strip() and not line.startswith("#")
                ]

                if deps:
                    print(f"\nLendo dependências de {group}:")

                    to_install = []

                    for dep in deps:
                        print(f"  - {dep}")

                        if "==" in dep:
                          pkg, required_version = dep.split("==")

                          if _needs_install(pkg.strip(), required_version.strip()):
                            to_install.append(dep)
                    
                    if not to_install:
                      print(
                        "\n Todas as depedendências já estão instaladas"
                        " nas versões do ambiente."
                      )
                    
                    else:
                      print("\n Instalando dependências necessárias:")
                      for dep in to_install:
                        print(f" + {dep}")
                      
                      result = subprocess.run(
                        ["pip", "install", *to_install],
                        check=False
                      )

                      if result.returncode == 0:
                        print("\n⚠️ Dependências instaladas.")
                        print("Reiniciando o kernel automaticamente...")
                        display(Javascript('google.colab.kernel.restart()'))
                        return
                else:
                    print(f"\n{group}: O arquivo não tem dependências a serem instaladas")

    _selected_groups = selected
    print(f"\nGrupos ativos: {_selected_groups}")

def sync(group, packages):
    """
    Sincroniza requirements sem sobrescrever versões existentes.

    Regras:
    - nova lib -> adiciona
    - mesma versão -> mantém
    - versão diferente -> alerta e NÃO altera
    """
    
    _check_project()

    req_file = REQ_DIR / f"{group}.txt"

    current = _parse_requirements(req_file)
    updated = False

    for pkg in packages:

        try:
            installed_version = md.version(pkg)

        except:
            print(f"[AVISO] {pkg} não está instalado.")
            continue

        if pkg not in current:
            current[pkg] = installed_version
            updated = True
            print(f"[ADICIONADO] {pkg}=={installed_version}")

        else:
            saved_version = current[pkg]

            if saved_version == installed_version:
                print(
                    f"[OK] {pkg} já registrado "
                    f"({saved_version})"
                )

            else:
                print(
                    f"[CONFLITO] {pkg}\n"
                    f"  versão salva:      {saved_version}\n"
                    f"  versão instalada:  {installed_version}\n"
                    f"  Mantendo versão original.\n"
                    f"  Preferível preservar a versão histórica "
                    f"para evitar incompatibilidade futura."
                )

    if updated:
        with open(req_file, "w") as f:
            for pkg in sorted(current):
                f.write(f"{pkg}=={current[pkg]}\n")

        print(f"\n{group}.txt atualizado.")

    else:
        print(f"\nNenhuma alteração realizada.")