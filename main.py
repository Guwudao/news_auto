from extract_data.extract_papers import PaperExtractor
from extract_data.paper_model import PaperModel
import json
from core.config import configer


if __name__ == '__main__':
    with open('papers.json', encoding='utf-8') as file:
        paper_dict_list = json.loads(file.read())
        paper_model_list = [PaperModel(**paper_dict) for paper_dict in paper_dict_list]
        PaperExtractor.extract_paper_with_list(paper_model_list)

        print(configer.config)




