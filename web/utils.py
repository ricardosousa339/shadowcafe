import os

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_ASSETS_DIR = os.path.join(_BASE_DIR, "assets")

def get_asset_path(filename: str) -> str:
    """Retorna o caminho completo de um asset procurando em assets e subdiretórios conhecidos."""
    # Se já existir direto em assets/
    direct = os.path.join(_ASSETS_DIR, filename)
    if os.path.exists(direct):
        return direct
    
    # Subpastas conhecidas
    subdirs = ["audio", "xicara", "cafeteria", "game_over", "fonts"]
    for subdir in subdirs:
        sub_path = os.path.join(_ASSETS_DIR, subdir, filename)
        if os.path.exists(sub_path):
            return sub_path
            
    # Fallback para o caminho direto
    return direct
