import pandas as pd
import os
import json

def get_metadata(file_name):
    # Проверяем, существует ли файл в директории
    if not os.path.exists(file_name):
        print(f"Ошибка: Файл {file_name} не найден в {os.getcwd()}")
        return None

    try:
        # Читаем CSV
        df = pd.read_csv(file_name)
        
        # Собираем метаданные для нашего AI-агента
        metadata = {
            "filename": file_name,
            "rows": len(df),
            "cols_count": len(df.columns),
            "schema": []
        }

        for col in df.columns:
            stats = {
                "column": col,
                "type": str(df[col].dtype),
                "non_null_count": int(df[col].count()),
                "unique_values": int(df[col].nunique()),
                "examples": df[col].dropna().unique()[:3].tolist()
            }
            metadata["schema"].append(stats)
            
        return metadata

    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None

# Тестируем
if __name__ == "__main__":
    data = get_metadata('bd.csv')
    if data:
        print("Метаданные успешно собраны!")
        print(json.dumps(data, indent=4, ensure_ascii=False))
