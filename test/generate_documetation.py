from create_meta import get_csv_metadata
from logic import generate_ai_content

def run_pipeline(input_csv, output_md):
    print(f" Шаг 1: Анализ {input_csv}...")
    meta = get_csv_metadata(input_csv)
    
    print(" Шаг 2: Генерация текста через AI...")
    markdown_text = generate_ai_content(meta)
    
    print(f" Шаг 3: Сохранение в {output_md}...")
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    
    print(" Документация готова!")

if __name__ == "__main__":
    run_pipeline("bd.csv", "DATA_DOC.md")
