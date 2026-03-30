import hashlib
from pathlib import Path
from PIL import Image


def md5_file(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.md5(data).hexdigest()


def sha256_file(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def weak_hash_by_dimensions(path: Path) -> str:
    """
    Hash propositalmente fraco e didático.
    Usa apenas largura e altura da imagem.
    Imagens diferentes com mesmo tamanho gerarão o mesmo 'hash'.
    """
    with Image.open(path) as img:
        width, height = img.size
    return f"{width}x{height}"


def main():
    image1 = Path("images/aviao.jpeg")
    image2 = Path("images/navio.jpeg")

    if not image1.exists() or not image2.exists():
        print("Erro: verifique se as imagens estão em ./images/")
        return

    print("=== HASHES CRIPTOGRÁFICOS ===")
    md5_img1 = md5_file(image1)
    md5_img2 = md5_file(image2)

    sha256_img1 = sha256_file(image1)
    sha256_img2 = sha256_file(image2)

    print(f"Imagem 1 (MD5):    {md5_img1}")
    print(f"Imagem 2 (MD5):    {md5_img2}")
    print(f"Colisão em MD5?    {'SIM' if md5_img1 == md5_img2 else 'NÃO'}\n")

    print(f"Imagem 1 (SHA256): {sha256_img1}")
    print(f"Imagem 2 (SHA256): {sha256_img2}")
    print(f"Colisão em SHA256? {'SIM' if sha256_img1 == sha256_img2 else 'NÃO'}\n")

    print("=== HASH FRACO / DIDÁTICO ===")
    weak1 = weak_hash_by_dimensions(image1)
    weak2 = weak_hash_by_dimensions(image2)

    print(f"Imagem 1 (weak hash): {weak1}")
    print(f"Imagem 2 (weak hash): {weak2}")
    print(f"Colisão no hash fraco? {'SIM' if weak1 == weak2 else 'NÃO'}")

    if weak1 == weak2:
        print("\nConclusão:")
        print("As imagens são diferentes, mas geraram o mesmo hash fraco.")
        print("Isso demonstra o conceito de colisão de hash.")
    else:
        print("\nNão houve colisão no hash fraco.")


if __name__ == "__main__":
    main()
