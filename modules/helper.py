from bs4 import BeautifulSoup
from pathlib import Path

# The images for questions are stored in the repository
REPOSITORY_LINK_FOR_PATH = "https://github.com/Prateek61/questions/blob/raw/"

def image_path_from_src(src: Path, img: str) -> str:
    # src is the path to the base questions folder
    # img is the path to the image from the base questions folder
    # Check if the image exists
    if not Path(src, img).exists():
        raise FileNotFoundError(f"Image {img} not found in {src}")
    # return the link to the image
    return f"{REPOSITORY_LINK_FOR_PATH}{src}/{img}?raw=true"

def html_body_from_file(folder_path: Path) -> BeautifulSoup:
    # check if folder_path/questions.html exists
    if not Path(folder_path, "questions.html").exists():
        raise FileNotFoundError(f"questions.html not found in {folder_path}")
    
    # open file
    with open(Path(folder_path, "questions.html"), "r") as f:
        html = f.read()
    # parse html
    soup = BeautifulSoup(html, "html.parser")
    # just keep the body
    soup = soup.body

    # Loop over all the images and change their src
    for img in soup.find_all("img"):
        # get the src
        src = img["src"]
        # change the src
        img["src"] = image_path_from_src(folder_path, src)

    # return the body
    return soup

def remove_tags_except_p_and_img(soup: BeautifulSoup) -> None:
    # remove all tags except <p> and <img> but keep their inner tags
    for tag in soup.find_all(True):
        if tag.name not in ["p", "img"]:
            tag.unwrap()

    



